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


def get_all():
    resp = requests.get(BASE_URL+ENDPONT)
    print(resp.status_code)
    print(resp.json())


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


def update_resource(id):
    emp_data = {
        'esal':7500,
        'eaddr':'delhi',
    }
    resp = requests.put(BASE_URL+ENDPONT+str(id) + '/', data=json.dumps(emp_data))
    print(resp.status_code)
    print(resp.json())


def delete_resource(id):
    resp = requests.delete(BASE_URL + ENDPONT + str(id) + '/')
    print(resp.status_code)
    print(resp.json())


print('1. Get the Employee detail type 1\n2. Get all Employees detail type 2\n3. Update Employee type 3'
      '\n4. Delete Employee type 4 ')

choose = int(input('Please choose the action '))
if choose == 1:
    id = input('Please Enter the Employee Id ')
    get_resource(id)
elif choose ==2:
    get_all()
elif choose == 3:
    id = input('Enter Employee id ')
    update_resource(id)
elif choose == 4:
    id = input('Enter Employee id ')
    delete_resource(id)
else:
    print('You have choose invalid option ')
