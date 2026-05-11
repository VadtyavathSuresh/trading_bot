import logging
from bot.validators import validate_side, validate_type
from bot.client import get_client

def place_order(symbol, side, order_type, quantity, price=None):
    side = validate_side(side)
    order_type = validate_type(order_type)

    params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("price is required for LIMIT orders")
        params["price"] = price
        params["timeInForce"] = "GTC"

    logging.info("Request: %s", params)

    try:
        client = get_client()
        response = client.futures_create_order(**params)
        logging.info("Response: %s", response)
        return {
            "success": True,
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice"),
        }
    except Exception as e:
        logging.exception("Order failed")
        return {"success": False, "error": str(e)}
