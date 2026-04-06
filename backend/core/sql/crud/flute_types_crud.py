from sql import session, logger
from sql.orm_models.flute_types import FluteType

logging = logger(__name__)


class CRUDFluteType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDFluteType create request")
            flute_type = FluteType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(flute_type)
                transaction_session.commit()
                transaction_session.refresh(flute_type)
            return flute_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDFluteType create function : {error}")
            raise error

    def read(self, flute_type_id: int):
        try:
            logging.info("CRUDFluteType read request")
            with session() as transaction_session:
                obj: FluteType = (
                    transaction_session.query(FluteType)
                    .filter(FluteType.flute_type_id == flute_type_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDFluteType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDFluteType read_all request")
            with session() as transaction_session:
                obj: FluteType = transaction_session.query(FluteType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDFluteType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDFluteType update request")
            with session() as transaction_session:
                transaction_session.query(FluteType).filter(
                    FluteType.flute_type_id == kwargs.get("flute_type_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDFluteType update function : {error}")
            raise error

    def delete(self, flute_type_id: int):
        try:
            logging.info("CRUDFluteType delete request")
            with session() as transaction_session:
                obj: FluteType = (
                    transaction_session.query(FluteType)
                    .filter(FluteType.flute_type_id == flute_type_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDFluteType delete function : {error}")
            raise error
