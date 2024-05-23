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

def get_users_ids(all_data):
    if all_data is None:
        return None
    try:
        users_ids = []
        for user in all_data["profiles"]:
            users_ids.append(user["id"])
        return users_ids
    except KeyError:
        print("Ошибка: отсутствует ключ 'profiles' в JSON данных")
        return None

def get_owner_text_pairs(all_data):
    if all_data is None:
        return None

    owner_text_dict = {}
    for item in all_data["items"]:
        owner_id = item.get("owner_id")
        text = item.get("text")
        if owner_id is not None and text is not None:
            owner_text_dict[text] = owner_id

    return owner_text_dict

def set_negative_values(groups_ids):
    if groups_ids is None:
        return None
    for i in range(len(groups_ids)):
        groups_ids[i] = -groups_ids[i]


file_name = "search_posts.json"
all_data = load_data_from_json(file_name)
owner_text_dict = get_owner_text_pairs(all_data)


first_key = next(iter(owner_text_dict))
first_value = owner_text_dict[first_key]


print(first_key, first_value)



# file_path = "search_posts.json"
# groups_ids = get_groups_ids(load_data_from_json(file_path))
# users_ids = get_users_ids(load_data_from_json(file_path))
#
# set_negative_values(groups_ids)
#
# print(users_ids)