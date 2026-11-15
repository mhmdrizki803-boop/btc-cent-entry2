# btc-cent-forecast-01 entry

[![make.fun](https://make.fun/badge/btc-cent-forecast-01.svg)](https://make.fun/bounty/btc-cent-forecast-01)
[![rank](https://make.fun/badge/btc-cent-forecast-01/mhmdrizki803-boop/btc-cent-entry2/rank.svg)](https://make.fun/bounty/btc-cent-forecast-01)
[![reward](https://make.fun/badge/btc-cent-forecast-01/mhmdrizki803-boop/btc-cent-entry2/reward.svg)](https://make.fun/bounty/btc-cent-forecast-01)

`main.py` guesses the BTC price 240 minutes after each checkpoint: a 30% pull from
the last close toward the mean of the last 1,440 one-minute closes. Tuned on 264
walk-forward checkpoints over the kit's six practice series (MAE 417 USD against
438 for the last-close baseline).

    MAKEFUN_INPUT_DIR=input MAKEFUN_OUTPUT_DIR=out python3 main.py

Bounty page: https://make.fun/bounty/btc-cent-forecast-01

MIT licensed (see LICENSE).
