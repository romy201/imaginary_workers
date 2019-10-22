import requests
import json

#    TESTING
#
# with open('app_related_data/the_workers_info.json', 'r') as json_f_d:
#     data_python = json.load(json_f_d)
#
# for x in range(len(data_python['paradigms'])):
#     r = requests.post('https://httpbin.org/post', data=data_python['paradigms'][x])
#     print(r.json()['form'])


def post_to(url_str):
    auth = ('bob', 'albert2002')
    with open('app_related_data/the_workers_info.json', 'r') as json_f_d:
        data_python = json.load(json_f_d)

    for data_piece in range(len(data_python[url_str])):
        r = requests.post('http://127.0.0.1:8000/{0}/'.format(url_str), data_python[url_str][data_piece], auth=auth)
        print(r.text)


# post_to('paradigms')


# post_to('jobs')

# post_to('workers')
