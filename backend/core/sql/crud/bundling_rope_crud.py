from sql import session, logger
from sql.orm_models.bundling_rope import BundlingRope

logging = logger(__name__)


class CRUDBundlingRope:
    def create(self, **kwargs):
        try:
            logging.info("CRUDBundlingRope create request")
            bundle = BundlingRope(**kwargs)
            with session() as transaction_session:
                transaction_session.add(bundle)
                transaction_session.commit()
                transaction_session.refresh(bundle)
            return bundle.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBundlingRope create function : {error}")
            raise error

    def read(self, bundle_id: int):
        try:
            logging.info("CRUDBundlingRope read request")
            with session() as transaction_session:
                obj: BundlingRope = transaction_session.query(BundlingRope).filter(BundlingRope.bundle_id == bundle_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDBundlingRope read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDBundlingRope read_all request")
            with session() as transaction_session:
                obj: BundlingRope = transaction_session.query(BundlingRope).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDBundlingRope read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDBundlingRope update request")
            with session() as transaction_session:
                transaction_session.query(BundlingRope).filter(BundlingRope.bundle_id == kwargs.get("bundle_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDBundlingRope update function : {error}")
            raise error

    def delete(self, bundle_id: int):
        try:
            logging.info("CRUDBundlingRope delete request")
            with session() as transaction_session:
                obj: BundlingRope = transaction_session.query(BundlingRope).filter(BundlingRope.bundle_id == bundle_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBundlingRope delete function : {error}")
            raise error
