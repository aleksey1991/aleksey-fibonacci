#fibonacci backend test code by Aleksey Treskov
import pytest
import requests


address = "http://13.59.70.88:5000/api/fibonacci/{}"


def test_basic_numbers():
    """
    This test will test happy path results for the Fibonachi sequence. 0 to 4 numbers were picked because they are the
    special cases for fibonacci numbers.
    """
    fibonacci = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        10: 55,
        20: 6765,
        40: 102334155,
        100: 354224848179261915075
    }
    for input in fibonacci:
        command = requests.get(address.format(input))
        assert command.status_code == 200
        response = command.json()
        assert 'fibonacci' in response
        assert response['fibonacci'] == fibonacci[input]

def test_negative_numbers():
    #This test will focus on making sure that negative numbers give us an error
    negative_num = {
        -1,
        -5,
        -10,
        -20
    }
    for input in negative_num:
        command = requests.get(address.format(input))
        assert command.status_code == 404
        response = command.json()
        assert response['error'] == 'resource not found'

def test_string():
    """
    This test will focus on making sure that inputing a string instead of a number will give us an error
    It includes lower case and upper case letters
    """
    random_string = {
        'TEST',
        'test',
        'TESTTEST'
    }
    for input in random_string:
        command = requests.get(address.format(input))
        assert command.status_code == 404
        response = command.json()
        assert response['error'] == 'resource not found'

def test_alphanumeric():
    """
    This test will focus on checking input that is aplphanumeric to make sure we receive an error
    It will test an input starting with a number
    It will test an input ending with a number
    It will test a rendom letter + number input
    """

    alphanumeric = {
        '5TEST',
        'test5',
        'testing343435testing'
    }
    for input in alphanumeric:
        command = requests.get(address.format(input))
        assert command.status_code == 404
        response = command.json()
        assert response['error'] == 'resource not found'

def test_decimal():
    #Testing to make sure decimal numbers/ float numbers will return an error
    decimal_num = {
        5.5,
        5.0,
        0.5,
    }
    for input in decimal_num:
        command = requests.get(address.format(input))
        assert command.status_code == 404
        response = command.json()
        assert response['error'] == 'resource not found'

def test_noinput():
    """
    Test to make sure a blank input returns an error
    """
    command = requests.get(address.format(''))
    assert command.status_code == 404
    response = command.json()
    assert response['error'] == 'resource not found'

def test_othercharacters():
    #Test is written to make sure that other common characters are not allowed as an input
    characters = {
        '#',
        '@',
        '$',
        '%',
        '^',
        '&',
        '*'
        '(',
        ')',
        '-',
        '+',
        '=',
    }
    for input in characters:
        command = requests.get(address.format(input))
        assert command.status_code == 404
        response = command.json()
        assert response['error'] == 'resource not found'


def test_invalid_request():
    #Test invalid request with an actual real fibonacci number 1

    invalidrequest = {
        'POST': requests.post,
        'DELETE': requests.delete,
        'PUT': requests.put

    }
    for change in invalidrequest:
        command =invalidrequest[change](address.format(1))
        assert command.status_code == 405
        response = command.json()
        assert response['error'] == 'method not supported'

def test_invalid_request_noinput():
    #Test invalid request with no input


    invalidrequest = {
        'POST': requests.post,
        'DELETE': requests.delete,
        'PUT': requests.put

    }
    for change in invalidrequest:
        command =invalidrequest[change](address.format(''))
        assert command.status_code == 404
        response = command.json()
        assert response['error'] == 'resource not found'

    """
    This test is commented out becuase trying to get a result for a very large number crashed the backend 
    """

#def test_large_input():
#command = requests.get(address.format(9999999999))
#assert command.status_code == 200
#response = command.json()









