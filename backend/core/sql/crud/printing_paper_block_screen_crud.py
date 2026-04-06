from sql import session, logger
from sql.orm_models.printing_paper_block_screen import PrintingPaperBlockScreen

logging = logger(__name__)


class CRUDPrintingPaperBlockScreen:
    def create(self, **kwargs):
        try:
            logging.info("CRUDPrintingPaperBlockScreen create request")
            print = PrintingPaperBlockScreen(**kwargs)
            with session() as transaction_session:
                transaction_session.add(print)
                transaction_session.commit()
                transaction_session.refresh(print)
            return print.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperBlockScreen create function : {error}")
            raise error

    def read(self, print_id: int):
        try:
            logging.info("CRUDPrintingPaperBlockScreen read request")
            with session() as transaction_session:
                obj: PrintingPaperBlockScreen = transaction_session.query(PrintingPaperBlockScreen).filter(PrintingPaperBlockScreen.print_id == print_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperBlockScreen read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDPrintingPaperBlockScreen read_all request")
            with session() as transaction_session:
                obj: PrintingPaperBlockScreen = transaction_session.query(PrintingPaperBlockScreen).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperBlockScreen read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDPrintingPaperBlockScreen update request")
            with session() as transaction_session:
                transaction_session.query(PrintingPaperBlockScreen).filter(PrintingPaperBlockScreen.print_id == kwargs.get("print_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperBlockScreen update function : {error}")
            raise error

    def delete(self, print_id: int):
        try:
            logging.info("CRUDPrintingPaperBlockScreen delete request")
            with session() as transaction_session:
                obj: PrintingPaperBlockScreen = transaction_session.query(PrintingPaperBlockScreen).filter(PrintingPaperBlockScreen.print_id == print_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPrintingPaperBlockScreen delete function : {error}")
            raise error
