from behave import given, when, then
from app.blueprints.auth.services.database import get_user_by_username

@given('Je suis sur la page "{page}"')
def step_impl(context, page):
    if not hasattr(context, 'browser'):
        raise AttributeError("'Context' object has no attribute 'browser'")
    context.browser.visit(context.base_url + page)

@when('Je saisis l\'identifiant "{username}"')
def step_impl(context, username):
    context.browser.fill('username', username)

@when('Je saisis le mot de passe "{password}"')
def step_impl(context, password):
    context.browser.fill('password', password)

@when('Je clique sur le bouton "{button}"')
def step_impl(context, button):
    context.browser.find_by_value(button).click()

@then('Je vois le message "{message}"')
def step_impl(context, message):
    assert message in context.browser.html

@then('Je suis redirigé vers la page d\'accueil')
def step_impl(context):
    assert context.browser.url == context.base_url + "/"

@when('Je saisis l\'email "{email}"')
def step_impl(context, email):
    context.browser.fill('email', email)

@then('L\'utilisateur existe en base de données avec l\'email "{email}"')
def step_impl(context, email):
    user = get_user_by_username(email)
    assert user is not None

@then('Je suis redirigé vers la page de connexion')
def step_impl(context):
    assert context.browser.url == context.base_url + "/auth/login"