import json
def load_data_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            all_data = json.load(file)
            return all_data
    except FileNotFoundError:
        print("файл не найден")
        return None
    except json.JSONDecodeError as error:
        print(f"ошибка декодирования файла: {error}")
        return None

def get_groups_ids(all_data):
    if all_data is None:
        return None
    try:
        groups_ids = []
        for group in all_data["groups"]:
            groups_ids.append(group["id"])
        return groups_ids
    except KeyError:
        print("Ошибка: отсутствует ключ 'groups' в JSON данных")
        return None

def set_negative_values(groups_ids):
    if groups_ids is None:
        return None
    for i in range(len(groups_ids)):
        groups_ids[i] = -groups_ids[i]




file_path = "search_posts.json"
groups_ids = get_groups_ids(load_data_from_json(file_path))
set_negative_values(groups_ids)

print(groups_ids)