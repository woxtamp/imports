from application import *
from datetime import *

if __name__ == '__main__':
    print("dirty_main.py")

    pay = salary.Payments()
    pay.calculate_salary()

    emp = people.Employees()
    emp.get_employees()

    print(f"Текущая дата: {datetime.today().strftime('%x')}")
