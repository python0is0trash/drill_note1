from openpyxl.styles import (
    Border,
    Side
)
from cfg import platoons, worksheet_1


def borders_func():
    ## рисование границ таблицы
    for i in range(5, 3 * len(platoons) + 14):
        for j in range(0, 10):
            worksheet_1[f'{chr(65 + j)}{i + 1}'].border = Border(left=Side(border_style='thin', color='000000'),
                                                                 top=Side(border_style='thin', color='000000'),
                                                                 bottom=Side(border_style='thin', color='000000'),
                                                                 right=Side(border_style='thin', color='000000')
                                                                 )
    worksheet_1['A1'].border = Border(top=Side(border_style='thin', color='000000'),
                                      left=Side(border_style='thin', color='000000'))
    worksheet_1['J1'].border = Border(top=Side(border_style='thin', color='000000'),
                                      right=Side(border_style='thin', color='000000'))
    worksheet_1['A4'].border = Border(left=Side(border_style='thin', color='000000'))
    worksheet_1['J4'].border = Border(right=Side(border_style='thin', color='000000'))
    for i in range(1, 9):
        worksheet_1[f'{chr(65 + i)}1'].border = Border(top=Side(border_style='thin', color='000000'))
        worksheet_1[f'{chr(65 + i)}5'].border = Border(top=Side(border_style='medium', color='000000'),
                                                       bottom=Side(border_style='medium', color='000000'))
        worksheet_1[f'{chr(65 + i)}{8 + len(platoons)}'].border = Border(top=Side(border_style='medium', color='000000'),
                                                                         bottom=Side(border_style='medium', color='000000'))
        worksheet_1[f'{chr(65 + i)}{11 + 2 * len(platoons)}'].border = Border(top=Side(border_style='medium', color='000000'),
                                                                              bottom=Side(border_style='medium', color='000000'))

    worksheet_1[f'A{5}'].border = Border(
        top=Side(border_style='medium', color='000000'),
        bottom=Side(border_style='medium', color='000000'),
        left=Side(border_style='thin', color='000000'))
    worksheet_1[f'J{5}'].border = Border(
        top=Side(border_style='medium', color='000000'),
        bottom=Side(border_style='medium', color='000000'),
        right=Side(border_style='thin', color='000000'))

    worksheet_1[f'A{8 + len(platoons)}'].border = Border(
        top=Side(border_style='medium', color='000000'),
        bottom=Side(border_style='medium', color='000000'),
        left=Side(border_style='thin', color='000000'))
    worksheet_1[f'J{8 + len(platoons)}'].border = Border(
        top=Side(border_style='medium', color='000000'),
        bottom=Side(border_style='medium', color='000000'),
        right=Side(border_style='thin', color='000000'))

    worksheet_1[f'A{11 + 2 * len(platoons)}'].border = Border(
        top=Side(border_style='medium', color='000000'),
        bottom=Side(border_style='medium', color='000000'),
        left=Side(border_style='thin', color='000000'))
    worksheet_1[f'J{11 + 2 * len(platoons)}'].border = Border(
        top=Side(border_style='medium', color='000000'),
        bottom=Side(border_style='medium', color='000000'),
        right=Side(border_style='thin', color='000000'))

    for outside_border in range(2):
        worksheet_1[f'A{outside_border + 2}'].border = Border(left=Side(border_style='thin', color='000000'))
        worksheet_1[f'J{outside_border + 2}'].border = Border(right=Side(border_style='thin', color='000000'))
