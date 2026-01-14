from behave import given, when, then
from flask import Flask
from app import create_app

@given(u'je suis sur la page d\'accueil')
def step_impl(context):
    context.app = create_app()
    context.client = context.app.test_client()

@when(u'je visite la page "/hello"')
def step_impl(context):
    context.response = context.client.get('/hello')

@then(u'je devrais voir un élément "img" avec l\'attribut "src" égal à "/public/logo.png"')
def step_impl(context):
    assert context.response.status_code == 200
    assert b'<img src="/public/logo.png"' in context.response.data

@then(u'je devrais voir un texte "Hello, World!"')
def step_impl(context):
    assert context.response.status_code == 200
    assert b'Hello, World!' in context.response.data

@then(u'le logo devrait avoir une classe "logo"')
def step_impl(context):
    assert context.response.status_code == 200
    assert b'class="logo"' in context.response.data

@then(u'le message devrait avoir une classe "message"')
def step_impl(context):
    assert context.response.status_code == 200
    assert b'class="message"' in context.response.data

@then(u'l\'élément "img.logo" devrait avoir un style "max-width" égal à "200px"')
def step_impl(context):
    assert context.response.status_code == 200
    assert b'max-width: 200px' in context.response.data

@then(u'l\'élément "img.logo" devrait avoir un style "margin-bottom" égal à "20px"')
def step_impl(context):
    assert context.response.status_code == 200
    assert b'margin-bottom: 20px' in context.response.data

@then(u'l\'élément ".message" devrait avoir un style "font-size" égal à "24px"')
def step_impl(context):
    assert context.response.status_code == 200
    assert b'font-size: 24px' in context.response.data

@then(u'l\'élément "body" devrait avoir un style "text-align" égal à "center"')
def step_impl(context):
    assert context.response.status_code == 200
    assert b'text-align: center' in context.response.data
