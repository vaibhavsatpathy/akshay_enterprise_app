from sql import session, logger
from sql.orm_models.product_types import ProductType

logging = logger(__name__)


class CRUDProductType:
    def create(self, **kwargs):
        """[CRUD function to create a new ProductType record]"""
        try:
            logging.info("CRUDProductType create request")
            product_type = ProductType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(product_type)
                transaction_session.commit()
                transaction_session.refresh(product_type)
            return product_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductType create function : {error}")
            raise error

    def read(self, product_type_id: int):
        """[CRUD function to read a ProductType record]"""
        try:
            logging.info("CRUDProductType read request")
            with session() as transaction_session:
                obj: ProductType = (
                    transaction_session.query(ProductType)
                    .filter(ProductType.product_type_id == product_type_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductType read function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read all ProductType records]"""
        try:
            logging.info("CRUDProductType read_all request")
            with session() as transaction_session:
                obj: ProductType = transaction_session.query(ProductType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        """[CRUD function to update a ProductType record]"""
        try:
            logging.info("CRUDProductType update request")
            with session() as transaction_session:
                transaction_session.query(ProductType).filter(
                    ProductType.product_type_id == kwargs.get("product_type_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductType update function : {error}")
            raise error

    def delete(self, product_type_id: int):
        """[CRUD function to delete a ProductType record]"""
        try:
            logging.info("CRUDProductType delete request")
            with session() as transaction_session:
                obj: ProductType = (
                    transaction_session.query(ProductType)
                    .filter(ProductType.product_type_id == product_type_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductType delete function : {error}")
            raise error
