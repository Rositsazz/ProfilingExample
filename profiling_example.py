from time import sleep


class Employee:

    def __init__(self, name, position, salary, bank_number):
        self.name = name
        self.salary = salary
        self.position = position
        self.bank_number = bank_number
        sleep(0.5)

    def increase_salary(self, bonus):
        self.salary += bonus

    def promote_to(self, new_position):
        self.position = new_position

    def get_personal_bank_check(self):
        return EmpBank.check_bank_number(self.bank_number)


class Company:

    def __init__(self, name, field, employees=[]):
        self.name = name
        self.field = field
        self.employees = employees

    def increase_employee_salaries_with(self, bonus):
        for employee in self.employees:
            employee.increase_salary(bonus)

    def pay_all_employees(self):
        for employee in self.employees:
              bank_check = employee.get_personal_bank_check()
              if bank_check:
                  self.pay_salary(employee.salary, employee.bank_number)

    def pay_salary(self, employee_salary, bank_number):
        EmpBank.send_money(employee_salary, bank_number)


class EmpBank:

    @classmethod
    def check_bank_number(cls, bank_number):
          sleep(1)
          return True

    @classmethod
    def send_money(cls, amount, bank_number):
          sleep(1)



def main():
    emp1 = Employee('Thor', 'God of Thunder', 1000, 'AVENGERSBANK1001 ')
    emp2 = Employee('HULK', 'Hulk', 5000, 'AVENGERSBANK1002 ')
    emp3 = Employee('Steve', 'Caption America', 750, 'AVENGERSBANK1003 ')

    company = Company('Avengers', 'movie', [emp1, emp2, emp3])
    company.pay_all_employees()
    print('Salaries - paid')


if __name__ == '__main__':
    # --------

    # main()

    # --------

    # import cProfile
    # retval = cProfile.run('main()')
    # main()

    # --------

    import cProfile
    import io
    import pstats
    pr = cProfile.Profile()
    pr.enable()
    main()
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s)
    ps.dump_stats('profiling_result.dmp')
    # sortby = pstats.SortKey.CUMULATIVE
    # ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    # third example

    # with cProfile.Profile() as pr:
    #     main()
    # pr.print_stats()