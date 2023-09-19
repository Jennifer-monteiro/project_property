
class Colors:
    RESET = "\033[0m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    BLUE = "\033[34m"

def calculate_roi(property_price, monthly_rental_income, annual_expenses):
    annual_income = monthly_rental_income * 12
    annual_profit = annual_income - annual_expenses
    roi = (annual_profit / property_price) * 100
    return roi

def main():
    property_price = float(input(f"{Colors.BLUE}Enter the property price: {Colors.RESET}"))
    monthly_rental_income = float(input(f"{Colors.BLUE}Enter the monthly rental income: {Colors.RESET}"))
    annual_expenses = float(input(f"{Colors.BLUE}Enter the annual property expenses: {Colors.RESET}"))

    roi = calculate_roi(property_price, monthly_rental_income, annual_expenses)

    if roi >= 0:
        roi_text = f"{Colors.GREEN}{roi:.2f}%{Colors.RESET}"
    else:
        roi_text = f"{Colors.RED}{roi:.2f}%{Colors.RESET}"

    print(f"The Return on Investment (ROI) for the property is: {roi_text}")

if __name__ == "__main__":
    main()
