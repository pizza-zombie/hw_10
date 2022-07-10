import json


def load_candidate(f):
    """Загружает кандидатов из файла в список"""
    raw_json = f.read()
    candidates = json.loads(raw_json)
    return candidates


def get_all(candidates):
    """Покажет нам всех кандидатов"""
    candidate_list = ''
    for candidate in candidates:
        candidate_list += f"{candidate['name']}\n"
        candidate_list += f"{candidate['position']}\n"
        candidate_list += f"{candidate['skills']}\n\n\n"
    return candidate_list

def get_by_pk(pk):
    """Вернет нам кандидата по pk"""
    candidate_pk = ''
    for candidate in candidates:
        if candidate['pk'] == pk:
            candidate_pk += f"{candidate['name']}\n"
            candidate_pk += f"{candidate['position']}\n"
            candidate_pk += f"{candidate['skills']}\n"
    return candidate_pk

def get_by_skill(skill_name):
    candidate_list = ''
    for candidate in candidates:
        if skill_name in candidate['skills']:
            candidate_list += f"{candidate['name']}\n"
            candidate_list += f"{candidate['position']}\n"
            candidate_list += f"{candidate['skills']}\n\n\n"
    return candidate_list

with open('candidates.json', 'r', encoding='utf-8') as f:
    candidates = load_candidate(f)

#print(get_all(candidates))
#print(f'<pre>\n{get_by_pk(int(input("Введите pk: ")))}\n</pre>')
#get_by_skill(input("Введите навык: "))