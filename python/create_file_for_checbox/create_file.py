#!/usr/bin/python3

import csv
import re
from collections import OrderedDict
from datetime import datetime
import json
from openpyxl import Workbook
from openpyxl import load_workbook
import db as database
#


def read_and_change_file(file_name):
    wb = load_workbook('example.xlsx')
    ws = wb.active
    ws['B11'] = 'Какое-то погодное явление...!'

    # Название дирекции | ФИО | Дата, время формирования
    min_row = 12
    for row in ws.iter_rows(min_row=min_row, min_col=2, max_col=4, max_row=min_row, values_only=True):
        ws[f'B{min_row}'] = 'Новое название дирекции'
        ws[f'C{min_row}'] = 'Новое ФИО отвественного руководителя'
        ws[f'D{min_row}'] = 'Новое дата, время формирования чек-листа'

    wb.save('example-modified.xlsx')


def connect_to_db():
    return database.DB(user="mptablo",
                       # пароль, который указали при установке PostgreSQL
                       password="tablo_rkbtyn",
                       host="localhost",
                       port="5432",
                       db_name="tablo"
                       )


try:
    db = connect_to_db()
    # получение всех служб
    services = db.query_with_a_dictionary(
        'select * from accounts.get_all_services', '').fetchall()
    # проходим по всем службам
    for service in services:
        sl_code = service['id']
        # получаем данные по всем мероприятиям для одной службы в формате dictionary
        data_for_a_single_service = query_result = db.query_with_a_dictionary(
            'select * from tablo_content.actual_storm_actions_for_excel where sl_code=%s',
            (sl_code,)).fetchall()
        if (len(data_for_a_single_service)):
            print('ehh')
            for full_service_data in data_for_a_single_service:
                print('here', full_service_data,
                      full_service_data['sl_full_name'], '\n')
        # query_result = db.query(
        #     'select * from tablo_content.actual_storm_actions_for_excel where sl_code=%s', (sl_code,))
        # data_for_a_single_service = query_result.fetchall()
        # if (len(data_for_a_single_service)):
        #     for full_service_data in data_for_a_single_service:
        #         print(full_service_data, type(full_service_data), '\n')

    # read_and_change_file()

except Exception as e:
    print('Exception', e)
