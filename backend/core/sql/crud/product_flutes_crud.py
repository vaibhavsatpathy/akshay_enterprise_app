from sql import session, logger
from sql.orm_models.product_flutes import ProductFlute

logging = logger(__name__)


class CRUDProductFlute:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProductFlute create request")
            flute = ProductFlute(**kwargs)
            with session() as transaction_session:
                transaction_session.add(flute)
                transaction_session.commit()
                transaction_session.refresh(flute)
            return flute.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductFlute create function : {error}")
            raise error

    def read(self, flute_id: int):
        try:
            logging.info("CRUDProductFlute read request")
            with session() as transaction_session:
                obj: ProductFlute = transaction_session.query(ProductFlute).filter(ProductFlute.flute_id == flute_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductFlute read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProductFlute read_all request")
            with session() as transaction_session:
                obj: ProductFlute = transaction_session.query(ProductFlute).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductFlute read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProductFlute update request")
            with session() as transaction_session:
                transaction_session.query(ProductFlute).filter(ProductFlute.flute_id == kwargs.get("flute_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductFlute update function : {error}")
            raise error

    def delete(self, flute_id: int):
        try:
            logging.info("CRUDProductFlute delete request")
            with session() as transaction_session:
                obj: ProductFlute = transaction_session.query(ProductFlute).filter(ProductFlute.flute_id == flute_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductFlute delete function : {error}")
            raise error
