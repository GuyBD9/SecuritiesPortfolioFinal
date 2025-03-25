# SecuritiesPortfolioDEMO/models/bonds/corporate_bond.py
from models.bonds.bond import Bond

class CorporateBond(Bond):
    def __init__(self, symbol: str, name: str, price: float, industry: str, volatility: str, bond_type: str = "corporate"):
        super().__init__(symbol, name, price, industry, volatility, bond_type)
