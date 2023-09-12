from app.db.db_init import make_session, CollectData


def delete_collect_data():
    session = make_session()
    session.query(CollectData).delete()
    session.commit()
    session.close()
