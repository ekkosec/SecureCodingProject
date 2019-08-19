from app import app, db
from app.models import User
import base64
# from flask import request


def check_user(request):
    if 'uid' in request.cookies.keys():
        user_name = base64.b64decode(str(request.cookies.get('uid'))).decode()
        user = User.query.filter_by(username=user_name).first()
        if user:
            return user
    return False


if __name__ == "__main__":
    check_user()