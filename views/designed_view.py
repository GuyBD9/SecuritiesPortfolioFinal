# SecuritiesPortfolioDEMO/views/designed_view.py
import sys
import asyncio
import matplotlib
matplotlib.use("TkAgg")  # Force use of TkAgg backend for GUI support (or try "macosx" on macOS)
import matplotlib.pyplot as plt
from tabulate import tabulate
from colorama import Fore, Style, init
from controllers.portfolio_controller import PortfolioController
from controllers.ai_controller import AIController

# Initialize Colorama for colored terminal output
init(autoreset=True)

def print_banner():
    """
    Prints the application banner and available commands.
    """
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + " Welcome to the Securities Investment Manager ".center(60, "="))
    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + "Available Commands:")
    commands = [
        ["setrisk <low|medium|high>", "Set portfolio risk level"],
        ["buy <stock|bond> <symbol> <quantity>", "Buy securities"],
        ["sell <symbol> <quantity>", "Sell securities"],
        ["ai <question>", "Consult AI for investment advice"],
        ["show portfolio", "Display current portfolio"],
        ["show securities", "List available securities"],
        ["exit", "Exit the program"]
    ]
    print(tabulate(commands, headers=["Command", "Description"], tablefmt="fancy_grid"))
    print()

async def handle_ai(ai_controller, command):
    """
    Handles the AI query asynchronously.
    """
    question = command[3:].strip()
    answer = await ai_controller.consult_ai(question)
    print(Fore.MAGENTA + "AI Response:" + Fore.YELLOW, answer)

def handle_show_portfolio(portfolio_controller):
    """
    Displays the portfolio in detail:
    - A table with Stock Name, Ticker, Price, Quantity, Value, and Share (%).
    - A bar chart showing the portfolio composition by share percentage.
    """
    if not portfolio_controller.portfolio:
        print(Fore.RED + "Portfolio is empty. Please buy some securities to display the portfolio chart.")
        return

    # Calculate total portfolio value
    total_portfolio_value = sum(sec.price * qty for sec, qty in portfolio_controller.portfolio.items())
    
    # Build a list of data rows for the table
    data = []
    for sec, qty in portfolio_controller.portfolio.items():
        sec_value = sec.price * qty
        share_percentage = (sec_value / total_portfolio_value) * 100 if total_portfolio_value > 0 else 0
        data.append([
            sec.name,                  # Security name
            sec.symbol,                # Ticker
            f"{sec.price:.2f}",        # Unit price
            qty,                       # Held quantity
            f"{sec_value:.2f}",        # Held value
            f"{share_percentage:.2f}%"  # Percentage of total portfolio
        ])

    # Print the table
    print(Fore.CYAN + "\nDetailed Portfolio:")
    headers = ["Stock Name", "Ticker", "Price ($)", "Quantity", "Value ($)", "Share (%)"]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

    # Prepare data for the bar chart
    names = [row[0] for row in data]  # Security names
    shares = [float(row[5].replace('%', '')) for row in data]  # Percentage values (without '%')
    
    # Create the bar chart
    plt.figure(figsize=(9, 5))
    plt.bar(names, shares, color='skyblue')
    plt.title("Portfolio Composition by Stock")
    plt.xlabel("Stock Name")
    plt.ylabel("Share (%)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()  # Adjust layout to fit labels
    print(Fore.GREEN + "Displaying chart... Please close the window to continue.")
    plt.show(block=True)  # Show the plot and block until the window is closed
    print(Fore.GREEN + "Chart window closed.")

def start_repl():
    """
    Starts the command-line REPL for interacting with the Securities Investment Manager.
    """
    portfolio_controller = PortfolioController(risk_level="Low Risk")
    ai_controller = AIController()

    print_banner()
    
    while True:
        command = input(Fore.BLUE + ">> " + Style.RESET_ALL).strip().lower()
        if command in ['exit', 'quit']:
            portfolio_controller.save_portfolio_to_db()
            print(Fore.RED + "Exiting... Goodbye!")
            sys.exit()
        elif command.startswith("setrisk"):
            try:
                _, level = command.split()
                portfolio_controller.set_risk_level(level.capitalize() + " Risk")
                print(Fore.GREEN + "Risk level set to:", portfolio_controller.risk_level)
            except ValueError:
                print(Fore.RED + "Usage: setrisk <low|medium|high>")
        elif command.startswith("buy"):
            parts = command.split()
            if len(parts) != 4:
                print(Fore.RED + "Usage: buy <stock|bond> <symbol> <quantity>")
                continue
            _, sec_type, symbol, qty = parts
            try:
                qty = int(qty)
            except ValueError:
                print(Fore.RED + "Quantity must be an integer.")
                continue
            result = asyncio.run(portfolio_controller.buy_security(sec_type, symbol, qty))
            print(Fore.GREEN + result)
        elif command.startswith("sell"):
            parts = command.split()
            if len(parts) != 3:
                print(Fore.RED + "Usage: sell <symbol> <quantity>")
                continue
            _, symbol, qty = parts
            try:
                qty = int(qty)
            except ValueError:
                print(Fore.RED + "Quantity must be an integer.")
                continue
            result = asyncio.run(portfolio_controller.sell_security(symbol, qty))
            print(Fore.GREEN + result)
        elif command.startswith("ai"):
            asyncio.run(handle_ai(ai_controller, command))
        elif command.startswith("show portfolio"):
            handle_show_portfolio(portfolio_controller)
        elif command.startswith("show securities"):
            from database.db_manager import DatabaseManager
            db = DatabaseManager()
            securities = db.get_all_securities()
            if securities:
                headers = ["Symbol", "Name", "Price", "Sector", "Volatility", "Type", "Stock Type", "Bond Type"]
                print(tabulate(securities, headers=headers, tablefmt="fancy_grid"))
            else:
                print(Fore.RED + "No securities found in the database.")
        else:
            print(Fore.RED + "Unknown command. Please try again.")

if __name__ == "__main__":
    start_repl()
