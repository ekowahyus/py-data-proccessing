import pandas as pd
import os
import json

def diff_element(list1, list2):
    return list(set(list1) - set(list2))

FILE_PATH_DATA = 'data/field_data.xlsx'
FILE_PATH_RESULT = 'result'
SHEET_NAME = 'Transaction Code'
trx_codes_column_name = 'Transaction Code'

excel_file = pd.read_excel(FILE_PATH_DATA, sheet_name = SHEET_NAME)
transaction_codes = excel_file[trx_codes_column_name]

raw_db_path = open('data/data_db.json')
data_db = json.load(raw_db_path)

trx_code_list_excel = []
trx_code_list_db = []

for trx_code_excel in transaction_codes:
    trx_code_list_excel.append(trx_code_excel)

for trx_code_db in data_db:
    trx_code_list_db.append(trx_code_db['code'])

different_data = diff_element(trx_code_list_excel, trx_code_list_db)

dictionaries = {'Transaction Code': different_data}
data_frame = pd.DataFrame(dictionaries)
data_frame.to_csv('result/different_data-qa.csv', index=False)