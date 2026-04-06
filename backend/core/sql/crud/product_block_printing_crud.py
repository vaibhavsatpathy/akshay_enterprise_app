from sql import session, logger
from sql.orm_models.product_block_printing import ProductBlockPrinting

logging = logger(__name__)


class CRUDProductBlockPrinting:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProductBlockPrinting create request")
            print = ProductBlockPrinting(**kwargs)
            with session() as transaction_session:
                transaction_session.add(print)
                transaction_session.commit()
                transaction_session.refresh(print)
            return print.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductBlockPrinting create function : {error}")
            raise error

    def read(self, print_id: int):
        try:
            logging.info("CRUDProductBlockPrinting read request")
            with session() as transaction_session:
                obj: ProductBlockPrinting = transaction_session.query(ProductBlockPrinting).filter(ProductBlockPrinting.print_id == print_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductBlockPrinting read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProductBlockPrinting read_all request")
            with session() as transaction_session:
                obj: ProductBlockPrinting = transaction_session.query(ProductBlockPrinting).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductBlockPrinting read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProductBlockPrinting update request")
            with session() as transaction_session:
                transaction_session.query(ProductBlockPrinting).filter(ProductBlockPrinting.print_id == kwargs.get("print_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductBlockPrinting update function : {error}")
            raise error

    def delete(self, print_id: int):
        try:
            logging.info("CRUDProductBlockPrinting delete request")
            with session() as transaction_session:
                obj: ProductBlockPrinting = transaction_session.query(ProductBlockPrinting).filter(ProductBlockPrinting.print_id == print_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductBlockPrinting delete function : {error}")
            raise error
