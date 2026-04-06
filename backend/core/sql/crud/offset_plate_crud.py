from sql import session, logger
from sql.orm_models.offset_plate import OffsetPlate

logging = logger(__name__)


class CRUDOffsetPlate:
    def create(self, **kwargs):
        try:
            logging.info("CRUDOffsetPlate create request")
            plate = OffsetPlate(**kwargs)
            with session() as transaction_session:
                transaction_session.add(plate)
                transaction_session.commit()
                transaction_session.refresh(plate)
            return plate.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDOffsetPlate create function : {error}")
            raise error

    def read(self, plate_id: int):
        try:
            logging.info("CRUDOffsetPlate read request")
            with session() as transaction_session:
                obj: OffsetPlate = transaction_session.query(OffsetPlate).filter(OffsetPlate.plate_id == plate_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDOffsetPlate read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDOffsetPlate read_all request")
            with session() as transaction_session:
                obj: OffsetPlate = transaction_session.query(OffsetPlate).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDOffsetPlate read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDOffsetPlate update request")
            with session() as transaction_session:
                transaction_session.query(OffsetPlate).filter(OffsetPlate.plate_id == kwargs.get("plate_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDOffsetPlate update function : {error}")
            raise error

    def delete(self, plate_id: int):
        try:
            logging.info("CRUDOffsetPlate delete request")
            with session() as transaction_session:
                obj: OffsetPlate = transaction_session.query(OffsetPlate).filter(OffsetPlate.plate_id == plate_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDOffsetPlate delete function : {error}")
            raise error
