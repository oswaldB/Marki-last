#!/usr/bin/env python
"""Direct test script for Hello World feature."""

import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from flask import Flask
from app import create_app

def test_hello_world_page():
    """Test the Hello World page directly."""
    app = create_app()
    client = app.test_client()
    
    # Test the hello route
    response = client.get('/hello')
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Test the content
    assert b'Hello, World!' in response.data, "Expected 'Hello, World!' in response"
    assert b'<img src="/public/logo.png"' in response.data, "Expected logo image in response"
    assert b'class="logo"' in response.data, "Expected logo class in response"
    assert b'class="message"' in response.data, "Expected message class in response"
    
    # Test the styles
    assert b'max-width: 200px' in response.data, "Expected max-width style in response"
    assert b'margin-bottom: 20px' in response.data, "Expected margin-bottom style in response"
    assert b'font-size: 24px' in response.data, "Expected font-size style in response"
    assert b'text-align: center' in response.data, "Expected text-align style in response"
    
    # Test the title
    assert b'<title>Hello World - Marki</title>' in response.data, "Expected title in response"
    
    # Test the font family
    assert b'font-family: \'Inter\', sans-serif' in response.data, "Expected font-family in response"
    
    # Test the body styles
    assert b'margin-top: 50px' in response.data, "Expected margin-top style in response"
    assert b'color: #333333' in response.data, "Expected color style in response"
    
    print("All tests passed!")

if __name__ == '__main__':
    test_hello_world_page()