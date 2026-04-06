from sql import session, logger
from sql.orm_models.product_ply_sheets import ProductPlySheet

logging = logger(__name__)


class CRUDProductPlySheet:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProductPlySheet create request")
            sheet = ProductPlySheet(**kwargs)
            with session() as transaction_session:
                transaction_session.add(sheet)
                transaction_session.commit()
                transaction_session.refresh(sheet)
            return sheet.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductPlySheet create function : {error}")
            raise error

    def read(self, sheet_id: int):
        try:
            logging.info("CRUDProductPlySheet read request")
            with session() as transaction_session:
                obj: ProductPlySheet = transaction_session.query(ProductPlySheet).filter(ProductPlySheet.sheet_id == sheet_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductPlySheet read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProductPlySheet read_all request")
            with session() as transaction_session:
                obj: ProductPlySheet = transaction_session.query(ProductPlySheet).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductPlySheet read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProductPlySheet update request")
            with session() as transaction_session:
                transaction_session.query(ProductPlySheet).filter(ProductPlySheet.sheet_id == kwargs.get("sheet_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductPlySheet update function : {error}")
            raise error

    def delete(self, sheet_id: int):
        try:
            logging.info("CRUDProductPlySheet delete request")
            with session() as transaction_session:
                obj: ProductPlySheet = transaction_session.query(ProductPlySheet).filter(ProductPlySheet.sheet_id == sheet_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductPlySheet delete function : {error}")
            raise error
