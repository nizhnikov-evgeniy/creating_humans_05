import random
from faker import Faker
import os


def read_file(filename):
    with open(filename, encoding='utf8') as file_:
        return file_.read()


def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf8') as file_:
        return file_.write(content)


def render_template(template_path, new_folder_path, context):
    content = read_file(template_path)


    for key, value in context.items():
        content = content.replace('{%s}' % key, str(value))

    write_to_file(new_folder_path, content)


def replace_letters(skill):
    replacements = {
        'а': 'а͠', 
        'б': 'б̋', 
        'в': 'в͒͠',
        'г': 'г͒͠', 
        'д': 'д̋', 
        'е': 'е͠',
        'ё': 'ё͒͠', 
        'ж': 'ж͒', 
        'з': 'з̋̋͠',
        'и': 'и', 
        'й': 'й͒͠', 
        'к': 'к̋̋',
        'л': 'л̋͠', 
        'м': 'м͒͠', 
        'н': 'н͒',
        'о': 'о̋', 
        'п': 'п̋͠', 
        'р': 'р̋͠',
        'с': 'с͒', 
        'т': 'т͒', 
        'у': 'у͒͠',
        'ф': 'ф̋̋͠', 
        'х': 'х͒͠', 
        'ц': 'ц̋',
        'ч': 'ч̋͠', 
        'ш': 'ш͒͠', 
        'щ': 'щ̋',
        'ъ': 'ъ̋͠', 
        'ы': 'ы̋͠', 
        'ь': 'ь̋',
        'э': 'э͒͠͠', 
        'ю': 'ю̋͠', 
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋', 
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋', 
        'Е': 'Е',
        'Ё': 'Ё͒͠', 
        'Ж': 'Ж͒', 
        'З': 'З̋̋͠',
        'И': 'И', 
        'Й': 'Й͒͠', 
        'К': 'К̋̋',
        'Л': 'Л̋͠', 
        'М': 'М͒͠', 
        'Н': 'Н͒',
        'О': 'О̋', 
        'П': 'П̋͠', 
        'Р': 'Р̋͠',
        'С': 'С͒', 
        'Т': 'Т͒', 
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠', 
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 
        'Ш': 'Ш͒͠', 
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 
        'Ы': 'Ы̋͠', 
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 
        'Ю': 'Ю̋͠', 
        'Я': 'Я̋',
        ' ': ' '
    }

    for letter, replacement in replacements.items():
        skill = skill.replace(letter, replacement)
    return skill


def main():
    os.makedirs('new_folder', exist_ok=True)
    fake = Faker("ru_RU")
    for n in range(10):
        skills = random.sample([
            "Стремительный прыжок", 
            "Электрический выстрел", 
            "Ледяной удар", 
            "Стремительный удар",
            "Кислотный взгляд", 
            "Тайный побег", 
            "Ледяной выстрел", 
            "Огненный заряд"
        ],3)

        for i in range(len(skills)):
            skills[i]=replace_letters(skills[i])

        context = {
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name_male(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18), 
            "skill_1": skills[0],
            "skill_2": skills[1],
            "skill_3": skills[2],
        }
        render_template(
            "charsheet.svg", f"new_folder/charsheet_{n+1}.svg", context
        ) 



if __name__ == '__main__':
    main()
