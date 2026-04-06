from sql import session, logger
from sql.orm_models.screen_printing import ScreenPrinting

logging = logger(__name__)


class CRUDScreenPrinting:
    def create(self, **kwargs):
        try:
            logging.info("CRUDScreenPrinting create request")
            print = ScreenPrinting(**kwargs)
            with session() as transaction_session:
                transaction_session.add(print)
                transaction_session.commit()
                transaction_session.refresh(print)
            return print.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDScreenPrinting create function : {error}")
            raise error

    def read(self, print_id: int):
        try:
            logging.info("CRUDScreenPrinting read request")
            with session() as transaction_session:
                obj: ScreenPrinting = transaction_session.query(ScreenPrinting).filter(ScreenPrinting.print_id == print_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDScreenPrinting read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDScreenPrinting read_all request")
            with session() as transaction_session:
                obj: ScreenPrinting = transaction_session.query(ScreenPrinting).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDScreenPrinting read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDScreenPrinting update request")
            with session() as transaction_session:
                transaction_session.query(ScreenPrinting).filter(ScreenPrinting.print_id == kwargs.get("print_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDScreenPrinting update function : {error}")
            raise error

    def delete(self, print_id: int):
        try:
            logging.info("CRUDScreenPrinting delete request")
            with session() as transaction_session:
                obj: ScreenPrinting = transaction_session.query(ScreenPrinting).filter(ScreenPrinting.print_id == print_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDScreenPrinting delete function : {error}")
            raise error
