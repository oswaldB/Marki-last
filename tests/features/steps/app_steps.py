from behave import given, when, then
from flask import Flask
from app import create_app

@given(u'je suis connecté en tant qu\'utilisateur')
def step_impl(context):
    context.app = create_app()
    context.client = context.app.test_client()
    context.response = context.client.post('/api/auth/login', json={
        'username': 'user1',
        'password': 'password'
    })

@when(u'je visite la page "{url}"')
def step_impl(context, url):
    context.response = context.client.get(url)

@then(u'je dois voir le tableau de bord avec les statistiques')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'stats' in data

@then(u'je dois voir les informations de mon profil')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'user' in data

@then(u'je dois voir les statistiques mises à jour en temps réel')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'stats' in data

@then(u'je dois voir mes informations mises à jour en temps réel')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'user' in data

@given(u'je ne suis pas connecté')
def step_impl(context):
    context.app = create_app()
    context.client = context.app.test_client()

@then(u'je dois être redirigé vers la page de login')
def step_impl(context):
    assert context.response.status_code == 302
    assert context.response.location == '/auth/login'

@then(u'je dois voir le message "{message}"')
def step_impl(context, message):
    data = context.response.get_json()
    assert data['status'] == 'error'
    assert data['message'] == message