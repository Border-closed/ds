#+Начальная сумма равна нулю
#+Допустимые действия: пополнить, снять, выйти
#+Сумма пополнения и снятия кратны 50 у.е.
#+Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#После каждой третей операции пополнения или снятия начисляются проценты - 3%
#+Нельзя снять больше, чем на счёте
#+При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
#Любое действие выводит сумму денег
#Дополнительно сохраняйте все операции поступления и снятия средств в список.

COMISSION = 0.015
TAX = 0.1
UP_TAX_LIMIT = 600
LOW_TAX_LIMIT = 30
ACC_LIMIT = 5000000
LIMIT_COUNT = 50
account_money = 0
operations_history = []

def operation_user():
    operation = input('Введите операцию: внести, снять или выйти ')
    if operation == 'выйти':
        return operation, 0  # Возвращаем 0, чтобы указать, что сумма не требуется
    elif operation in ('внести', 'снять'):
        return operation, count()
    else:
        return 'Такая команда не поддерживается '

def operation(operation_user, count):
    global account_money
    if operation_user == 'внести':
        account_money = plus(account_money, count)
    elif operation_user == 'снять':
        account_money = minus(account_money, count)
    elif operation_user == 'выйти':
        exit_app()
    else:
        print('Такая команда не поддерживается ')

def count():
    while True:
        count_str = input('Введите сумму кратную 50 ')
        try:
            count = int(count_str)
            if count % LIMIT_COUNT == 0:
                return count
            else:
                print('Вы ввели сумму не кратную 50. Попробуйте еще раз.')
        except ValueError:
            print('Вы ввели некорректное значение. Попробуйте еще раз.')

def plus(account_money, count):
    global operations_history
    if count == 0:
        print('Вы ввели сумму не кратную 50 ')
    else:
        account_money = limit(account_money) + count
        operations_history.append(f'Пополнение: +{count} у.е.')
    print_result(account_money)
    return account_money

def minus(account_money, count):
    global operations_history
    account_money_temp = limit(account_money) - count - percent(count)
    if account_money_temp < 0:
        print(f'Вы не можете снять такую сумму, у вас на счете {account_money} у.е.')
        result = account_money
    else:
        result = account_money_temp
        operations_history.append(f'Снятие: -{count} у.е.')
    print_result(result)
    return result

def limit(account_money):
    if account_money > ACC_LIMIT:
        account_money -= account_money * TAX
    return account_money

def percent(count):
    percent = COMISSION * count
    if percent < LOW_TAX_LIMIT:
        return LOW_TAX_LIMIT
    elif percent > UP_TAX_LIMIT:
        return UP_TAX_LIMIT
    else:
        return percent

def print_result(account_money):
    print('У вас', account_money, 'у.е. на счете')

def exit_app(operations_history):
    print('История операций:')
    for operation in operations_history:
        print(operation)
    print_result(account_money)
    exit()

for i in range(0, 10):
    operation_user_str, count_user_str = operation_user()
    if operation_user_str == 'выйти':
        exit_app(operations_history)
        break
    operation(operation_user_str, count_user_str)
