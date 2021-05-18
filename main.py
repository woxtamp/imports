from application.salary import Payments
from application.db.people import Employees
import datetime as dt

if __name__ == '__main__':
    print("main.py")

    pay = Payments()
    pay.calculate_salary()

    emp = Employees()
    emp.get_employees()

    print(f"Текущая дата: {dt.datetime.today().strftime('%x')}")
