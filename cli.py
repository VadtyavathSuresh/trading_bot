import argparse
from bot.logging_config import setup_logging
from bot.orders import place_order

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)
    args = parser.parse_args()

    result = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price,
    )
    print(result)

if __name__ == "__main__":
    main()
