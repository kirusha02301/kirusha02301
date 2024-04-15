print('0 в качестве знака операции'
      '\nзавершит работу программы\n')

while True:
    s = input('Знак (+, -, *, /): ')
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input('a = '))
        b = float(input('b = '))
        if s == '+':
            print('%.2f' % (a + b))
        elif s == '-':
            print('%.2f' % (a - b))
        elif s == '*':
            print('%.2f' % (a * b))
        elif s == '/':
            if b != 0:
                print('%.2f' % (a / b))
            else:
                print('Деление на ноль!')
    else:
        print('Неверный знак операции!')
print('0 в качестве знака - выход из программы\n')

while True:
    s = input('Знак (+, -, *, /): ')
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input('a = '))
        b = float(input('b = '))
        match s:
            case '+':
                print('%.2f' % (a + b))
            case '-':
                print('%.2f' % (a - b))
            case '*':
                print('%.2f' % (a * b))
            case '/':
                if b != 0:
                    print('%.2f' % (a / b))
                else:
                    print('Деление на ноль!')
    else:
        print('Неверный знак операции!')
# Запрашиваем у пользователя желаемое действие
operation = input(message)​
 
# Выводим сообщение о выбранной операции или что она отсутствует
if operation == '+':
   print('Сложение')
elif operation == '-':
   print('Вычитание')
elif operation == '/':
   print('Деление')
elif operation == '*':
   print('Умножение')
else:
   print('Неизвестная операция') 


def calculate(a, b, operation):
   result = None 

   if operation == '+':
       result = sum(a, b)
   elif operation == '-':
       result = subtract(a, b)
   elif operation == '/':
       result = divide(a, b)
   elif operation == '*':
       result = multiply(a, b)
   else:
       print('Неизвестная операция')  
    
   return result

def run_calculator():
   # Запрашиваем данные
   a = int(input('Введите первое число: '))
   b = int(input('Введите второе число: '))

   # Запрашиваем тип операции
   operation = ask_operation()
  
   # Производим вычисления
   result = calculate(a, b, operation)
 
   # Выводим результат в консоль
   print(f'Результат вычислений: {result}')

def calculate(a, b, operation):
   result = None
 
   if operation == '+':
       result = sum(a, b)
 
   elif operation == '-':
       result = subtract(a, b)
  
   elif operation == '/':
       result = divide(a, b)
 
   elif operation == '*':
       result = multiply(a, b)
 
​   # Возведение в степень
   elif operation == '^' or operation == '**':
       result = pow(a, b)
 
   else:
       print('Неизвестная операция')
 
   return result
