from sql import session, logger
from sql.orm_models.product_gum import ProductGum

logging = logger(__name__)


class CRUDProductGum:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProductGum create request")
            gum = ProductGum(**kwargs)
            with session() as transaction_session:
                transaction_session.add(gum)
                transaction_session.commit()
                transaction_session.refresh(gum)
            return gum.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductGum create function : {error}")
            raise error

    def read(self, gum_id: int):
        try:
            logging.info("CRUDProductGum read request")
            with session() as transaction_session:
                obj: ProductGum = transaction_session.query(ProductGum).filter(ProductGum.gum_id == gum_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductGum read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProductGum read_all request")
            with session() as transaction_session:
                obj: ProductGum = transaction_session.query(ProductGum).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductGum read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProductGum update request")
            with session() as transaction_session:
                transaction_session.query(ProductGum).filter(ProductGum.gum_id == kwargs.get("gum_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductGum update function : {error}")
            raise error

    def delete(self, gum_id: int):
        try:
            logging.info("CRUDProductGum delete request")
            with session() as transaction_session:
                obj: ProductGum = transaction_session.query(ProductGum).filter(ProductGum.gum_id == gum_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductGum delete function : {error}")
            raise error
