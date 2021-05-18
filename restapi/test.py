import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPONT = 'api/'

def get_resource(id):
    resp = requests.get(BASE_URL+ENDPONT+id+'/')
    print(resp.status_code)
    if resp.status_code == requests.codes.ok:
        print(resp.json())
    else:
        print('Something goes wrong.please check it')


id = input('Enter Employee id ')
get_resource(id)

def get_all():
    resp = requests.get(BASE_URL+ENDPONT)
    print(resp.status_code)
    print(resp.json())

get_all()

def create_resource():
    new_emp = {
        'eno':400,
        'ename':'Raja',
        'esal':50000,
        'eaddr':'Noida'
    }
    resp = requests.post(BASE_URL+ENDPONT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

create_resource()

def update_resource(id):
    emp_data = {
        'esal':750,
        'eaddr':'delhi',
    }
    resp = requests.put(BASE_URL+ENDPONT+str(id) + '/', data=json.dumps(emp_data))
    print(resp.status_code)
    print(resp.json())


id = input('Enter id and information')
update_resource(id)


def delete_resource(id):
    resp = requests.delete(BASE_URL + ENDPONT + str(id) + '/')
    print(resp.status_code)
    print(resp.json())

create_resource()
update_resource('4')
delete_resource('3')
get_all()