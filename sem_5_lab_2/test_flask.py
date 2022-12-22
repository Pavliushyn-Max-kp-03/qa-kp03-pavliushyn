import requests
import json
from flask import Flask, render_template, request, url_for, redirect

from app import app

flask_app = app
def test_func():
    pass


def test_index_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is lab2'

def test_binary_pages():
    with flask_app.test_client() as test_client:
        response = test_client.get('/binaryFile')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'This is binary files pages'
        response = test_client.get('/binaryFiles')
        assert response.status_code == 200

        response = test_client.get('/binaryFile_read/1')
        assert response.status_code == 302
        response = test_client.get('/binaryFile_delete/1')
        assert response.status_code == 200
        response = test_client.get('/binaryFile_move/1')
        assert response.status_code == 405
        response = test_client.get('/binaryFile_del')
        assert response.status_code == 201
        response = test_client.get('/binaryFile_create/binaryFiles')
        assert response.status_code == 405


        response = test_client.get('/binaryFile_read')
        assert response.status_code == 404
        response = test_client.get('/binaryFile_delete')
        assert response.status_code == 404
        response = test_client.get('/binaryFile_move')
        assert response.status_code == 404
def test_buffer_pages():
    with flask_app.test_client() as test_client:
        response = test_client.get('/bufFile')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'This is buf files pages'
        response = test_client.get('/bufFiles')
        assert response.status_code == 200

        response = test_client.get('/bufFile_read/1')
        assert response.status_code == 200
        response = test_client.get('/bufFile_delete/1')
        assert response.status_code == 302
        response = test_client.get('/bufFile_move/1')
        assert response.status_code == 405
        response = test_client.get('/bufFile_push/2')
        assert response.status_code == 405
        response = test_client.get('/bufFile_create/bufFiles')
        assert response.status_code == 405

        response = test_client.get('/bufferFile_read')
        assert response.status_code == 404
        response = test_client.get('/bufferFile_move')
        assert response.status_code == 404
        response = test_client.get('/bufferFile_push')
        assert response.status_code == 404
        response = test_client.get('/bufferFile_consume')
        assert response.status_code == 404
def test_logtextfile_pages():
    with flask_app.test_client() as test_client:
        response = test_client.get('/logFile')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'This is log files pages'
        response = test_client.get('/logFiles')
        assert response.text == '{"logFiles":[{"father":null,"fileName":"logFile1","id":1,"info":"info1"},{"father":"directory1","id":2,"info":"info2","title":"logFile2"}]}\n'
        assert response.status_code == 200
        response = test_client.get('/logFile_create')
        assert response.status_code == 404
        response = test_client.get('/logFile_delete')
        assert response.status_code == 404
        response = test_client.get('/logtextFile_read')
        assert response.status_code == 404

        response = test_client.get('/logFile_read/1')
        assert response.status_code == 200
        response = test_client.get('/logFile_move/1')
        assert response.status_code == 405
        response = test_client.get('/logFile_append/2')
        assert response.status_code == 405
        response = test_client.get('/logFile_create/logFiles')
        assert response.status_code == 405

def test_directory_pages():
    with flask_app.test_client() as test_client:
        response = test_client.get('/directory')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'This is directory pages'
        response = test_client.get('/directories')
        assert response.status_code == 200

        response = test_client.get('/dir_read/1')
        assert response.status_code == 200
        response = test_client.get('/dir_del')
        assert response.status_code == 200
        response = test_client.get('/dir_move/1')
        assert response.status_code == 405

        response = test_client.get('/directory_read')
        assert response.status_code == 404
        response = test_client.get('/directory_list')
        assert response.status_code == 404
        response = test_client.get('/directory_move')
        assert response.status_code == 404