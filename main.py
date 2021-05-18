from application.salary import Payments
from db.people import Employees
import datetime as date

if __name__ == '__main__':
    pay = Payments()
    pay.calculate_salary()
    empl = Employees()
    empl.get_employees()
    print(date.datetime.today())
