from sql import session, logger
from sql.orm_models.binding_cloth import BindingCloth

logging = logger(__name__)


class CRUDBindingCloth:
    def create(self, **kwargs):
        try:
            logging.info("CRUDBindingCloth create request")
            cloth = BindingCloth(**kwargs)
            with session() as transaction_session:
                transaction_session.add(cloth)
                transaction_session.commit()
                transaction_session.refresh(cloth)
            return cloth.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBindingCloth create function : {error}")
            raise error

    def read(self, cloth_id: int):
        try:
            logging.info("CRUDBindingCloth read request")
            with session() as transaction_session:
                obj: BindingCloth = transaction_session.query(BindingCloth).filter(BindingCloth.cloth_id == cloth_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDBindingCloth read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDBindingCloth read_all request")
            with session() as transaction_session:
                obj: BindingCloth = transaction_session.query(BindingCloth).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDBindingCloth read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDBindingCloth update request")
            with session() as transaction_session:
                transaction_session.query(BindingCloth).filter(BindingCloth.cloth_id == kwargs.get("cloth_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDBindingCloth update function : {error}")
            raise error

    def delete(self, cloth_id: int):
        try:
            logging.info("CRUDBindingCloth delete request")
            with session() as transaction_session:
                obj: BindingCloth = transaction_session.query(BindingCloth).filter(BindingCloth.cloth_id == cloth_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBindingCloth delete function : {error}")
            raise error
