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

@then(u'je dois voir la topbar avec les informations de l\'utilisateur connecté')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'topbar' in data

@then(u'je dois voir l\'espace de contenu avec le contenu principal de la page')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert 'content' in data

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

@when(u'je clique sur un lien de navigation dans la sidebar')
def step_impl(context):
    context.response = context.client.get('/dashboard')

@then(u'je dois être redirigé vers la page correspondante')
def step_impl(context):
    assert context.response.status_code == 200

@given(u'je visite une page utilisant le layout `app-layout.html` sur un écran mobile')
def step_impl(context):
    context.response = context.client.get('/dashboard', headers={'User-Agent': 'Mobile'})

@then(u'la sidebar doit être masquée par défaut')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['sidebar']['isOpen'] == False

@then(u'le bouton de toggle doit être visible')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['sidebar']['toggleVisible'] == True

@given(u'je visite une page utilisant le layout `app-layout.html` sur un écran large')
def step_impl(context):
    context.response = context.client.get('/dashboard', headers={'User-Agent': 'Desktop'})

@then(u'la sidebar doit être visible par défaut')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['sidebar']['isOpen'] == True

@then(u'le bouton de toggle doit être masqué')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.get_json()
    assert data['sidebar']['toggleVisible'] == False