from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_pages', __name__,
                         template_folder='templates')


@simple_pages.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/git')
def git():
    try:
        return render_template('git.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/docker')
def docker():
    try:
        return render_template('docker.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/flask')
def flask():
    try:
        return render_template('flask.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/cicd')
def cicd():
    try:
        return render_template('cicd.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/pylint')
def pylint():
    try:
        return render_template('pylint.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/aaa')
def aaa():
    try:
        return render_template('aaa.html')
    except TemplateNotFound:

        abort(404)


@simple_pages.route('/oops')
def oops():
    try:
        return render_template('oops.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/solid')
def solid():
    try:
        return render_template('solid.html')
    except TemplateNotFound:
        abort(404)
