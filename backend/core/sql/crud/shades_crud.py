from datetime import datetime
from sql import session, logger
from sql.orm_models.shades import Shade

logging = logger(__name__)


class CRUDShade:
    def create(self, **kwargs):
        try:
            logging.info("CRUDShade create request")
            shade = Shade(**kwargs)
            shade.created_at = datetime.now()
            shade.updated_at = datetime.now()
            with session() as transaction_session:
                transaction_session.add(shade)
                transaction_session.commit()
                transaction_session.refresh(shade)
            return shade.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDShade create function : {error}")
            raise error

    def read(self, shade_id: int):
        try:
            logging.info("CRUDShade read request")
            with session() as transaction_session:
                obj: Shade = (
                    transaction_session.query(Shade)
                    .filter(Shade.shade_id == shade_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDShade read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDShade read_all request")
            with session() as transaction_session:
                obj: Shade = transaction_session.query(Shade).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDShade read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDShade update request")
            with session() as transaction_session:
                transaction_session.query(Shade).filter(
                    Shade.shade_id == kwargs.get("shade_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDShade update function : {error}")
            raise error

    def delete(self, shade_id: int):
        try:
            logging.info("CRUDShade delete request")
            with session() as transaction_session:
                obj: Shade = (
                    transaction_session.query(Shade)
                    .filter(Shade.shade_id == shade_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDShade delete function : {error}")
            raise error
