from sql import session, logger
from sql.orm_models.rejected_items import RejectedItem

logging = logger(__name__)


class CRUDRejectedItem:
    def create(self, **kwargs):
        try:
            logging.info("CRUDRejectedItem create request")
            rejected = RejectedItem(**kwargs)
            with session() as transaction_session:
                transaction_session.add(rejected)
                transaction_session.commit()
                transaction_session.refresh(rejected)
            return rejected.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItem create function : {error}")
            raise error

    def read(self, rejected_id: int):
        try:
            logging.info("CRUDRejectedItem read request")
            with session() as transaction_session:
                obj: RejectedItem = transaction_session.query(RejectedItem).filter(RejectedItem.rejected_id == rejected_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItem read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDRejectedItem read_all request")
            with session() as transaction_session:
                obj: RejectedItem = transaction_session.query(RejectedItem).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItem read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDRejectedItem update request")
            with session() as transaction_session:
                transaction_session.query(RejectedItem).filter(RejectedItem.rejected_id == kwargs.get("rejected_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItem update function : {error}")
            raise error

    def delete(self, rejected_id: int):
        try:
            logging.info("CRUDRejectedItem delete request")
            with session() as transaction_session:
                obj: RejectedItem = transaction_session.query(RejectedItem).filter(RejectedItem.rejected_id == rejected_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItem delete function : {error}")
            raise error
