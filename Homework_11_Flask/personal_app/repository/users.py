from personal_app.models import db, User
import bcrypt


def create_user(username, email, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=10))
    user = User(username=username, email=email, hash=hashed)
    db.session.add(user)
    db.session.commit()
    return user


def login(email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user.hash):
            return user
    return None


def set_token(user, token):
    print('SET TOKEN:', user, token)
    user.token_cookie = token
    db.session.commit()


def get_user_by_token(token):
    user = db.session.query(User).filter(User.token_cookie == token).first()
    if not user:
        return None
    return user
