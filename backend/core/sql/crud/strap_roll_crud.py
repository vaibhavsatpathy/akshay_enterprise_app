from sql import session, logger
from sql.orm_models.strap_roll import StrapRoll

logging = logger(__name__)


class CRUDStrapRoll:
    def create(self, **kwargs):
        try:
            logging.info("CRUDStrapRoll create request")
            roll = StrapRoll(**kwargs)
            with session() as transaction_session:
                transaction_session.add(roll)
                transaction_session.commit()
                transaction_session.refresh(roll)
            return roll.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStrapRoll create function : {error}")
            raise error

    def read(self, roll_id: int):
        try:
            logging.info("CRUDStrapRoll read request")
            with session() as transaction_session:
                obj: StrapRoll = transaction_session.query(StrapRoll).filter(StrapRoll.roll_id == roll_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDStrapRoll read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDStrapRoll read_all request")
            with session() as transaction_session:
                obj: StrapRoll = transaction_session.query(StrapRoll).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDStrapRoll read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDStrapRoll update request")
            with session() as transaction_session:
                transaction_session.query(StrapRoll).filter(StrapRoll.roll_id == kwargs.get("roll_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDStrapRoll update function : {error}")
            raise error

    def delete(self, roll_id: int):
        try:
            logging.info("CRUDStrapRoll delete request")
            with session() as transaction_session:
                obj: StrapRoll = transaction_session.query(StrapRoll).filter(StrapRoll.roll_id == roll_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStrapRoll delete function : {error}")
            raise error
