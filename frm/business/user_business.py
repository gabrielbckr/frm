import datetime as dt
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from frm.domain import Friend, Alert
from frm.repository import FriendRepository, AlertRepository
from frm.util import constants as const


def add_friend(name, frequency=30):
    friend = Friend()
    friend.name = name
    friend.frequency = frequency
    repo = FriendRepository()
    repo.create(friend)


def update_friend_frequency(name, frequency):
    repo = FriendRepository()
    f: Friend = repo.get_by_name(name)
    f.frequency = frequency
    repo.commit()


def check_friends_for_alert():
    repo = FriendRepository()
    friends = repo.get_all()
    for f in friends:
        process_alert(f)


def process_alert(f: Friend):
    repo = AlertRepository()
    old_alert: Alert = repo.get_top_by_user_id(f.id)
    if old_alert:
        if not old_alert.is_solved:
            return
        new_trigger = \
            old_alert.trigger_time + dt.timedelta(days=f.frequency)
    else:
        new_trigger = dt.date.today() + dt.timedelta(days=f.frequency)
    alert = Alert()
    alert.user_id = f.id
    alert.trigger_time = new_trigger
    alert.is_solved = False
    repo.create(alert)


def send_mail_with_alerts():
    alerts = get_all_alerts()
    if not len(alerts):
        return
    addr = os.getenv(const.SEND_MAIL)
    pw = os.getenv(const.SEND_PASSWORD)
    recipient = os.getenv(const.USER_MAIL)
    print(f"{addr}:{pw} {recipient}")
    make_mail(alerts, addr, pw, recipient)


def get_all_alerts():
    a_repo = AlertRepository()
    f_repo = FriendRepository()
    alerts = a_repo.get_by_active()
    friends = []
    al: Alert
    for al in alerts:
        f = f_repo.get_by_id(al.user_id)
        friends.append(f"{f.name}: {al.trigger_time}")
    return friends


def make_mail(alert_list, sender_email, password, receiver_email):

    message = MIMEMultipart("alternative")
    message["Subject"] = "FRM - Friend Alert"
    message["From"] = sender_email
    message["To"] = receiver_email

    html_alert_string = "\n".join([f"<li>{x}</li>" for x in alert_list])

    html = f"""

    <html>
      <body>
        <p>
            Hi, FRM - Friend Relationship Management alerts
            It's time to get in touch with these people!
        <p>
        <ul>
            {html_alert_string}
        </ul>
      </body>
    </html>
    """

    mail_body = MIMEText(html, "html")

    message.attach(mail_body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
