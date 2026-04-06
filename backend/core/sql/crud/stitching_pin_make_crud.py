from sql import session, logger
from sql.orm_models.stitching_pin_make import StitchingPinMake

logging = logger(__name__)


class CRUDStitchingPinMake:
    def create(self, **kwargs):
        try:
            logging.info("CRUDStitchingPinMake create request")
            make = StitchingPinMake(**kwargs)
            with session() as transaction_session:
                transaction_session.add(make)
                transaction_session.commit()
                transaction_session.refresh(make)
            return make.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMake create function : {error}")
            raise error

    def read(self, make_id: int):
        try:
            logging.info("CRUDStitchingPinMake read request")
            with session() as transaction_session:
                obj: StitchingPinMake = transaction_session.query(StitchingPinMake).filter(StitchingPinMake.make_id == make_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMake read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDStitchingPinMake read_all request")
            with session() as transaction_session:
                obj: StitchingPinMake = transaction_session.query(StitchingPinMake).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMake read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDStitchingPinMake update request")
            with session() as transaction_session:
                transaction_session.query(StitchingPinMake).filter(StitchingPinMake.make_id == kwargs.get("make_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMake update function : {error}")
            raise error

    def delete(self, make_id: int):
        try:
            logging.info("CRUDStitchingPinMake delete request")
            with session() as transaction_session:
                obj: StitchingPinMake = transaction_session.query(StitchingPinMake).filter(StitchingPinMake.make_id == make_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMake delete function : {error}")
            raise error
