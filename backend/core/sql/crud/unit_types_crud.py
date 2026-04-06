from sql import session, logger
from sql.orm_models.unit_types import UnitType

logging = logger(__name__)


class CRUDUnitType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDUnitType create request")
            unit_type = UnitType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(unit_type)
                transaction_session.commit()
                transaction_session.refresh(unit_type)
            return unit_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDUnitType create function : {error}")
            raise error

    def read(self, unit_type_id: int):
        try:
            logging.info("CRUDUnitType read request")
            with session() as transaction_session:
                obj: UnitType = (
                    transaction_session.query(UnitType)
                    .filter(UnitType.unit_type_id == unit_type_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDUnitType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDUnitType read_all request")
            with session() as transaction_session:
                obj: UnitType = transaction_session.query(UnitType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDUnitType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDUnitType update request")
            with session() as transaction_session:
                transaction_session.query(UnitType).filter(
                    UnitType.unit_type_id == kwargs.get("unit_type_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDUnitType update function : {error}")
            raise error

    def delete(self, unit_type_id: int):
        try:
            logging.info("CRUDUnitType delete request")
            with session() as transaction_session:
                obj: UnitType = (
                    transaction_session.query(UnitType)
                    .filter(UnitType.unit_type_id == unit_type_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDUnitType delete function : {error}")
            raise error
