from app.db.db_init import make_session, User, CollectData
from app.lib.security import hash_password


def create_user(login: str, password: str) -> bool:
    session = make_session()
    password = hash_password(password)
    user = User(login=login, password=password)
    session.add(user)
    session.commit()
    session.close()
    return True


def create_collect_data(collect_data: list) -> bool:
    session = make_session()
    collect_data = CollectData(type=collect_data[0], mutability=collect_data[1],
                               description=collect_data[2], syntax_examples=collect_data[3])
    session.add(collect_data)
    session.commit()
    session.close()
    return True

