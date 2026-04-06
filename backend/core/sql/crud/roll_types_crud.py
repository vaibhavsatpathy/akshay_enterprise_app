from sql import session, logger
from sql.orm_models.roll_types import RollType

logging = logger(__name__)


class CRUDRollType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDRollType create request")
            roll_type = RollType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(roll_type)
                transaction_session.commit()
                transaction_session.refresh(roll_type)
            return roll_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRollType create function : {error}")
            raise error

    def read(self, roll_type_id: int):
        try:
            logging.info("CRUDRollType read request")
            with session() as transaction_session:
                obj: RollType = transaction_session.query(RollType).filter(RollType.roll_type_id == roll_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDRollType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDRollType read_all request")
            with session() as transaction_session:
                obj: RollType = transaction_session.query(RollType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDRollType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDRollType update request")
            with session() as transaction_session:
                transaction_session.query(RollType).filter(RollType.roll_type_id == kwargs.get("roll_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDRollType update function : {error}")
            raise error

    def delete(self, roll_type_id: int):
        try:
            logging.info("CRUDRollType delete request")
            with session() as transaction_session:
                obj: RollType = transaction_session.query(RollType).filter(RollType.roll_type_id == roll_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRollType delete function : {error}")
            raise error
