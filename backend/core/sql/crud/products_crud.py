from sql import session, logger
from sql.orm_models.products import Product

logging = logger(__name__)


class CRUDProduct:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProduct create request")
            product = Product(**kwargs)
            with session() as transaction_session:
                transaction_session.add(product)
                transaction_session.commit()
                transaction_session.refresh(product)
            return product.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProduct create function : {error}")
            raise error

    def read(self, product_id: int):
        try:
            logging.info("CRUDProduct read request")
            with session() as transaction_session:
                obj: Product = transaction_session.query(Product).filter(Product.product_id == product_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProduct read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProduct read_all request")
            with session() as transaction_session:
                obj: Product = transaction_session.query(Product).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProduct read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProduct update request")
            with session() as transaction_session:
                transaction_session.query(Product).filter(Product.product_id == kwargs.get("product_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProduct update function : {error}")
            raise error

    def delete(self, product_id: int):
        try:
            logging.info("CRUDProduct delete request")
            with session() as transaction_session:
                obj: Product = transaction_session.query(Product).filter(Product.product_id == product_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProduct delete function : {error}")
            raise error
