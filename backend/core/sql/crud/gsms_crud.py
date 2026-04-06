from datetime import datetime

from sql import session, logger
from sql.orm_models.gsms import Gsm

logging = logger(__name__)


class CRUDGsm:
    def create(self, **kwargs):
        """[CRUD function to create a new Gsm record]"""
        try:
            logging.info("CRUDGsm create request")
            gsm = Gsm(**kwargs)
            gsm.created_at = datetime.now()
            gsm.updated_at = datetime.now()
            with session() as transaction_session:
                transaction_session.add(gsm)
                transaction_session.commit()
                transaction_session.refresh(gsm)
            return gsm.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDGsm create function : {error}")
            raise error

    def read(self, gsm_id: int):
        """[CRUD function to read a Gsm record]"""
        try:
            logging.info("CRUDGsm read request")
            with session() as transaction_session:
                obj: Gsm = (
                    transaction_session.query(Gsm).filter(Gsm.gsm_id == gsm_id).first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDGsm read function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read all Gsm records]"""
        try:
            logging.info("CRUDGsm read_all request")
            with session() as transaction_session:
                obj: Gsm = transaction_session.query(Gsm).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDGsm read_all function : {error}")
            raise error

    def update(self, **kwargs):
        """[CRUD function to update a Gsm record]"""
        try:
            logging.info("CRUDGsm update request")
            with session() as transaction_session:
                transaction_session.query(Gsm).filter(
                    Gsm.gsm_id == kwargs.get("gsm_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDGsm update function : {error}")
            raise error

    def delete(self, gsm_id: int):
        """[CRUD function to delete a Gsm record]"""
        try:
            logging.info("CRUDGsm delete request")
            with session() as transaction_session:
                obj: Gsm = (
                    transaction_session.query(Gsm).filter(Gsm.gsm_id == gsm_id).first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDGsm delete function : {error}")
            raise error
