# SecuritiesPortfolioDEMO/models/bonds/government_bond.py
from models.bonds.bond import Bond

class GovernmentBond(Bond):
    def __init__(self, symbol: str, name: str, price: float, industry: str, volatility: str, bond_type: str = "government"):
        super().__init__(symbol, name, price, industry, volatility, bond_type)
