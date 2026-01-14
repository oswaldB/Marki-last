from behave import given, when, then
from flask import url_for
from app.models import User
from app import db


@given('un utilisateur qui accède à la page superadmin (ST-008)')
def step_given_user_access_superadmin(context):
    context.response = context.client.get('/superadmin')


@given('la base de données est vide (ST-008)')
def step_given_empty_database(context):
    # Supprimer tous les utilisateurs pour simuler une base vide
    db.session.query(User).delete()
    db.session.commit()


@when('je saisis le mot de passe superadmin "{password}" (ST-008)')
def step_when_enter_superadmin_password(context, password):
    context.form_data = {
        'superadmin_password': password,
        'username': '',
        'password': '',
        'confirm_password': ''
    }


@when('je saisis le nom d\'utilisateur "{username}" (ST-008)')
def step_when_enter_username(context, username):
    context.form_data['username'] = username


@when('je saisis le mot de passe "{password}" (ST-008)')
def step_when_enter_password(context, password):
    context.form_data['password'] = password


@when('je confirme le mot de passe "{confirm_password}" (ST-008)')
def step_when_confirm_password(context, confirm_password):
    context.form_data['confirm_password'] = confirm_password


@when('je clique sur le bouton "Créer le Premier Administrateur" (ST-008)')
def step_when_click_create_admin(context):
    context.response = context.client.post('/superadmin', data=context.form_data, follow_redirects=True)


@then('je devrais voir le formulaire de création (ST-008)')
def step_then_see_creation_form(context):
    assert context.response.status_code == 200
    assert b'Créer le Premier Administrateur' in context.response.data


@then('un nouvel utilisateur devrait être créé avec le rôle "admin" (ST-008)')
def step_then_user_created_with_admin_role(context):
    user = User.query.filter_by(is_admin=True).first()
    assert user is not None
    assert user.is_admin is True


@then('je devrais être redirigé vers la page de login (ST-008)')
def step_then_redirected_to_login(context):
    assert context.response.status_code == 200
    assert b'Login' in context.response.data


@then('je devrais voir un message d\'erreur "{message}" (ST-008)')
def step_then_see_error_message(context, message):
    assert message.encode() in context.response.data