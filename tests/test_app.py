import sys
import os

# Insert the path where app.py is located
sys.path.insert(0, '/home/ubuntu')

import pytest
from app import app  # Now app will be imported from the correct path

@pytest.fixture
def client():
    app.config['TESTING'] = True  # Enable testing mode in Flask
    with app.test_client() as client:  # Use Flask's test client
        yield client

def test_home(client):
    """Test if the home route renders correctly."""
    response = client.get('/')  # Simulate a GET request to the home route
    assert response.status_code == 200  # Check if the status code is 200
    assert b"Welcome to Our Website" in response.data  # Check if the expected text is in the response
