class Colors:
    RESET = "\033[0m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    BLUE = "\033[34m"

class ROICalculator:
    def __init__(self):
        self.property_price = 0
        self.monthly_rental_income = 0
        self.annual_expenses = 0

    def gather_user_input(self):
        self.property_price = float(input(f"{Colors.BLUE}Enter the property price: {Colors.RESET}"))
        self.monthly_rental_income = float(input(f"{Colors.BLUE}Enter the monthly rental income: {Colors.RESET}"))
        self.annual_expenses = float(input(f"{Colors.BLUE}Enter the annual property expenses: {Colors.RESET}"))

    def calculate_roi(self):
        annual_income = self.monthly_rental_income * 12
        annual_profit = annual_income - self.annual_expenses
        roi = (annual_profit / self.property_price) * 100
        return roi

    def run(self):
        self.gather_user_input()
        roi = self.calculate_roi()

        if roi >= 0:
            roi_text = f"{Colors.GREEN}{roi:.2f}%{Colors.RESET}"
        else:
            roi_text = f"{Colors.RED}{roi:.2f}%{Colors.RESET}"

        print(f"The Return on Investment (ROI) for the property is: {roi_text}")

if __name__ == "__main__":
    roi_calculator = ROICalculator()
    roi_calculator.run()
