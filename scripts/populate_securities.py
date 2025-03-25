# SecuritiesPortfolioDEMO/scripts/populate_securities.py
from database.db_manager import DatabaseManager

def populate_securities():
    db = DatabaseManager()
    
    # מניות טכנולוגיה
    db.insert_security("AAPL", "Apple Inc.", 150.0, "technology", "high", "stock", "common", "")
    db.insert_security("MSFT", "Microsoft Corporation", 300.0, "technology", "high", "stock", "common", "")
    db.insert_security("GOOG", "Alphabet Inc.", 2800.0, "technology", "high", "stock", "common", "")
    db.insert_security("FB", "Meta Platforms", 200.0, "technology", "high", "stock", "common", "")
    db.insert_security("NFLX", "Netflix Inc.", 500.0, "technology", "high", "stock", "common", "")
    
    # מניות מתעשיות שונות
    db.insert_security("TSLA", "Tesla Inc.", 700.0, "transportation", "high", "stock", "common", "")
    db.insert_security("AMZN", "Amazon.com Inc.", 3400.0, "industry and finance", "high", "stock", "common", "")
    db.insert_security("DIS", "Disney", 90.0, "consumer goods", "low", "stock", "common", "")
    db.insert_security("PG", "Procter & Gamble", 140.0, "consumer goods", "low", "stock", "common", "")
    db.insert_security("JNJ", "Johnson & Johnson", 165.0, "health care", "low", "stock", "common", "")
    
    # מניות מועדפות
    db.insert_security("PGP", "Procter & Gamble Preferred", 140.0, "consumer goods", "low", "stock", "preferred", "")
    db.insert_security("KO", "Coca-Cola Preferred", 55.0, "consumer goods", "low", "stock", "preferred", "")
    
    # מניות פיננסיות
    db.insert_security("JPM", "JPMorgan Chase", 160.0, "industry and finance", "medium", "stock", "common", "")
    db.insert_security("BAC", "Bank of America", 40.0, "industry and finance", "medium", "stock", "common", "")
    db.insert_security("WFC", "Wells Fargo", 45.0, "industry and finance", "medium", "stock", "common", "")
    
    # מניות מחוץ לארה״ב
    db.insert_security("TSM", "Taiwan Semiconductor", 120.0, "technology", "high", "stock", "common", "")
    db.insert_security("BABA", "Alibaba Group", 180.0, "technology", "high", "stock", "common", "")
    db.insert_security("SONY", "Sony Corporation", 100.0, "technology", "medium", "stock", "common", "")
    
    # אגרות חוב ממשלתיות
    db.insert_security("USGOV", "US Government Bond", 100.0, "industry and finance", "low", "bond", "", "government")
    db.insert_security("UKGOV", "UK Government Bond", 100.0, "industry and finance", "low", "bond", "", "government")
    
    # אגרות חוב תאגידיות
    db.insert_security("CORP1", "Corporate Bond 1", 100.0, "industry and finance", "high", "bond", "", "corporate")
    db.insert_security("CORP2", "Corporate Bond 2", 95.0, "industry and finance", "high", "bond", "", "corporate")
    db.insert_security("CORP3", "Corporate Bond 3", 105.0, "industry and finance", "high", "bond", "", "corporate")
    
    # אגרות חוב מקרקעין
    db.insert_security("REBD", "Real Estate Bond", 102.0, "real estate", "low", "bond", "", "real_estate")
    
    # עוד מניות – להשלמת 30 רשומות
    db.insert_security("V", "Visa Inc.", 220.0, "industry and finance", "medium", "stock", "common", "")
    db.insert_security("MA", "Mastercard Inc.", 350.0, "industry and finance", "medium", "stock", "common", "")
    db.insert_security("ADBE", "Adobe Inc.", 500.0, "technology", "high", "stock", "common", "")
    db.insert_security("ORCL", "Oracle Corporation", 90.0, "technology", "medium", "stock", "common", "")
    db.insert_security("CRM", "Salesforce.com Inc.", 250.0, "technology", "high", "stock", "common", "")
    db.insert_security("INTC", "Intel Corporation", 60.0, "technology", "medium", "stock", "common", "")
    db.insert_security("CSCO", "Cisco Systems", 55.0, "technology", "medium", "stock", "common", "")
    db.insert_security("XOM", "Exxon Mobil", 65.0, "energy and health care", "medium", "stock", "common", "")
    db.insert_security("CVX", "Chevron Corporation", 120.0, "energy and health care", "medium", "stock", "common", "")
    db.insert_security("PFE", "Pfizer Inc.", 40.0, "health care", "low", "stock", "common", "")
    db.insert_security("MRK", "Merck & Co.", 80.0, "health care", "low", "stock", "common", "")
    
    print("Database has been populated with sample securities.")

if __name__ == "__main__":
    populate_securities()
