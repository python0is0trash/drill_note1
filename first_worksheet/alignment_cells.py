from cfg import platoons, workbook_alignment_center, workbook_alignment_left, worksheet_1


def alignment_func():
    # выравнивание
    for current_string in range(1, 15 + 3 * len(platoons)):
        for current_column in [0, 8, 9]:
            worksheet_1[f'{chr(65 + current_column)}{current_string}'].alignment = workbook_alignment_center

    for current_string in range(7, 15 + 3 * len(platoons)):
        worksheet_1[f'B{current_string}'].alignment = workbook_alignment_left

    for current_string in [6, 9 + len(platoons), 12 + 2 * len(platoons)]:
        worksheet_1[f'B{current_string}'].alignment = workbook_alignment_center

