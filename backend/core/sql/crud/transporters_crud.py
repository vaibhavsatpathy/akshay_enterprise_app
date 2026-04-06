from datetime import datetime

from sql import session, logger
from sql.orm_models.transporters import Transporter

logging = logger(__name__)


class CRUDTransporter:
    def create(self, **kwargs):
        try:
            logging.info("CRUDTransporter create request")
            transporter = Transporter(**kwargs)
            transporter.created_at = datetime.now()
            transporter.updated_at = datetime.now()
            with session() as transaction_session:
                transaction_session.add(transporter)
                transaction_session.commit()
                transaction_session.refresh(transporter)
            return transporter.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDTransporter create function : {error}")
            raise error

    def read(self, transporter_id: int):
        try:
            logging.info("CRUDTransporter read request")
            with session() as transaction_session:
                obj: Transporter = (
                    transaction_session.query(Transporter)
                    .filter(Transporter.transporter_id == transporter_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDTransporter read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDTransporter read_all request")
            with session() as transaction_session:
                obj: Transporter = transaction_session.query(Transporter).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDTransporter read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDTransporter update request")
            with session() as transaction_session:
                transaction_session.query(Transporter).filter(
                    Transporter.transporter_id == kwargs.get("transporter_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDTransporter update function : {error}")
            raise error

    def delete(self, transporter_id: int):
        try:
            logging.info("CRUDTransporter delete request")
            with session() as transaction_session:
                obj: Transporter = (
                    transaction_session.query(Transporter)
                    .filter(Transporter.transporter_id == transporter_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDTransporter delete function : {error}")
            raise error
