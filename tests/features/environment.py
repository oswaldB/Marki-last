from app import create_app

def before_all(context):
    context.app = create_app()
    context.app.testing = True
    context.client = context.app.test_client()

def after_all(context):
    pass