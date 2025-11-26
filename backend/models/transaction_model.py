from datetime import datetime

class Transaction:
    def __init__(self, buyer_id, seller_id, quantity, price, timestamp=None):
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return {
            "buyer_id": self.buyer_id,
            "seller_id": self.seller_id,
            "quantity": self.quantity,
            "price": self.price,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            buyer_id=data.get("buyer_id"),
            seller_id=data.get("seller_id"),
            quantity=data.get("quantity"),
            price=data.get("price"),
            timestamp=data.get("timestamp")
        )
