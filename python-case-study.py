# Question 1: Basic Salary Calculation
print("**************************************")
def calculate_basic_salary(hourly_rate, hours_worked):
    return hourly_rate * hours_worked

print("Calculates the basic salary of an employee:~")
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked: "))
basic_salary = calculate_basic_salary(hourly_rate, hours_worked)
print(f"Basic Salary: ${basic_salary:.2f}")
print("--------------------------------------")

# Question 2: Overtime Pay Calculation
def calculate_overtime_pay(hourly_rate, hours_worked):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
    else:
        overtime_pay = 0
    return overtime_pay

print("Calculate overtime pay for an employee:~")
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked: "))
overtime_pay = calculate_overtime_pay(hourly_rate, hours_worked)
print(f"Overtime Pay: ${overtime_pay:.2f}")
print("--------------------------------------")

# Question 3: Total Pay with Tax Deduction
def calculate_total_pay(basic_salary, tax_rate):
    tax_deduction = basic_salary * (tax_rate / 100)
    total_pay = basic_salary - tax_deduction
    return total_pay, tax_deduction

print("Calculates the total pay of an employee:~")
basic_salary = float(input("Enter basic salary: "))
tax_rate = float(input("Enter tax rate(%): "))
total_pay, tax_deduction = calculate_total_pay(basic_salary, tax_rate)
print(f"Tax Deduction: ${tax_deduction:.2f}")
print(f"Total Pay after Tax: ${total_pay:.2f}")
print("--------------------------------------")

# Question 4: Bonus and Total Pay
def calculate_bonus_and_total_pay(basic_salary, bonus_percentage):
    bonus = basic_salary * (bonus_percentage / 100)
    total_pay = basic_salary + bonus
    return bonus, total_pay

print("Calculates an employee's bonus and total pay")
basic_salary = float(input("Enter basic salary: "))
bonus_percentage = float(input("Enter bonus percentage: "))
bonus, total_pay = calculate_bonus_and_total_pay(basic_salary, bonus_percentage)
print(f"Bonus: ${bonus:.2f}")
print(f"Total Pay with Bonus: ${total_pay:.2f}")
print("--------------------------------------")

# Question 5: Total Payroll Calculation
def calculate_total_payroll(hourly_rate, hours_worked, tax_rate, bonus_percentage):
    basic_salary = calculate_basic_salary(hourly_rate, hours_worked)
    overtime_pay = calculate_overtime_pay(hourly_rate, hours_worked)
    tax_deduction = basic_salary * (tax_rate / 100)
    bonus = basic_salary * (bonus_percentage / 100)
    total_payroll = basic_salary + overtime_pay - tax_deduction + bonus
    return {
        "Basic Salary": basic_salary,
        "Overtime Pay": overtime_pay,
        "Tax Deduction": tax_deduction,
        "Bonus": bonus,
        "Total Payroll": total_payroll
    }

print("Calculates the total payroll:~")
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked: "))
tax_rate = float(input("Enter tax rate (%): "))
bonus_percentage = float(input("Enter bonus percentage (%): "))
payroll = calculate_total_payroll(hourly_rate, hours_worked, tax_rate, bonus_percentage)

for key, value in payroll.items():
    print(f"{key}: ${value:.2f}")
    print("--------------------------------------")

# Question 6: Monthly Salary Calculation
def calculate_monthly_salary(hourly_rate, weekly_hours):
    weekly_salary = calculate_basic_salary(hourly_rate, weekly_hours)
    monthly_salary = weekly_salary * 4  # Assuming 4 weeks in a month
    return monthly_salary

print("Calculates the monthly salary of an employee based on their hourly rate and weekly hours worked:~")
hourly_rate = float(input("Enter hourly rate: "))
weekly_hours = float(input("Enter weekly hours worked: "))
monthly_salary = calculate_monthly_salary(hourly_rate, weekly_hours)
print(f"Monthly Salary: ${monthly_salary:.2f}")
print("**************************************")
 