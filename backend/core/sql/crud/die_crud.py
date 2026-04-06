from sql import session, logger
from sql.orm_models.die import Die

logging = logger(__name__)


class CRUDDie:
    def create(self, **kwargs):
        try:
            logging.info("CRUDDie create request")
            die = Die(**kwargs)
            with session() as transaction_session:
                transaction_session.add(die)
                transaction_session.commit()
                transaction_session.refresh(die)
            return die.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDDie create function : {error}")
            raise error

    def read(self, die_id: int):
        try:
            logging.info("CRUDDie read request")
            with session() as transaction_session:
                obj: Die = transaction_session.query(Die).filter(Die.die_id == die_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDDie read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDDie read_all request")
            with session() as transaction_session:
                obj: Die = transaction_session.query(Die).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDDie read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDDie update request")
            with session() as transaction_session:
                transaction_session.query(Die).filter(Die.die_id == kwargs.get("die_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDDie update function : {error}")
            raise error

    def delete(self, die_id: int):
        try:
            logging.info("CRUDDie delete request")
            with session() as transaction_session:
                obj: Die = transaction_session.query(Die).filter(Die.die_id == die_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDDie delete function : {error}")
            raise error
