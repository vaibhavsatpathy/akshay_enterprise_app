from sql import session, logger
from sql.orm_models.paper_types import PaperType

logging = logger(__name__)


class CRUDPaperType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDPaperType create request")
            paper_type = PaperType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(paper_type)
                transaction_session.commit()
                transaction_session.refresh(paper_type)
            return paper_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPaperType create function : {error}")
            raise error

    def read(self, paper_type_id: int):
        try:
            logging.info("CRUDPaperType read request")
            with session() as transaction_session:
                obj: PaperType = transaction_session.query(PaperType).filter(PaperType.paper_type_id == paper_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDPaperType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDPaperType read_all request")
            with session() as transaction_session:
                obj: PaperType = transaction_session.query(PaperType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDPaperType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDPaperType update request")
            with session() as transaction_session:
                transaction_session.query(PaperType).filter(PaperType.paper_type_id == kwargs.get("paper_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDPaperType update function : {error}")
            raise error

    def delete(self, paper_type_id: int):
        try:
            logging.info("CRUDPaperType delete request")
            with session() as transaction_session:
                obj: PaperType = transaction_session.query(PaperType).filter(PaperType.paper_type_id == paper_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPaperType delete function : {error}")
            raise error
