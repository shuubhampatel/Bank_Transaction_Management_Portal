import logging

from app import db
from app.db.models import User, Transaction


def test_adding_user(application):
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        # showing how to add a record
        # create a record
        user = User('test@test.com', 'test1234')
        # add it to get ready to be committed
        db.session.add(user)
        # call the commit
        # db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        user = User.query.filter_by(email='test@test.com').first()
        # asserting that the user retrieved is correct
        assert user.email == 'test@test.com'
        # this is how you get a related record ready for insert
        user.transactions = [Transaction("1000", "CREDIT"), Transaction("500", "DEBIT")]
        # commit is what saves the songs
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        trans1 = Transaction.query.filter_by(amount='1000').first()
        assert trans1.amount == "1000"
        # changing the title of the song
        trans1.amount = "1000"
        # saving the new title of the song
        db.session.commit()
        trans2 = Transaction.query.filter_by(amount='500').first()
        assert trans2.amount == "500"
        # checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0