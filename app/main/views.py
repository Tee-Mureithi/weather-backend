from flask import Flask, subscribe
from flask_mail_sendgrid import MailSendGrid
from flask_mail import Message
from forms import SubscriberForm
from app import db


from app.requests import get_weather_update

app = Flask(__name__)
app.config['MAIL_SENDGRID_API_KEY'] = 'XXXXXXXX'
mail = MailSendGrid(app)

@app.route("/")
def index():
    message = Message("Hello",
        sender="from@example.com",
        recipients=["to@example.com"])


# @app.route('/', methods = ["GET","POST"])
# def subscriber():

#     weather = get_weather_update()

    # form = SubscriberForm()
    # if form.validate_on_submit():
    #     subscribe = Subscribe(email = form.email.data)

    #     db.session.add(subscribe)
    #     db.session.commit()

    #     mail_message("Welcome to the Weather App!","email/subscribe",subscribe.email,user=subscribe)

    #     flash("Subscribed successfully. You'll never run short on weather details!")

    #     return redirect (url_for('auth.login'))
    #     # return redirect(url_for('main.index'))

    # weather = Weather.query.all()

    # return render_template('index.html', form = form, quotes=quotes, blogs=blogs)

