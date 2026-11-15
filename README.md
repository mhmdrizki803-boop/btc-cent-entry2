# btc-cent-forecast-01 entry

`main.py` guesses the BTC price 240 minutes after each checkpoint: a 30% pull from the last close toward the mean of the last 1,440 closes.

    MAKEFUN_INPUT_DIR=input MAKEFUN_OUTPUT_DIR=out python3 main.py

MIT licensed (see LICENSE).
