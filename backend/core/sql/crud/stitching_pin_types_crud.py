from sql import session, logger
from sql.orm_models.stitching_pin_types import StitchingPinType

logging = logger(__name__)


class CRUDStitchingPinType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDStitchingPinType create request")
            pin_type = StitchingPinType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(pin_type)
                transaction_session.commit()
                transaction_session.refresh(pin_type)
            return pin_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinType create function : {error}")
            raise error

    def read(self, pin_type_id: int):
        try:
            logging.info("CRUDStitchingPinType read request")
            with session() as transaction_session:
                obj: StitchingPinType = transaction_session.query(StitchingPinType).filter(StitchingPinType.pin_type_id == pin_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDStitchingPinType read_all request")
            with session() as transaction_session:
                obj: StitchingPinType = transaction_session.query(StitchingPinType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDStitchingPinType update request")
            with session() as transaction_session:
                transaction_session.query(StitchingPinType).filter(StitchingPinType.pin_type_id == kwargs.get("pin_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinType update function : {error}")
            raise error

    def delete(self, pin_type_id: int):
        try:
            logging.info("CRUDStitchingPinType delete request")
            with session() as transaction_session:
                obj: StitchingPinType = transaction_session.query(StitchingPinType).filter(StitchingPinType.pin_type_id == pin_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinType delete function : {error}")
            raise error
