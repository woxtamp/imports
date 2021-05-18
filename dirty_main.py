from application.salary import *
from db.people import *
from datetime import *

if __name__ == '__main__':
    pay = Payments()
    pay.calculate_salary()
    empl = Employees()
    empl.get_employees()
    print(datetime.today())
