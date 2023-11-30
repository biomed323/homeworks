# def read_domains(filename):
#     try:
#         with open(filename, 'r') as file:
#
#             domain_lines = file.readlines()
#
#
#             domains = [line.strip() for line in domain_lines]
#
#
#             domains = [domain.replace('.', '') for domain in domains]
#
#             return domains
#     except FileNotFoundError:
#         print(f"Файл {filename} не знайдено.")
#         return None



# def get_last_names(filename):
#     try:
#         with open(filename, 'r') as file:
#
#             lines = file.readlines()
#
#
#             last_names = [line.split('\t')[1].strip() for line in lines]
#
#             return last_names
#     except FileNotFoundError:
#         print(f"Файл {filename} не знайдено.")
#         return None
#
#
# filename = 'names.txt'
# result = get_last_names(filename)
#
# if result:
#     print(f"Прізвища: {result}")
#
#
#
#
# filename = 'domains.txt'
# result = read_domains(filename)
#
# if result:
#     print(f"Імена доменів без крапок: {result}")



import re

def extract_dates(filename):
    try:
        with open(filename, 'r') as file:
           
            lines = file.readlines()


            result_list = []


            for line in lines:

                date_match = re.search(r'\b\d{1,2}(st|nd|rd|th) [a-zA-Z]+ \d{4}\b', line)


                if date_match:
                    date = date_match.group(0)
                    result_list.append({"date": date})

            return result_list
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None

filename = 'authors.txt'
result = extract_dates(filename)

if result:
    print(f"Результат: {result}")
