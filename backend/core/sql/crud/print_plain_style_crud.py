from sql import session, logger
from sql.orm_models.print_plain_style import PrintPlainStyle

logging = logger(__name__)


class CRUDPrintPlainStyle:
    def create(self, **kwargs):
        try:
            logging.info("CRUDPrintPlainStyle create request")
            print_plain_style = PrintPlainStyle(**kwargs)
            with session() as transaction_session:
                transaction_session.add(print_plain_style)
                transaction_session.commit()
                transaction_session.refresh(print_plain_style)
            return print_plain_style.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPrintPlainStyle create function : {error}")
            raise error

    def read(self, print_plain_style_id: int):
        try:
            logging.info("CRUDPrintPlainStyle read request")
            with session() as transaction_session:
                obj: PrintPlainStyle = transaction_session.query(PrintPlainStyle).filter(PrintPlainStyle.print_plain_style_id == print_plain_style_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDPrintPlainStyle read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDPrintPlainStyle read_all request")
            with session() as transaction_session:
                obj: PrintPlainStyle = transaction_session.query(PrintPlainStyle).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDPrintPlainStyle read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDPrintPlainStyle update request")
            with session() as transaction_session:
                transaction_session.query(PrintPlainStyle).filter(PrintPlainStyle.print_plain_style_id == kwargs.get("print_plain_style_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDPrintPlainStyle update function : {error}")
            raise error

    def delete(self, print_plain_style_id: int):
        try:
            logging.info("CRUDPrintPlainStyle delete request")
            with session() as transaction_session:
                obj: PrintPlainStyle = transaction_session.query(PrintPlainStyle).filter(PrintPlainStyle.print_plain_style_id == print_plain_style_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPrintPlainStyle delete function : {error}")
            raise error
