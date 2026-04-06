from sql import session, logger
from sql.orm_models.product_papers import ProductPaper

logging = logger(__name__)


class CRUDProductPaper:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProductPaper create request")
            paper = ProductPaper(**kwargs)
            with session() as transaction_session:
                transaction_session.add(paper)
                transaction_session.commit()
                transaction_session.refresh(paper)
            return paper.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductPaper create function : {error}")
            raise error

    def read(self, gross_id: int):
        try:
            logging.info("CRUDProductPaper read request")
            with session() as transaction_session:
                obj: ProductPaper = transaction_session.query(ProductPaper).filter(ProductPaper.gross_id == gross_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductPaper read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProductPaper read_all request")
            with session() as transaction_session:
                obj: ProductPaper = transaction_session.query(ProductPaper).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductPaper read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProductPaper update request")
            with session() as transaction_session:
                transaction_session.query(ProductPaper).filter(ProductPaper.gross_id == kwargs.get("gross_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductPaper update function : {error}")
            raise error

    def delete(self, gross_id: int):
        try:
            logging.info("CRUDProductPaper delete request")
            with session() as transaction_session:
                obj: ProductPaper = transaction_session.query(ProductPaper).filter(ProductPaper.gross_id == gross_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductPaper delete function : {error}")
            raise error
