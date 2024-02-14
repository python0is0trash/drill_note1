from cfg import help_list, platoons, worksheet_1, Font

head_font = Font(
    name='Times New Roman',
    size=28,
    bold=True,
    italic=False,
    underline='none',
    strike=False,
    color='00000000'
)


def table_head_func():
    ## заполнение таблицы данными
    for i in range(3):
        current_string = 5 + i * len(platoons) + 3 * i
        worksheet_1[f'A{current_string}'].value = ''
        worksheet_1[f'A{current_string + 1}'].value = help_list[4]
        worksheet_1[f'A{current_string + 1}'].font = head_font
        worksheet_1[f'B{current_string + 1}'].value = help_list[7 + i]
        worksheet_1[f'B{current_string + 1}'].font = head_font
        worksheet_1[f'I{current_string + 1}'].value = help_list[5]
        worksheet_1[f'I{current_string + 1}'].font = head_font
        worksheet_1[f'J{current_string + 1}'].value = help_list[6]
        worksheet_1[f'J{current_string + 1}'].font = head_font

    for i in range(4):
        head_cell = worksheet_1[f'A{i + 1}']
        head_cell.font = Font(
            name='Times New Roman',
            size=36,
            bold=False,
            italic=False,
            underline='none',
            strike=False,
            color='00000000'
        )
        head_cell.value = str(help_list[i])

