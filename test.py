#!/usr/bin/env python3
'''Testing of API endpoints usimg requests'''
import pprint
import requests

url = "https://apis-fi9i.onrender.com"
def test_post():
    '''Test the post endpoint'''
    url = url + "/api"
    data = {'name': input("Name:= ")}
    #post
    newUser = requests.post(url, json=data)
    if newUser.status_code == 201:
        userInfo = newUser.json()
        userId = userInfo['id']
        print(f"new user created !!")
        return userInfo
    else:
        return newUser.json()

def test_get():
    '''Test the GET endpoint'''
    getUrl = url + '/api/' + input("UserId:= ")
    user = requests.get(getUrl)
    if user.status_code == 200:
        userInfo = user.json()
        return userInfo
    else:
        return user.json()
def test_put():
    '''Test the put method'''
    data = {'name': 'New name'}
    updateUrl = url + '/api/' + input('UserId: ')
    update = requests.put(updateUrl, json=data)
    if update.status_code == 200:
        userInfo = update.json()
        print('Updated successfully')
        return userInfo
    else:
        return update.json()

def test_delete():
    '''Test the delete endpoint'''
    deleteUrl = url + '/api/' + input('UserId: ')
    delete = requests.delete(deleteUrl)
    if delete.status_code == 204:
        print('User has been deleted')
        return delete
    else:
        return delete.json()

# Checker
def all_users():
    ''' Get all'''
    url = url + '/api'
    check = requests.get(url)
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
    if user == 'put':
        print(test_put())
    if user == 'delete':
        print(test_delete())
    if user == 'quit':
        break
    else:
        print('Unknown parameters, used allowed parameters')
