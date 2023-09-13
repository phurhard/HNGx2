#!/usr/bin/env python3
'''Testing of API endpoints usimg requests'''
import pprint
import requests

url = "https://apis-fi9i.onrender.com"
# url = "http://127.0.0.1:5000" # uncomment for localhost testing
def test_post():
    '''Test the post endpoint'''
    postUrl = url + "/api"
    data = {'name': input("Name:= ")}
    #post
    newUser = requests.post(postUrl, json=data)
    if newUser.status_code == 201:
        userInfo = newUser.json()
        userId = userInfo['id']
        print(f"new user created !!")
        return userInfo
    else:
        return newUser.json()

def test_get():
    '''Test the GET endpoint'''
    getUrl = url + '/api/' + input("Name:= ")
    user = requests.get(getUrl)
    if user.status_code == 200:
        userInfo = user.json()
        return userInfo
    else:
        return user.json()
def test_put():
    '''Test the put method'''
    updateUrl = url + '/api/' + input('Name: ')
    New_name = str(input("New name: "))
    data = {'name': New_name}
    update = requests.put(updateUrl, json=data)
    if update.status_code == 200:
        userInfo = update.json()
        print('Updated successfully')
        return userInfo
    else:
        return update.json()

def test_delete():
    '''Test the delete endpoint'''
    deleteUrl = url + '/api/' + input('Name: ')
    delete = requests.delete(deleteUrl)
    if delete.status_code == 204:
        print('User has been deleted')
    else:
        return delete.json()

# Checker
def all_users():
    ''' Get all'''
    Url = url + '/api'
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
