from sql import session, logger
from sql.orm_models.product_stitching_pin import ProductStitchingPin

logging = logger(__name__)


class CRUDProductStitchingPin:
    def create(self, **kwargs):
        try:
            logging.info("CRUDProductStitchingPin create request")
            pin = ProductStitchingPin(**kwargs)
            with session() as transaction_session:
                transaction_session.add(pin)
                transaction_session.commit()
                transaction_session.refresh(pin)
            return pin.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductStitchingPin create function : {error}")
            raise error

    def read(self, pin_id: int):
        try:
            logging.info("CRUDProductStitchingPin read request")
            with session() as transaction_session:
                obj: ProductStitchingPin = transaction_session.query(ProductStitchingPin).filter(ProductStitchingPin.pin_id == pin_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDProductStitchingPin read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDProductStitchingPin read_all request")
            with session() as transaction_session:
                obj: ProductStitchingPin = transaction_session.query(ProductStitchingPin).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDProductStitchingPin read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDProductStitchingPin update request")
            with session() as transaction_session:
                transaction_session.query(ProductStitchingPin).filter(ProductStitchingPin.pin_id == kwargs.get("pin_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDProductStitchingPin update function : {error}")
            raise error

    def delete(self, pin_id: int):
        try:
            logging.info("CRUDProductStitchingPin delete request")
            with session() as transaction_session:
                obj: ProductStitchingPin = transaction_session.query(ProductStitchingPin).filter(ProductStitchingPin.pin_id == pin_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProductStitchingPin delete function : {error}")
            raise error
