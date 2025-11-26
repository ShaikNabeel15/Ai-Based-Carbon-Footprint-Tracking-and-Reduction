import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

def get_ai_suggestions(carbon_produced, factory_type="General"):
    if not API_KEY:
        return "AI suggestions unavailable (API Key missing)."
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"""
    You are an expert environmental consultant. A {factory_type} factory has produced {carbon_produced} tons of carbon.
    The government threshold is 1000 tons.
    
    If they are above the threshold, provide 3 specific, actionable steps to reduce emissions immediately.
    If they are below, provide 3 tips to maintain low emissions and potentially sell more credits.
    
    Format the output as a simple HTML list (<ul><li>...</li></ul>).
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text
        # Clean up markdown formatting
        text = text.replace("```html", "").replace("```", "")
        return text
    except Exception as e:
        return f"Error generating suggestions: {str(e)}"

def get_admin_summary(factories, transactions):
    if not API_KEY:
        return "AI summary unavailable."

    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"""
    Analyze the following carbon trading market data:
    Factories: {factories}
    Transactions: {transactions}
    
    Provide a concise executive summary for the admin.
    Highlight:
    1. Total market emissions.
    2. Most polluting factory.
    3. Most active trader.
    4. Any anomalies or risks.
    
    Format as HTML.
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text
        # Clean up markdown formatting
        text = text.replace("```html", "").replace("```", "")
        return text
    except Exception as e:
        return f"Error generating summary: {str(e)}"
