from sql import session, logger
from sql.orm_models.box_types import BoxType

logging = logger(__name__)


class CRUDBoxType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDBoxType create request")
            box_type = BoxType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(box_type)
                transaction_session.commit()
                transaction_session.refresh(box_type)
            return box_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBoxType create function : {error}")
            raise error

    def read(self, box_type_id: int):
        try:
            logging.info("CRUDBoxType read request")
            with session() as transaction_session:
                obj: BoxType = transaction_session.query(BoxType).filter(BoxType.box_type_id == box_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDBoxType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDBoxType read_all request")
            with session() as transaction_session:
                obj: BoxType = transaction_session.query(BoxType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDBoxType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDBoxType update request")
            with session() as transaction_session:
                transaction_session.query(BoxType).filter(BoxType.box_type_id == kwargs.get("box_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDBoxType update function : {error}")
            raise error

    def delete(self, box_type_id: int):
        try:
            logging.info("CRUDBoxType delete request")
            with session() as transaction_session:
                obj: BoxType = transaction_session.query(BoxType).filter(BoxType.box_type_id == box_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBoxType delete function : {error}")
            raise error
