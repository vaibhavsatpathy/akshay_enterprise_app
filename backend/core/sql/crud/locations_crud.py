from datetime import datetime
from sql import session, logger
from sql.orm_models.locations import Location

logging = logger(__name__)


class CRUDLocation:
    def create(self, **kwargs):
        try:
            logging.info("CRUDLocation create request")
            location = Location(**kwargs)
            location.created_at = datetime.now()
            location.updated_at = datetime.now()
            with session() as transaction_session:
                transaction_session.add(location)
                transaction_session.commit()
                transaction_session.refresh(location)
            return location.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDLocation create function : {error}")
            raise error

    def read(self, location_id: int):
        try:
            logging.info("CRUDLocation read request")
            with session() as transaction_session:
                obj: Location = (
                    transaction_session.query(Location)
                    .filter(Location.location_id == location_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDLocation read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDLocation read_all request")
            with session() as transaction_session:
                obj: Location = transaction_session.query(Location).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDLocation read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDLocation update request")
            with session() as transaction_session:
                transaction_session.query(Location).filter(
                    Location.location_id == kwargs.get("location_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDLocation update function : {error}")
            raise error

    def delete(self, location_id: int):
        try:
            logging.info("CRUDLocation delete request")
            with session() as transaction_session:
                obj: Location = (
                    transaction_session.query(Location)
                    .filter(Location.location_id == location_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDLocation delete function : {error}")
            raise error
