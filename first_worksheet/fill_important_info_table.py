from cfg import platoons, info_list, worksheet_1


def fill_func():
    faculty_start = 7
    for i in range(faculty_start, faculty_start + len(platoons)):
        worksheet_1[f'A{i}'].value = platoons[i - faculty_start]
        worksheet_1[f'B{i}'].value = info_list[i % 3]

    # наряд
    faculty_start += 3 + len(platoons)
    for i in range(faculty_start, faculty_start + len(platoons)):
        worksheet_1[f'A{i}'].value = platoons[i - faculty_start]
        worksheet_1[f'B{i}'].value = info_list[i % 3]

    # другие причины
    faculty_start += 3 + len(platoons)
    for i in range(faculty_start, faculty_start + len(platoons)):
        worksheet_1[f'A{i}'].value = platoons[i - faculty_start]
        worksheet_1[f'B{i}'].value = info_list[i % 3]

    faculty_start += 3 + len(platoons)
    for i in range(2):
        pass