from app.core.config import settings
from app.core.dependencies import get_db, get_test_db
from app.core.security import get_password_hash
from app.database.models import Item, Role, User
from app.database.db import Base, engine, test_engine


def init_db(engine_to_bind, is_test_db: bool = False) -> None:
    Base.metadata.create_all(bind=engine_to_bind)

    db_gen = get_db()

    if is_test_db:
        db_gen = get_test_db()

    db = next(db_gen)
    items = db.query(Item).all()
    roles = db.query(Role).all()

    if not (items and roles):
        objects = [
            Item(name='apples', quantity=100),
            Role(name='buyer'),
            Role(name='seller'),
        ]
        db.bulk_save_objects(objects)
        db.commit()

    if is_test_db:
        users = db.query(User).all()
        if not users:
            user = User(
                username=settings.TEST_USER_USERNAME,
                password=get_password_hash(settings.TEST_USER_PASSWORD),
                role_id=settings.TEST_USER_ROLE_ID,
            )
            db.add(user)
            db.commit()


if __name__ == '__main__':
    init_db(engine)
    init_db(test_engine, True)
