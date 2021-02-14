Sales = input()
Sales = int(Sales)
if Sales <= 10000:
    Salary = float(1500 + Sales * 0.05)
elif Sales > 10000 and Sales < 50000:
    Salary = float((1500 + 10000 * 0.05) + ((Sales - 10000) * 0.03))
elif Sales > 50000:
    Salary = float((1500 + 10000 * 0.05) + ((50000 - 10000) * 0.03) +
                   ((Salary - 50000) * 0.02))
print('%.2f' % Salary)
