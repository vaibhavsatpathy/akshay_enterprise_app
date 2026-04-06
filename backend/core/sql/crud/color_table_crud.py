from sql import session, logger
from sql.orm_models.color_table import ColorTable

logging = logger(__name__)


class CRUDColorTable:
    def create(self, **kwargs):
        try:
            logging.info("CRUDColorTable create request")
            color = ColorTable(**kwargs)
            with session() as transaction_session:
                transaction_session.add(color)
                transaction_session.commit()
                transaction_session.refresh(color)
            return color.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDColorTable create function : {error}")
            raise error

    def read(self, color_id: int):
        try:
            logging.info("CRUDColorTable read request")
            with session() as transaction_session:
                obj: ColorTable = transaction_session.query(ColorTable).filter(ColorTable.color_id == color_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDColorTable read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDColorTable read_all request")
            with session() as transaction_session:
                obj: ColorTable = transaction_session.query(ColorTable).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDColorTable read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDColorTable update request")
            with session() as transaction_session:
                transaction_session.query(ColorTable).filter(ColorTable.color_id == kwargs.get("color_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDColorTable update function : {error}")
            raise error

    def delete(self, color_id: int):
        try:
            logging.info("CRUDColorTable delete request")
            with session() as transaction_session:
                obj: ColorTable = transaction_session.query(ColorTable).filter(ColorTable.color_id == color_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDColorTable delete function : {error}")
            raise error
