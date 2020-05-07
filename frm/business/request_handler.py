from frm.business import add_friend
from flask import Flask


app = Flask()


def get_daily_alerts():
    pass


def create_friend(name, frequency):
    add_friend(name, frequency)


@app.route('/')
def create_alert():
    pass
