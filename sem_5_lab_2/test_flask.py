import requests
import json
from flask import Flask, render_template, request, url_for, redirect

from app import app

flask_app = app
def test_func():
    pass


def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello World1'