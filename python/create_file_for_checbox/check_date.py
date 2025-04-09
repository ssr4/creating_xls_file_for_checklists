
import db as database
from datetime import datetime
FORMAT_DATE = '%Y-%m-%d %H:%M:%S'


def connect_to_db():
    return database.DB(user="mptablo",
                       # пароль, который указали при установке PostgreSQL
                       password="tablo_rkbtyn",
                       host="localhost",
                       port="5432",
                       db_name="tablo"
                       )


def get_file_metadata_from_db(db, filename):
    metadata = db.query_with_a_dictionary(
        f"select filename, upload_time from files_uploading.select_file_metadata('{filename}')", '').fetchall()
    return metadata


def get_difference_between_two_dates_in_hours(date1, date2):
    d1 = date1.strftime(FORMAT_DATE)
    d2 = date2.strftime(FORMAT_DATE)
    dt1 = datetime.strptime(d1, FORMAT_DATE)
    dt2 = datetime.strptime(d2, FORMAT_DATE)
    subtract = abs(dt2 - dt1)
    days = subtract.days
    seconds = subtract.seconds
    hours = days*24 + seconds / 3600
    return hours


def check_date(db, file):
    try:
        isOk = False
        # print(file,  os.path.getctime(f'{dir}/{file}'), '\n')
        # получение всех служб
        metadata = get_file_metadata_from_db(db, file)
        if (len(metadata)):
            upload_time = metadata[0]['upload_time']
            # get difference between today and upload_time
            hours = get_difference_between_two_dates_in_hours(
                datetime.today(), upload_time)
            minimum_available_hours = 3
            if (hours >= minimum_available_hours):
                isOk = True
    except Exception as e:
        print(e)
    finally:
        return isOk
