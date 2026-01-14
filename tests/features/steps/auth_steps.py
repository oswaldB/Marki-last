from behave import given, when, then
from flask import Flask
from app import create_app

@given(u'je suis sur la page "{url}"')
def step_impl(context, url):
    context.app = create_app()
    context.client = context.app.test_client()
    context.response = context.client.get(url)

@given(u'je suis sur la page "{url}" avec le layout `app-layout.html`')
def step_impl(context, url):
    context.app = create_app()
    context.client = context.app.test_client()
    context.response = context.client.get(url)

@when(u'je saisis l\'identifiant "{username}"')
def step_impl(context, username):
    context.username = username

@when(u'je saisis le mot de passe "{password}"')
def step_impl(context, password):
    context.password = password

@when(u'je clique sur "{button}"')
def step_impl(context, button):
    if button == "Se connecter":
        context.response = context.client.post('/api/auth/login', json={
            'username': context.username,
            'password': context.password
        })
    elif button == "Créer un compte":
        context.response = context.client.post('/api/auth/register', json={
            'username': context.username,
            'password': context.password
        })
    elif button == "Récupérer le mot de passe":
        context.response = context.client.post('/api/auth/forgot_password', json={
            'username': context.username
        })
    elif button == "Créer le premier administrateur":
        context.response = context.client.post('/api/superadmin', json={
            'password': context.password
        })
    elif button == "Ajouter un collaborateur":
        context.response = context.client.post('/api/settings/team/add_collaborator', json={
            'username': context.username,
            'password': context.password
        })
    elif button == "Valider":
        context.response = context.client.post('/api/settings/team/add_collaborator', json={
            'username': context.username,
            'password': context.password
        })

@then(u'je dois être redirigé vers la page "{url}"')
def step_impl(context, url):
    assert context.response.status_code == 302
    assert context.response.location == url

@then(u'je dois voir le drawer pour changer le mot de passe')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['drawer']['isOpen'] == True

@then(u'je dois être redirigé vers la page de création de compte')
def step_impl(context):
    assert context.response.status_code == 302
    assert context.response.location == '/auth/register'

@given(u'je suis connecté en tant qu\'administrateur')
def step_impl(context):
    context.app = create_app()
    context.client = context.app.test_client()
    context.response = context.client.post('/api/auth/login', json={
        'username': 'admin',
        'password': 'password'
    })

@given(u'je suis connecté en tant qu\'utilisateur non administrateur')
def step_impl(context):
    context.app = create_app()
    context.client = context.app.test_client()
    context.response = context.client.post('/api/auth/login', json={
        'username': 'user1',
        'password': 'password'
    })

@given(u'je suis connecté en tant qu\'administrateur avec le layout `app-layout.html`')
def step_impl(context):
    context.app = create_app()
    context.client = context.app.test_client()
    context.response = context.client.post('/api/auth/login', json={
        'username': 'admin',
        'password': 'password'
    })



@when(u'je saisis le nouveau mot de passe "{password}"')
def step_impl(context, password):
    context.newPassword = password

@given(u'le premier administrateur est déjà créé')
def step_impl(context):
    context.app = create_app()
    context.client = context.app.test_client()
    context.response = context.client.post('/api/superadmin', json={
        'password': 'Citron6-Mustang8'
    })
