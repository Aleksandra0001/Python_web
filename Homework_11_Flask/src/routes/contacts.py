from flask import Flask, render_template
from src import app


@app.route('/todo')
def contacts():
    return 'This is the contacts page'


@app.route('/todo/create')
def create():
    return 'Create a new todo'
