from sql import session, logger
from sql.orm_models.printing_paper_offset import PrintingPaperOffset

logging = logger(__name__)


class CRUDPrintingPaperOffset:
    def create(self, **kwargs):
        try:
            logging.info("CRUDPrintingPaperOffset create request")
            print = PrintingPaperOffset(**kwargs)
            with session() as transaction_session:
                transaction_session.add(print)
                transaction_session.commit()
                transaction_session.refresh(print)
            return print.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperOffset create function : {error}")
            raise error

    def read(self, print_id: int):
        try:
            logging.info("CRUDPrintingPaperOffset read request")
            with session() as transaction_session:
                obj: PrintingPaperOffset = transaction_session.query(PrintingPaperOffset).filter(PrintingPaperOffset.print_id == print_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperOffset read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDPrintingPaperOffset read_all request")
            with session() as transaction_session:
                obj: PrintingPaperOffset = transaction_session.query(PrintingPaperOffset).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperOffset read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDPrintingPaperOffset update request")
            with session() as transaction_session:
                transaction_session.query(PrintingPaperOffset).filter(PrintingPaperOffset.print_id == kwargs.get("print_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperOffset update function : {error}")
            raise error

    def delete(self, print_id: int):
        try:
            logging.info("CRUDPrintingPaperOffset delete request")
            with session() as transaction_session:
                obj: PrintingPaperOffset = transaction_session.query(PrintingPaperOffset).filter(PrintingPaperOffset.print_id == print_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperOffset delete function : {error}")
            raise error
