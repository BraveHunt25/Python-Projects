# Hernández Jiménez Erick Yael
# Last edited: 06-12-2024
# Excercise based on Federico Azzurro's "Learn Python By Coding: 10 Projects"
# Link to the course: https://www.udemy.com/course/10-mini-projects
def calculate_finances(monthly_income: float, tax_rate: float, expenses: dict = {}, currency: str = '$')->None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

    print('-'*30)
    print(f"Monthly income: {currency}{monthly_income:,.2f}")
    print(f"Tax rate: {tax_rate:,.0f}%")
    print(f"Monthly tax: {currency}{monthly_tax:,.2f}")
    print(f"Monthly net income: {currency}{monthly_net_income:,.2f}")
    print(f"Yearly salary: {currency}{yearly_salary:,.2f}")
    print(f"Yearly tax paid: {currency}{yearly_tax:,.2f}")
    print(f"Yearly net income: {currency}{yearly_net_income:,.2f}")
    income_left: float = monthly_net_income
    print("Expenses per month:")
    if expenses:
        for key, value in expenses.items():
            print(f"\t - {key}: {currency}{value}")
            income_left -= value
    else: 
        print(f"{currency}0")
    print(f"Monthly amount left: {currency}{income_left:,.2f}")
    yearly_income_left: float = income_left * 12
    print(f"Yearly amount left: {currency}{yearly_income_left:,.2f}")
    print('-'*30)

if __name__ == '__main__':
    while True:
        try:
            monthly_income: float = float(input("Enter your monthly salary: "))
            tax_rate: float = float(input("Enter your tax rate (%): "))
            break
        except (ValueError, TypeError) as e:
            print(f"{e}. Enter a valid number")
    currency: str = input("Enter the currency you work with: ")
    expenses: dict = {}
    print("Expenses:")
    while True:
        concept: str = str(input("Enter the concept of your expense (press 'enter' to exit): "))
        if concept:
            while True:
                try:
                    value: float = float(input("Enter the monthly amount paid: "))
                    expenses[concept] = value
                    break
                except (ValueError, TypeError) as e:
                    print(f"{e}. Enter a valid number")
        else:
            break
    calculate_finances(monthly_income, tax_rate, expenses, currency)
