import json, os, statistics

IN_DIR = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

WINDOW = 1440
PULL = 0.3

def forecast(prices):
    if not prices:
        return 1.0
    last = prices[-1]
    if len(prices) < 2:
        return last
    window = prices[-WINDOW:]
    mean = statistics.fmean(window)
    guess = last + PULL * (mean - last)
    return min(max(guess, 1e-9), 10000000.0 - 1e-9)

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for name in sorted(os.listdir(IN_DIR)):
        if not name.endswith(".in"):
            continue
        with open(os.path.join(IN_DIR, name)) as f:
            data = json.load(f)
        out = {"forecasts": []}
        for m in data.get("markets", []):
            case_id = m.get("id", data.get("case"))
            out["forecasts"].append({"case": case_id, "price": forecast(m.get("prices", []))})
        stem = name[:-3] + ".out"
        with open(os.path.join(OUT_DIR, stem), "w") as f:
            json.dump(out, f)

main()
# guess: each checkpoint forecasts the BTC price 240 minutes ahead as 30% of the way from the last close toward the 1,440-close mean
