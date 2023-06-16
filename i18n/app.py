#!/usr/bin/env python3
""" App """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime
import locale

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config Class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def is_valid_timezone(time):
    """ Return the timezone """
    try:
        return timezone(time)
    except UnknownTimeZoneError:
        return None


@babel.localeselector
def get_locale():
    """ return the accept languages """
    user = get_user()
    language = request.args.get('locale')
    if language and language in app.config['LANGUAGES']:
        return language
    elif user and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Return the timezone to use """
    user = get_user()
    time = request.args.get('timezone')
    if time:
        valid = is_valid_timezone(time)
        if valid:
            return valid
    if user:
        valid = is_valid_timezone(user.get('timezone'))
        if valid:
            return valid
    return timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


def get_user():
    """ Get the user_id """
    id = request.args.get('login_as')
    if id:
        id = int(id)
        return users.get(id)
    return None


@app.before_request
def before_request():
    """ Look if a user is logged """
    user = get_user()
    if user:
        g.user = user
    time = get_timezone()
    print(time)
    utc_dt = datetime.now()
    au_tz = time
    au_dt = utc_dt.astimezone(au_tz)
    if get_locale() == 'en':
        locale.setlocale(locale.LC_TIME,"en_US.UTF-8")
        fmt = '%b %d, %Y, %I:%M:%S %p'
    elif get_locale() == 'fr':
        locale.setlocale(locale.LC_TIME,"fr_FR.UTF-8")
        fmt = '%d %b %Y à %H:%M:%S'
    au_dt = au_dt.strftime(fmt)
    print(au_dt)
    g.current_time = au_dt


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Return a template """
    return render_template('index.html')
