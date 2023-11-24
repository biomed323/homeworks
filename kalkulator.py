
q1 = int (input('Введіть число 1: '))
q2 = int (input('Введіть число 2: '))

v = int (input('1 Додавання \n 2 Віднімання \n 3 Ділення \n 4 Множення \n'))

if v == 1:
    r = q1 + q2
    p = 'Додавання'
    t = p
if v == 2:
    r = q1 - q2
    l = 'Віднімання'
    t = l
if v == 3:
    r = float(q1 / q2)
    m = 'Ділення'
    t = m
if v == 4:
    r = q1 * q2
    n = 'Множення'
    t = n
print ('Результат ',t,' = ',r)

answer = input('Бажаєте продовжити?\n'

      ' Введіть + якщо так і інщий символ, якщо ні: ')

if answer != '+':

        progam_is_running = False
