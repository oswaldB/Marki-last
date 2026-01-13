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

@then(u'je dois voir la sidebar avec les liens de navigation')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'sidebar' in data

@given(u'je visite une page utilisant le layout `app-layout.html` sur un écran mobile')
def step_impl(context):
    context.response = context.client.get('/dashboard', headers={'User-Agent': 'Mobile'})

@then(u'la sidebar doit être masquée par défaut')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['sidebar']['isOpen'] == False

@then(u'je dois voir le bouton de toggle de la sidebar')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['sidebar']['toggleVisible'] == True

@when(u'je clique sur le bouton de toggle de la sidebar')
def step_impl(context):
    context.response = context.client.post('/api/toggle_sidebar')

@then(u'la sidebar doit s\'ouvrir')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['sidebar']['isOpen'] == True

@then(u'la sidebar doit se fermer')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['sidebar']['isOpen'] == False

@then(u'je dois voir la liste des liens de navigation dans la sidebar')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'links' in data['sidebar']

@then(u'les liens doivent être affichés sous forme de liste verticale')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert isinstance(data['sidebar']['links'], list)

@when(u'je clique sur un lien de navigation dans la sidebar')
def step_impl(context):
    context.response = context.client.get('/dashboard')

@then(u'je dois être redirigé vers la page correspondante')
def step_impl(context):
    assert context.response.status_code == 200

@then(u'je dois voir le footer de la sidebar')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'footer' in data['sidebar']

@then(u'le footer doit contenir la version de l\'application')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'version' in data['sidebar']['footer']