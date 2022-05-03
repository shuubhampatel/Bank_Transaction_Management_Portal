"""These are reusable template function"""
from os import getenv
import datetime


def utility_text_processors():
    message = "IS601 Bank Transaction Management Portal"

    def deployment_environment():
        return getenv('FLASK_ENV', None)

    def current_year():
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        return year

    return dict(
        mymessage=message,
        deployment_environment=deployment_environment(),
        year=current_year(),
    )
