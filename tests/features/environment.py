from app import create_app
import requests

def before_all(context):
    context.app = create_app()
    context.app.testing = True
    context.client = context.app.test_client()
    context.base_url = 'http://localhost:5000'

def after_all(context):
    pass