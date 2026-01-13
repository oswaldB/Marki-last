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

@when(u'je visite une page utilisant le layout `app-layout.html`')
def step_impl(context):
    context.response = context.client.get('/dashboard')

@then(u'je dois voir la topbar avec les informations de l\'utilisateur connecté')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'topbar' in data

@then(u'je dois voir mon nom d\'utilisateur dans la topbar')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'username' in data['topbar']

@then(u'je dois voir mon avatar dans la topbar')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'avatar' in data['topbar']

@when(u'je clique sur mon avatar dans la topbar')
def step_impl(context):
    context.response = context.client.post('/api/toggle_user_menu')

@then(u'le menu déroulant doit s\'ouvrir')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['userMenu']['isOpen'] == True

@then(u'je dois voir les options "Profil" et "Déconnexion"')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'Profil' in data['userMenu']['options']
    assert 'Déconnexion' in data['userMenu']['options']

@when(u'je clique en dehors du menu déroulant')
def step_impl(context):
    context.response = context.client.post('/api/close_user_menu')

@then(u'le menu déroulant doit se fermer')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['userMenu']['isOpen'] == False

@then(u'je dois voir le badge de notifications dans la topbar')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'notifications' in data['topbar']

@then(u'je dois voir le nombre de notifications non lues')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'unreadCount' in data['topbar']['notifications']

@when(u'je clique sur le badge de notifications')
def step_impl(context):
    context.response = context.client.post('/api/toggle_notifications')

@then(u'la liste des notifications doit s\'afficher')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['notifications']['isOpen'] == True

@when(u'je clique sur une notification')
def step_impl(context):
    context.response = context.client.post('/api/mark_notification_as_read', json={
        'notificationId': 1
    })

@then(u'la notification doit être marquée comme lue')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['status'] == 'success'

@then(u'le badge de notifications doit être mis à jour')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'unreadCount' in data['topbar']['notifications']