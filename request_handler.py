from first_worksheet.merge_table_cells import merge_func
from first_worksheet.width_height_of_cells import width_height_func
from first_worksheet.borders import borders_func
from first_worksheet.alignment_cells import alignment_func
from first_worksheet.table_head import table_head_func
from first_worksheet.fill_important_info_table import fill_func
from cfg import help_list, workbook, worksheet_1, worksheet_2

merge_func()
borders_func()
alignment_func()
table_head_func()
fill_func()
width_height_func()
workbook.save("test.xlsx")
