from backend.database import get_factories, save_factories, get_transactions, save_transactions
from backend.models.transaction_model import Transaction

THRESHOLD = 1000

def update_carbon_produced(factory_id, amount):
    factories = get_factories()
    for f in factories:
        if f['factory_id'] == factory_id:
            f['carbon_produced'] = amount
            # Reset trading status based on new amount
            if amount > THRESHOLD:
                f['buy_quantity'] = amount - THRESHOLD
                f['selling_quantity'] = 0
            else:
                f['selling_quantity'] = THRESHOLD - amount
                f['buy_quantity'] = 0
            
            save_factories(factories)
            return {"success": "Carbon data updated", "data": f}
    return {"error": "Factory not found"}

def get_sellers():
    factories = get_factories()
    sellers = [f for f in factories if f['selling_quantity'] > 0 and f['price_per_ton'] > 0]
    return sellers

def set_selling_info(factory_id, quantity, price):
    factories = get_factories()
    for f in factories:
        if f['factory_id'] == factory_id:
            if quantity > (THRESHOLD - f['carbon_produced']):
                 return {"error": "Cannot sell more than available limit"}
            f['selling_quantity'] = quantity
            f['price_per_ton'] = price
            save_factories(factories)
            return {"success": "Selling info updated"}
    return {"error": "Factory not found"}

def buy_carbon(buyer_id, seller_id, quantity):
    factories = get_factories()
    buyer = next((f for f in factories if f['factory_id'] == buyer_id), None)
    seller = next((f for f in factories if f['factory_id'] == seller_id), None)

    if not buyer or not seller:
        return {"error": "Buyer or Seller not found"}

    if seller['selling_quantity'] < quantity:
        return {"error": "Not enough carbon available from this seller"}

    cost = quantity * seller['price_per_ton']
    
    # Update Buyer
    buyer['carbon_bought_as_per_now'] += quantity
    buyer['buy_quantity'] = max(0, buyer['buy_quantity'] - quantity)

    # Update Seller
    seller['selling_quantity'] -= quantity
    seller['sold_carbon'] += quantity

    save_factories(factories)

    # Record Transaction
    transactions = get_transactions()
    new_tx = Transaction(buyer_id, seller_id, quantity, cost)
    transactions.append(new_tx.to_dict())
    save_transactions(transactions)

    return {"success": "Transaction successful"}
