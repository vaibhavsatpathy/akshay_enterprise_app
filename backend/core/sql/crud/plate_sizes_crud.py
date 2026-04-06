from sql import session, logger
from sql.orm_models.plate_sizes import PlateSize

logging = logger(__name__)


class CRUDPlateSize:
    def create(self, **kwargs):
        try:
            logging.info("CRUDPlateSize create request")
            plate_size = PlateSize(**kwargs)
            with session() as transaction_session:
                transaction_session.add(plate_size)
                transaction_session.commit()
                transaction_session.refresh(plate_size)
            return plate_size.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPlateSize create function : {error}")
            raise error

    def read(self, plate_size_id: int):
        try:
            logging.info("CRUDPlateSize read request")
            with session() as transaction_session:
                obj: PlateSize = transaction_session.query(PlateSize).filter(PlateSize.plate_size_id == plate_size_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDPlateSize read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDPlateSize read_all request")
            with session() as transaction_session:
                obj: PlateSize = transaction_session.query(PlateSize).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDPlateSize read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDPlateSize update request")
            with session() as transaction_session:
                transaction_session.query(PlateSize).filter(PlateSize.plate_size_id == kwargs.get("plate_size_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDPlateSize update function : {error}")
            raise error

    def delete(self, plate_size_id: int):
        try:
            logging.info("CRUDPlateSize delete request")
            with session() as transaction_session:
                obj: PlateSize = transaction_session.query(PlateSize).filter(PlateSize.plate_size_id == plate_size_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPlateSize delete function : {error}")
            raise error
