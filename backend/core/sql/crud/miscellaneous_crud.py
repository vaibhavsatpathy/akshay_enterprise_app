from sql import session, logger
from sql.orm_models.miscellaneous import Miscellaneous

logging = logger(__name__)


class CRUDMiscellaneous:
    def create(self, **kwargs):
        try:
            logging.info("CRUDMiscellaneous create request")
            misc = Miscellaneous(**kwargs)
            with session() as transaction_session:
                transaction_session.add(misc)
                transaction_session.commit()
                transaction_session.refresh(misc)
            return misc.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDMiscellaneous create function : {error}")
            raise error

    def read(self, misc_id: int):
        try:
            logging.info("CRUDMiscellaneous read request")
            with session() as transaction_session:
                obj: Miscellaneous = transaction_session.query(Miscellaneous).filter(Miscellaneous.misc_id == misc_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDMiscellaneous read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDMiscellaneous read_all request")
            with session() as transaction_session:
                obj: Miscellaneous = transaction_session.query(Miscellaneous).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDMiscellaneous read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDMiscellaneous update request")
            with session() as transaction_session:
                transaction_session.query(Miscellaneous).filter(Miscellaneous.misc_id == kwargs.get("misc_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDMiscellaneous update function : {error}")
            raise error

    def delete(self, misc_id: int):
        try:
            logging.info("CRUDMiscellaneous delete request")
            with session() as transaction_session:
                obj: Miscellaneous = transaction_session.query(Miscellaneous).filter(Miscellaneous.misc_id == misc_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDMiscellaneous delete function : {error}")
            raise error
