#!/usr/bin/env python3
'''Testing of API endpoints usimg requests'''
import pprint
import requests

url = "https://apis-fi9i.onrender.com"
# url = "http://127.0.0.1:5000" # uncomment for localhost testing
def test_post():
    '''Test the post endpoint'''
    postUrl = f"{url}/api"
    data = {'name': input("Name:= ")}
    #post
    newUser = requests.post(postUrl, json=data)
    if newUser.status_code != 201:
        return newUser.json()
    userInfo = newUser.json()
    userId = userInfo['id']
    print("new user created !!")
    return userInfo

def test_get():
    '''Test the GET endpoint'''
    getUrl = f'{url}/api/' + input("Name:= ")
    user = requests.get(getUrl)
    return user.json()
def test_put():
    '''Test the put method'''
    updateUrl = f'{url}/api/' + input('Name: ')
    New_name = str(input("New name: "))
    data = {'name': New_name}
    update = requests.put(updateUrl, json=data)
    if update.status_code != 200:
        return update.json()
    userInfo = update.json()
    print('Updated successfully')
    return userInfo

def test_delete():
    '''Test the delete endpoint'''
    deleteUrl = f'{url}/api/' + input('Name: ')
    delete = requests.delete(deleteUrl)
    if delete.status_code == 204:
        print('User has been deleted')
    else:
        return delete.json()

# Checker
def all_users():
    ''' Get all'''
    Url = f'{url}/api'
    check = requests.get(Url)
    if check.status_code == 200:
        return check.json()
    else:
        return 'Oh NO, what is happenning'

#the loop
while True:
    options = ['check', 'post', 'get', 'delete', 'update', 'quit']
    print(f'Availabe options are {options}')
    user = input('Which operation do u want to perform:   ')
    user.lower()
    if user == 'check':
        print(all_users())
    if user == 'post':
        print(test_post())
    if user == 'get':
        print(test_get())
    if user == 'update':
        print(test_put())
    if user == 'delete':
        print(test_delete())
    if user == 'quit':
        break
    else:
        print('Unknown parameters, used allowed parameters')
