def find_common_participants(list1, list2, delimiter=','):
    group1 = set(list1.split(delimiter))
    group2 = set(list2.split(delimiter))

    common_participants = sorted(group1 & group2)

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(f"Общие участники: {common_participants}")