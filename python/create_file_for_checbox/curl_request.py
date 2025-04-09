import requests
import os
import base64
import datetime
import json
dirname = '/home/feodor/Desktop/programming/rzd/python/create_file_for_checbox/actions'
# giving file extension
ext = ('.xlsx')


def sent_message_to_express_chat():
    try:
        for file in os.listdir(dirname):
            if file.endswith(ext):
                # print(file)
                with open(f'{dirname}/{file}', "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                    data_obj = {
                        "file": encoded_string,
                        "namefile": file,
                    }
                    # convert into JSON:
                    # todo
                    url = 'http://localhost:3000/clear_files.php'
                    headers = {'content-type': 'application/json',
                               'Accept-Charset': 'UTF-8'}
                    requests.post(url, data=data_obj,
                                  headers=headers, verify=False)
    except Exception as e:
        print('Exception', e)
    else:
        print(f'Success sent! {datetime.datetime.today()}')
