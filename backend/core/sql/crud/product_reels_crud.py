from sql import session, logger
from sql.orm_models.product_reels import ProductReel

logging = logger(__name__)


class CRUDProductReel:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProductReel create request")
            reel = ProductReel(**kwargs)
            with session() as transaction_session:
                transaction_session.add(reel)
                transaction_session.commit()
                transaction_session.refresh(reel)
            return reel.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductReel create function : {error}")
            raise error

    def read(self, reel_id: int):
        try:
            logging.info("CRUDProductReel read request")
            with session() as transaction_session:
                obj: ProductReel = transaction_session.query(ProductReel).filter(ProductReel.reel_id == reel_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductReel read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProductReel read_all request")
            with session() as transaction_session:
                obj: ProductReel = transaction_session.query(ProductReel).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductReel read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProductReel update request")
            with session() as transaction_session:
                transaction_session.query(ProductReel).filter(ProductReel.reel_id == kwargs.get("reel_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductReel update function : {error}")
            raise error

    def delete(self, reel_id: int):
        try:
            logging.info("CRUDProductReel delete request")
            with session() as transaction_session:
                obj: ProductReel = transaction_session.query(ProductReel).filter(ProductReel.reel_id == reel_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductReel delete function : {error}")
            raise error
