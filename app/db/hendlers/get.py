from typing import Tuple

from app.db.db_init import User, make_session, CollectData


def get_user(login: str) -> dict:
    session = make_session()
    user = session.query(User).filter(User.login == login).first()
    session.close()
    return user


def get_all_collect_data() -> Tuple[list]:
    session = make_session()
    collect_data = session.query(CollectData).all()
    session.close()
    return collect_data
