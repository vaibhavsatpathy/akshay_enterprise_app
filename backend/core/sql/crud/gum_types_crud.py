from sql import session, logger
from sql.orm_models.gum_types import GumType

logging = logger(__name__)


class CRUDGumType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDGumType create request")
            gum_type = GumType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(gum_type)
                transaction_session.commit()
                transaction_session.refresh(gum_type)
            return gum_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDGumType create function : {error}")
            raise error

    def read(self, gum_type_id: int):
        try:
            logging.info("CRUDGumType read request")
            with session() as transaction_session:
                obj: GumType = (
                    transaction_session.query(GumType)
                    .filter(GumType.gum_type_id == gum_type_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDGumType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDGumType read_all request")
            with session() as transaction_session:
                obj: GumType = transaction_session.query(GumType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDGumType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDGumType update request")
            with session() as transaction_session:
                transaction_session.query(GumType).filter(
                    GumType.gum_type_id == kwargs.get("gum_type_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDGumType update function : {error}")
            raise error

    def delete(self, gum_type_id: int):
        try:
            logging.info("CRUDGumType delete request")
            with session() as transaction_session:
                obj: GumType = (
                    transaction_session.query(GumType)
                    .filter(GumType.gum_type_id == gum_type_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDGumType delete function : {error}")
            raise error
