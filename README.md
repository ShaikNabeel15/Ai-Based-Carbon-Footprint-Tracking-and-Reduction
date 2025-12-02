# 🏭 AI-Based Carbon Footprint Tracking & Reduction

### README.md

## 📌 1. Overview

This project is an **AI-driven carbon footprint tracking and carbon
trading platform**.\
Factories enter their carbon output, and the system checks if they
exceed the government threshold of **1000 tons**.

Based on this: - Below 1000 tons → Factory becomes a Seller - Above 1000
tons → Factory must Buy carbon credits

The system includes: - Factory onboarding\
- Carbon input dashboard\
- Automated AI analysis\
- Buy/Sell pages\
- Transaction logging\
- Admin portal\
- AI recommendations using Google Gemini

## 📌 Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/carbon_ai_agent.git
    cd carbon_ai_agent
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## 📌 Usage

1.  **Run the application:**

    ```bash
    python backend/app.py
    ```

2.  **Access the platform:**
    Open your browser and navigate to `http://127.0.0.1:5000`.


## 📌 2. System Flow

    Signup/Login → Dashboard → Input Carbon →  
    AI Analysis → Threshold Check →  
        < 1000 tons → Sell Page  
        > 1000 tons → Buy Page  
    → Transaction Handling → History → Admin → AI Suggestions

## 📌 3. Tech Stack

  Component   Technology
  ----------- ------------------------
  Frontend    HTML, CSS, JS
  Backend     Python (Flask/FastAPI)
  Database    JSON
  AI Model    Google Gemini
  Auth        bcrypt

## 📌 4. Project Folder Structure

    carbon_ai_agent/
    ├── backend/
    │   ├── app.py
    │   ├── auth.py
    │   ├── carbon_logic.py
    │   ├── ai_agent.py
    │   ├── database.py
    │   ├── models/
    │   └── utils/
    ├── data/
    ├── frontend/
    └── README.md

## 📌 5. Database Structure

### factories.json

``` json
[
  {
    "factory_name": "fact1",
    "factory_id": "f001",
    "mail_id": "fact1@gmail.com",
    "password": "hashed_password",
    "carbon_produced": 0
  }
]
```

### transactions.json

``` json
[
  {
    "buyer_id": "f002",
    "seller_id": "f001",
    "quantity": 100,
    "price": 500
  }
]
```

## 📌 6. Backend Components

-   app.py → Main server\
-   auth.py → Authentication\
-   carbon_logic.py → Threshold & trading logic\
-   ai_agent.py → Gemini-based insights\
-   database.py → JSON read/write

## 📌 7. AI Agent Capabilities

-   Predict emissions\
-   Generate reduction tips\
-   Rank sellers\
-   Admin analytics

## 📌 8. Frontend Pages

-   signup.html\
-   login.html\
-   dashboard.html\
-   carbon_input.html\
-   buy_page.html\
-   sell_page.html\
-   history.html\
-   admin_dashboard.html

## 📌 9. Required Python Packages

    pip install flask bcrypt google-generativeai python-dotenv

## 📌 10. Summary

Full AI-powered carbon trading ecosystem with: - Authentication\
- Factory dashboard\
- Buy/Sell flows\
- Admin panel\
- AI insights


