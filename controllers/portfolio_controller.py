# SecuritiesPortfolioDEMO/controllers/portfolio_controller.py
import asyncio
from database.db_manager import DatabaseManager
from risk.risk_calculator import calculate_portfolio_risk, classify_risk

class PortfolioController:
    def __init__(self, risk_level: str = "Low Risk", db_manager=None):
        self.risk_level = risk_level
        self.portfolio = {}  
        self.db_manager = db_manager or DatabaseManager()
        self._load_portfolio_from_db()
    
    def _load_portfolio_from_db(self):
        query = "SELECT symbol, name, price, quantity, total_value FROM portfolio"
        loaded_data = self.db_manager.fetch_all(query)
        for symbol, name, price, quantity, _ in loaded_data:
            security = self.create_security(symbol, name, price)
            self.portfolio[security] = quantity

    def save_portfolio_to_db(self):
        # clean and add updated security
        self.db_manager.execute_query("DELETE FROM portfolio")
        for security, qty in self.portfolio.items():
            total_value = security.price * qty
            self.db_manager.execute_query(
                """
                INSERT INTO portfolio (symbol, name, price, quantity, total_value)
                VALUES (?, ?, ?, ?, ?)
                """,
                (security.symbol, security.name, security.price, qty, total_value)
            )

    @staticmethod
    def create_security(symbol, name, price):
        # base decision create bond if = "bond"
        if "bond" in name.lower():
            from models.bonds.corporate_bond import CorporateBond
            return CorporateBond(symbol, name, price, industry="Unknown", volatility="low", bond_type="corporate")
        else:
            from models.stocks.common_stock import CommonStock
            return CommonStock(symbol, name, price, dividend_yield=0.0, industry="Unknown", volatility="low")

    async def buy_security(self, sec_type: str, symbol: str, quantity: int) -> str:
        # simulate in imaginary price for buying security
        security = self.create_security(symbol, f"{symbol} {sec_type.title()}", 100.0)
        current_qty = self.portfolio.get(security, 0)
        self.portfolio[security] = current_qty + quantity
        self.db_manager.save_transaction("buy", security, quantity)
        return f"Purchused {quantity} units from {security}"

    async def sell_security(self, symbol: str, quantity: int) -> str:
        found = None
        for security in self.portfolio:
            if security.symbol.lower() == symbol.lower():
                found = security
                break
        if found:
            current_qty = self.portfolio[found]
            if current_qty < quantity:
                return f"Not enough units for sale: {current_qty}"
            self.portfolio[found] = current_qty - quantity
            if self.portfolio[found] == 0:
                del self.portfolio[found]
            self.db_manager.save_transaction("sell", found, quantity)
            return f"Sold {quantity} units from {security}"
        else:
            return f"Security {symbol} is not available"

    def set_risk_level(self, risk_level: str):
        self.risk_level = risk_level

    def calculate_portfolio_risk(self) -> str:
        risk_score = calculate_portfolio_risk(self.portfolio)
        return classify_risk(risk_score)
