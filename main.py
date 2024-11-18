import json  # Импортируем модуль json

kvalf = input("Введите номер квалификации: ")  # Запрашиваем у пользователя номер квалификации
find = False  # Инициализируем переменную find как False

with open("dump.json", 'r', encoding='utf-8') as file:  # Открываем файл dump.json для чтения
    read_file = json.load(file)  # Загружаем содержимое файла в переменную read_file
    for skill in read_file:  # Перебираем каждый элемент в read_file
        if skill.get("model") == "data.skill":  # Проверяем, является ли значение "model" = data.skill"
            if skill["fields"].get("code") == kvalf:  # Проверяем, совпадает ли код квалификации с введенным
                skill_code = skill["fields"].get("code")  # Получаем код квалификации
                skill_title = skill["fields"].get("title")  # Получаем название квалификации
                find = True  # Устанавливаем find в True, так как квалификация найдена

for specialty in read_file:  # Перебираем каждый элемент в read_file
    if specialty.get("model") == "data.specialty":  # Проверяем, является ли значение "model" = data.specialty"
        specialty_code = specialty["fields"].get("code")  # Получаем код специальности
        if specialty_code in skill_code:  # Проверяем, содержится ли код специальности в коде квалификации
            specialty_title = specialty["fields"].get("title")  # Получаем название специальности
            specialty_educational = specialty["fields"].get("c_type")  # Получаем тип образования 
            specialty_c = specialty["fields"].get("code")  # Получаем код специальности

if not find:  # Проверяем, была ли найдена квалификация
    print("=============== Не найдено ===============")  #вывод на консоль
else:  # Если квалификация найдена
    print("=============== Найдено ===============")  # Вывод на консоль
    print(f"{specialty_c} >> Специальность '{specialty_title}', {specialty_educational}")  #вывод на консоль 
    print(f"{kvalf} >> Квалификация '{skill_title}'")  #вывод на консоль 
