from sql import session, logger
from sql.orm_models.product_spare_parts import ProductSparePart

logging = logger(__name__)


class CRUDProductSparePart:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProductSparePart create request")
            part = ProductSparePart(**kwargs)
            with session() as transaction_session:
                transaction_session.add(part)
                transaction_session.commit()
                transaction_session.refresh(part)
            return part.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductSparePart create function : {error}")
            raise error

    def read(self, part_id: int):
        try:
            logging.info("CRUDProductSparePart read request")
            with session() as transaction_session:
                obj: ProductSparePart = transaction_session.query(ProductSparePart).filter(ProductSparePart.part_id == part_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductSparePart read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProductSparePart read_all request")
            with session() as transaction_session:
                obj: ProductSparePart = transaction_session.query(ProductSparePart).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductSparePart read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProductSparePart update request")
            with session() as transaction_session:
                transaction_session.query(ProductSparePart).filter(ProductSparePart.part_id == kwargs.get("part_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductSparePart update function : {error}")
            raise error

    def delete(self, part_id: int):
        try:
            logging.info("CRUDProductSparePart delete request")
            with session() as transaction_session:
                obj: ProductSparePart = transaction_session.query(ProductSparePart).filter(ProductSparePart.part_id == part_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductSparePart delete function : {error}")
            raise error
