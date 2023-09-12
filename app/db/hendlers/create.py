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


def create_collect_data(_type: str, mutability: str, description: str, syntax_examples: str) -> bool:
    session = make_session()
    collect_data = CollectData(type=_type, mutability=mutability,
                               description=description, syntax_examples=syntax_examples)
    session.add(collect_data)
    session.commit()
    session.close()
    return True

