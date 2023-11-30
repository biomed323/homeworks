def calculator():
    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть операцію (+, -, *, /): ")
            num2 = float(input("Введіть друге число: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Помилка: Ділення на нуль неможливе.")
                    continue  # Повторити цикл
                else:
                    result = num1 / num2
            else:
                print("Помилка: Невідома операція.")
                continue  # Повторити цикл

            print("Результат:", result)

        except ValueError:
            print("Помилка: Будь ласка, введіть числа коректно.")
        except Exception as e:
            print(f"Помилка: {e}")

        repeat = input("Бажаєте повторити операцію? (так/ні): ")
        if repeat.lower() != 'так':
            break

if __name__ == "__main__":
    calculator()
