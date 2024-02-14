from cfg import platoons, info_list, main_style, worksheet_1


def merge_func():
    ## объединение ячеек
    for i in range(1, 5):
        worksheet_1.merge_cells(f'A{i}:J{i}')
    worksheet_1.merge_cells('A5:J5')

    # больные
    worksheet_1.merge_cells('B6:H6')
    platoon_number = platoons[0][-2]
    course_start = 7
    faculty_start = course_start
    for i in range(faculty_start, len(platoons) + faculty_start):
        worksheet_1.merge_cells(f'B{i}:H{i}')
        worksheet_1[f'A{i}'].style = main_style
        worksheet_1[f'B{i}'].style = main_style
        worksheet_1[f'I{i}'].style = main_style
        worksheet_1[f'J{i}'].style = main_style
        current_platoon_number = platoons[i - faculty_start][-2]
        if current_platoon_number != platoon_number:
            worksheet_1.merge_cells(f'J{course_start}:J{i - 1}')
            platoon_number = current_platoon_number
            course_start = i
    worksheet_1.merge_cells(f'J{course_start}:J{6 + len(platoons)}')
    course_start = len(platoons) + 7
    worksheet_1[f'A{course_start}'].style = main_style
    worksheet_1[f'I{course_start}'].style = main_style
    worksheet_1.merge_cells(f'A{course_start}:H{course_start}')
    worksheet_1.merge_cells(f'I{course_start}:J{course_start}')
    course_start += 1

    # наряд
    worksheet_1.merge_cells(f'A{course_start}:J{course_start}')
    worksheet_1.merge_cells(f'B{course_start + 1}:H{course_start + 1}')
    platoon_number = platoons[0][-2]
    course_start += 2
    faculty_start = course_start
    for i in range(faculty_start, faculty_start + len(platoons)):
        worksheet_1.merge_cells(f'B{i}:H{i}')
        worksheet_1[f'A{i}'].style = main_style
        worksheet_1[f'B{i}'].style = main_style
        worksheet_1[f'I{i}'].style = main_style
        worksheet_1[f'J{i}'].style = main_style
        current_platoon_number = platoons[i - faculty_start][-2]
        if current_platoon_number != platoon_number:
            worksheet_1.merge_cells(f'J{course_start}:J{i - 1}')
            platoon_number = current_platoon_number
            course_start = i
    worksheet_1.merge_cells(f'J{course_start}:J{9 + 2 * len(platoons)}')
    course_start = 10 + 2 * len(platoons)
    worksheet_1[f'A{course_start}'].style = main_style
    worksheet_1[f'I{course_start}'].style = main_style
    worksheet_1.merge_cells(f'A{course_start}:H{course_start}')
    worksheet_1.merge_cells(f'I{course_start}:J{course_start}')
    course_start += 1

    # другие причины
    worksheet_1.merge_cells(f'A{course_start}:J{course_start}')
    worksheet_1.merge_cells(f'B{course_start + 1}:H{course_start + 1}')
    platoon_number = platoons[0][-2]
    course_start += 2
    faculty_start = course_start
    for i in range(faculty_start, faculty_start + len(platoons)):
        worksheet_1.merge_cells(f'B{i}:H{i}')
        worksheet_1[f'A{i}'].style = main_style
        worksheet_1[f'B{i}'].style = main_style
        worksheet_1[f'I{i}'].style = main_style
        worksheet_1[f'J{i}'].style = main_style
        current_platoon_number = platoons[i - faculty_start][-2]
        if current_platoon_number != platoon_number:
            worksheet_1.merge_cells(f'J{course_start}:J{i - 1}')
            platoon_number = current_platoon_number
            course_start = i
    worksheet_1.merge_cells(f'J{course_start}:J{12 + 3 * len(platoons)}')
    course_start = 13 + 3 * len(platoons)
    for i in range(2):
        worksheet_1[f'A{course_start + i}'].style = main_style
        worksheet_1[f'I{course_start + i}'].style = main_style
        worksheet_1.merge_cells(f'A{course_start + i}:H{course_start + i}')
        worksheet_1.merge_cells(f'I{course_start + i}:J{course_start + i}')
