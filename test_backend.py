import unittest
import os
import json
from backend.auth import signup_user, login_user
from backend.carbon_logic import update_carbon_produced, set_selling_info, buy_carbon
from backend.database import save_factories, save_transactions

class TestCarbonApp(unittest.TestCase):
    def setUp(self):
        # Reset data for testing
        save_factories([])
        save_transactions([])

    def test_auth(self):
        # Signup
        res = signup_user("Factory A", "f001", "a@test.com", "password123")
        self.assertIn("success", res)
        
        # Login
        res = login_user("a@test.com", "password123")
        self.assertIn("success", res)
        self.assertEqual(res['user']['factory_id'], "f001")

    def test_carbon_logic(self):
        signup_user("Factory A", "f001", "a@test.com", "password123")
        signup_user("Factory B", "f002", "b@test.com", "password123")

        # Factory A: High Carbon (Buyer)
        update_carbon_produced("f001", 1200)
        res = login_user("a@test.com", "password123")
        self.assertEqual(res['user']['buy_quantity'], 200)

        # Factory B: Low Carbon (Seller)
        update_carbon_produced("f002", 800)
        res = login_user("b@test.com", "password123")
        self.assertEqual(res['user']['selling_quantity'], 200)

        # Factory B lists for sale
        set_selling_info("f002", 100, 50) # 100 tons at $50/ton
        
        # Factory A buys
        buy_carbon("f001", "f002", 50)
        
        # Verify balances
        res_a = login_user("a@test.com", "password123")
        res_b = login_user("b@test.com", "password123")
        
        self.assertEqual(res_a['user']['carbon_bought_as_per_now'], 50)
        self.assertEqual(res_b['user']['sold_carbon'], 50)
        self.assertEqual(res_b['user']['selling_quantity'], 50)

if __name__ == '__main__':
    unittest.main()
