from behave import *
import requests


# Tutorial steps
@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

# Example steps
@given('the api url')
def step_impl(context):
    context.url = 'http://localhost:8000/api/hello'

@when('we make a request to the api')
def step_impl(context):
    context.response = requests.get(context.url)

@then('json response is retrieved with status code {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code), f'Status code is not {status_code}'

 

