from behave import given, then

@given('Je suis sur la page hello "{page}"')
def step_impl(context, page):
    context.response = context.client.get(page)

@then('Je vois le titre "{text}"')
def step_impl(context, text):
    assert text in context.response.data.decode('utf-8')

@then('Je vois le sous-titre "{text}"')
def step_impl(context, text):
    assert text in context.response.data.decode('utf-8')

@then('Je vois le texte "{text}"')
def step_impl(context, text):
    assert text in context.response.data.decode('utf-8')

@then('Je vois un bouton "{text}"')
def step_impl(context, text):
    assert text in context.response.data.decode('utf-8')