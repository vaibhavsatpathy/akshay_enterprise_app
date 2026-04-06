from sql import session, logger
from sql.orm_models.product_paper_bundles import ProductPaperBundle

logging = logger(__name__)


class CRUDProductPaperBundle:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProductPaperBundle create request")
            bundle = ProductPaperBundle(**kwargs)
            with session() as transaction_session:
                transaction_session.add(bundle)
                transaction_session.commit()
                transaction_session.refresh(bundle)
            return bundle.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductPaperBundle create function : {error}")
            raise error

    def read(self, bundle_id: int):
        try:
            logging.info("CRUDProductPaperBundle read request")
            with session() as transaction_session:
                obj: ProductPaperBundle = transaction_session.query(ProductPaperBundle).filter(ProductPaperBundle.bundle_id == bundle_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductPaperBundle read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProductPaperBundle read_all request")
            with session() as transaction_session:
                obj: ProductPaperBundle = transaction_session.query(ProductPaperBundle).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductPaperBundle read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProductPaperBundle update request")
            with session() as transaction_session:
                transaction_session.query(ProductPaperBundle).filter(ProductPaperBundle.bundle_id == kwargs.get("bundle_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductPaperBundle update function : {error}")
            raise error

    def delete(self, bundle_id: int):
        try:
            logging.info("CRUDProductPaperBundle delete request")
            with session() as transaction_session:
                obj: ProductPaperBundle = transaction_session.query(ProductPaperBundle).filter(ProductPaperBundle.bundle_id == bundle_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductPaperBundle delete function : {error}")
            raise error
