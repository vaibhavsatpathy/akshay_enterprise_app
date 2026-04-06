from sql import session, logger
from sql.orm_models.rejected_item_types import RejectedItemType

logging = logger(__name__)


class CRUDRejectedItemType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDRejectedItemType create request")
            rejected_item_type = RejectedItemType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(rejected_item_type)
                transaction_session.commit()
                transaction_session.refresh(rejected_item_type)
            return rejected_item_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItemType create function : {error}")
            raise error

    def read(self, rejected_item_type_id: int):
        try:
            logging.info("CRUDRejectedItemType read request")
            with session() as transaction_session:
                obj: RejectedItemType = transaction_session.query(RejectedItemType).filter(RejectedItemType.rejected_item_type_id == rejected_item_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItemType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDRejectedItemType read_all request")
            with session() as transaction_session:
                obj: RejectedItemType = transaction_session.query(RejectedItemType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItemType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDRejectedItemType update request")
            with session() as transaction_session:
                transaction_session.query(RejectedItemType).filter(RejectedItemType.rejected_item_type_id == kwargs.get("rejected_item_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItemType update function : {error}")
            raise error

    def delete(self, rejected_item_type_id: int):
        try:
            logging.info("CRUDRejectedItemType delete request")
            with session() as transaction_session:
                obj: RejectedItemType = transaction_session.query(RejectedItemType).filter(RejectedItemType.rejected_item_type_id == rejected_item_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRejectedItemType delete function : {error}")
            raise error
