def calculus(salary):
    if salary > 2000.00:
        new_salary = salary + (salary * (4/100))
        reajust = new_salary - salary
        percentage = 4
        return new_salary, reajust, percentage
    elif salary > 1200.00:
        new_salary = salary + (salary * (7/100))
        reajust = new_salary - salary
        percentage = 7
        return new_salary, reajust, percentage
    elif salary > 800.00:
        new_salary = salary + (salary * (10/100))
        reajust = new_salary - salary
        percentage = 10
        return new_salary, reajust, percentage
    elif salary > 400.00:
        new_salary = salary + (salary * (12/100))
        reajust = new_salary - salary
        percentage = 12
        return new_salary, reajust, percentage
    else:
        new_salary = salary + (salary * (15/100))
        reajust = new_salary - salary
        percentage = 15
        return new_salary, reajust, percentage


salary = float(input())

print(f'Novo salario: {calculus(salary)[0]:.2f}')
print(f'Reajuste ganho: {calculus(salary)[1]:.2f}')
print(f'Em percentual: {calculus(salary)[2]} %')
