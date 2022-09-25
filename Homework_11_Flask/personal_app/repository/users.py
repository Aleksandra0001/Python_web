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
