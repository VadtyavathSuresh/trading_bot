# Binance Futures Testnet Trading Bot

A Python CLI application to place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features
- MARKET and LIMIT orders
- BUY and SELL support
- Input validation
- Logging to `logs/trading_bot.log`
- Error handling
- `.env` configuration

## Setup

```bash
git clone <your-repo-url>
cd trading_bot_submission
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file from `.env.example` and add your Binance testnet API credentials.

## Usage

### MARKET Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Assumptions
- User has a Binance Futures Testnet account and API credentials.
- Testnet base URL: https://testnet.binancefuture.com
