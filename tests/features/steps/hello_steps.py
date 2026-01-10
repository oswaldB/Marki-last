from behave import given, when, then
from flask import Flask
from app import create_app

@given(u'je suis sur la page "{url}"')
def step_impl(context, url):
    context.app = create_app()
    context.client = context.app.test_client()
    context.response = context.client.get(url)

@when(u'je visite la page "{url}"')
def step_impl(context, url):
    context.response = context.client.get(url)

@then(u'je dois voir le message "{message}"')
def step_impl(context, message):
    assert message in context.response.data.decode('utf-8'), \
        f"Le message '{message}' n'a pas été trouvé dans la réponse."
