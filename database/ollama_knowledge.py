# SecuritiesPortfolioDEMO/database/ollama_knowledge.py
import sqlite3

DB_PATH = "database/ollama_knowledge.db"

def fetch_knowledge():
    """
    Resoring database information and returning dictionary
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT section, content FROM knowledge")
    data = cursor.fetchall()
    conn.close()
    return {section: content for section, content in data}

if __name__ == "__main__":
    knowledge_data = fetch_knowledge()
    if knowledge_data:
        print("Database uploaded!")
        for section, content in knowledge_data.items():
            print(f"\n📌 {section}:\n{content[:300]}...")
    else:
        print("Error! No information found.")
