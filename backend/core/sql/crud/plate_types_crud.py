from sql import session, logger
from sql.orm_models.plate_types import PlateType

logging = logger(__name__)


class CRUDPlateType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDPlateType create request")
            plate_type = PlateType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(plate_type)
                transaction_session.commit()
                transaction_session.refresh(plate_type)
            return plate_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPlateType create function : {error}")
            raise error

    def read(self, plate_type_id: int):
        try:
            logging.info("CRUDPlateType read request")
            with session() as transaction_session:
                obj: PlateType = transaction_session.query(PlateType).filter(PlateType.plate_type_id == plate_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDPlateType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDPlateType read_all request")
            with session() as transaction_session:
                obj: PlateType = transaction_session.query(PlateType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDPlateType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDPlateType update request")
            with session() as transaction_session:
                transaction_session.query(PlateType).filter(PlateType.plate_type_id == kwargs.get("plate_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDPlateType update function : {error}")
            raise error

    def delete(self, plate_type_id: int):
        try:
            logging.info("CRUDPlateType delete request")
            with session() as transaction_session:
                obj: PlateType = transaction_session.query(PlateType).filter(PlateType.plate_type_id == plate_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPlateType delete function : {error}")
            raise error
