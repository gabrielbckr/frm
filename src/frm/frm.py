from flask import Flask
from flask_cors import CORS

from src.frm.Business import RequestHandler, Scheduler

app = Flask(__name__)
CORS(app)

app = Flask(__name__)


@app.route("/daily", methods=["GET"])
def get_daily_alerts():
    RequestHandler.get_daily_alerts()
    pass


def run_frm():
    app.run()

def run_scheduler():
    Scheduler.schedule_tasks


if __name__ == "__main__":
    run_frm()
