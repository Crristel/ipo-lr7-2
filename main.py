import json
num=int(input("Введите нужную вам квалификацию:"))
find = False
with open("dump.json", 'r', encoding='utf-8') as file: 
    read_file = json.load(file)
for i in read_file:
     if i.get("model") == "data.skill":
       if i["fields"].get("specialty") == num: 
           skill_code = i["fields"].get("code")
           skill_title = i["fields"].get("title")
           find=True

for i in read_file:
    if i.get("model")=="data.specialty":
        specialty_code = i["fields"].get("code")
        if specialty_code in skill_code:  
             specialty_title = i["fields"].get("title")
             specialty_educational = i["fields"].get("c_type")


if not find:
    print("==========Не найдено============")
else:
    print("===================Найдено==============")
    print(f"{specialty_code} >> Специальность '{specialty_title}' , {specialty_educational}")
    print(f"{skill_code} >> Квалификация '{skill_title}'")
