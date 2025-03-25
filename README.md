# SecuritiesPortfolioFinal
The models define the data structures and business rules. They represent securities such as stocks (common and preferred) and bonds (corporate and government) and provide methods to update prices and calculate risk.
# SecuritiesPortfolioDEMO

SecuritiesPortfolioDEMO is a command-line interface (CLI) application for managing an investment portfolio. Built in Python, the project follows modern design principles such as MVC (Model-View-Controller) and SOLID to ensure a modular, scalable, and maintainable codebase. The application allows users to buy and sell securities, consult an integrated AI service for investment advice, and view detailed portfolio reports with both textual and graphical visualizations.

## Features

- **Portfolio Management:**  
  - Buy and sell securities.
  - Automatically save portfolio data to a SQLite database.
- **AI Consultation:**  
  - Ask investment-related questions using an integrated AI service.
- **Graphical Visualizations:**  
  - Display detailed portfolio data in a table.
  - Visualize portfolio composition with bar charts.
- **Modular Architecture:**  
  - Built using MVC and SOLID principles for clear separation of concerns.

## Folder Structure

SecuritiesPortfolioDEMO/
├── ai/
│ └── ollama_model.py ├── controllers/
│ ├── ai_controller.py
│ └── portfolio_controller.py ├── database/
│ ├── db_manager.py
│ └── ollama_knowledge.py ├── models/
│ ├── security.py
│ ├── stocks/
│ │ ├── stock.py
│ │ ├── common_stock.py │ │ └── preferred_stock.py │ └── bonds/
│ ├── bond.py
│ ├── corporate_bond.py │ └── government_bond.py ├── risk/
│ ├── consts.py
│ └── risk_calculator.py
├── scripts/
│ └── populate_securities.py ├── views/
│ ├── console_view.py
│ ├── designed_view.py
│ └── portfolio_view.py
└── main.py
