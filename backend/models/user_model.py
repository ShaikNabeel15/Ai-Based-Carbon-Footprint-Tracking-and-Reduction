class User:
    def __init__(self, factory_name, factory_id, mail_id, password, carbon_produced=0, selling_quantity=0, buy_quantity=0, price_per_ton=0, sold_carbon=0, carbon_bought_as_per_now=0):
        self.factory_name = factory_name
        self.factory_id = factory_id
        self.mail_id = mail_id
        self.password = password
        self.carbon_produced = carbon_produced
        self.selling_quantity = selling_quantity
        self.buy_quantity = buy_quantity
        self.price_per_ton = price_per_ton
        self.sold_carbon = sold_carbon
        self.carbon_bought_as_per_now = carbon_bought_as_per_now

    def to_dict(self):
        return {
            "factory_name": self.factory_name,
            "factory_id": self.factory_id,
            "mail_id": self.mail_id,
            "password": self.password,
            "carbon_produced": self.carbon_produced,
            "selling_quantity": self.selling_quantity,
            "buy_quantity": self.buy_quantity,
            "price_per_ton": self.price_per_ton,
            "sold_carbon": self.sold_carbon,
            "carbon_bought_as_per_now": self.carbon_bought_as_per_now
        }

    @staticmethod
    def from_dict(data):
        return User(
            factory_name=data.get("factory_name"),
            factory_id=data.get("factory_id"),
            mail_id=data.get("mail_id"),
            password=data.get("password"),
            carbon_produced=data.get("carbon_produced", 0),
            selling_quantity=data.get("selling_quantity", 0),
            buy_quantity=data.get("buy_quantity", 0),
            price_per_ton=data.get("price_per_ton", 0),
            sold_carbon=data.get("sold_carbon", 0),
            carbon_bought_as_per_now=data.get("carbon_bought_as_per_now", 0)
        )
