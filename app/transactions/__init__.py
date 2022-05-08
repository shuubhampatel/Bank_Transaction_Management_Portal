import csv
import logging
import os

from flask import Blueprint, render_template, abort, url_for, current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename, redirect

from app.db import db
from app.db.models import Transaction
from app.transactions.forms import csv_upload

transactions = Blueprint('transactions', __name__,
                  template_folder='templates')


@transactions.route('/transactions', methods=['GET'], defaults={"page": 1})
@transactions.route('/transactions/<int:page>', methods=['GET'])
def transactions_browse(page):
    page = page
    per_page = 1000
    pagination = Transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    ball = 0
    if current_user.balance is None:
        ball = 0
    else:
        ball = current_user.balance
    try:
        return render_template('browse_transactions.html', data=data, pagination=pagination, ball=ball)
    except TemplateNotFound:
        abort(404)


@transactions.route('/transactions/upload', methods=['POST', 'GET'])
@login_required
def transactions_upload():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("csvlog")

        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        # user = current_user
        if current_user.balance is None:
            bal = current_user.inital_balance
        else:
            bal = current_user.balance
        log.info(bal)
        list_of_transactions = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_transactions.append(Transaction(row['AMOUNT'], row['TYPE']))
                log.info(bal)
                bal = bal + int(row['AMOUNT'])

        current_user.transactions = list_of_transactions
        current_user.set_balance(bal)
        current_user.inital_balance = bal
        db.session.commit()
        return redirect(url_for('transactions.transactions_browse'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)
