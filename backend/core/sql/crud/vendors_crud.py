from datetime import datetime
from sql import session, logger
from sql.orm_models.vendors import Vendor

logging = logger(__name__)


class CRUDVendor:
    def create(self, **kwargs):
        try:
            logging.info("CRUDVendor create request")
            vendor = Vendor(**kwargs)
            vendor.created_at = datetime.now()
            vendor.updated_at = datetime.now()
            with session() as transaction_session:
                transaction_session.add(vendor)
                transaction_session.commit()
                transaction_session.refresh(vendor)
            return vendor.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDVendor create function : {error}")
            raise error

    def read(self, vendor_id: int):
        try:
            logging.info("CRUDVendor read request")
            with session() as transaction_session:
                obj: Vendor = (
                    transaction_session.query(Vendor)
                    .filter(Vendor.vendor_id == vendor_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDVendor read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDVendor read_all request")
            with session() as transaction_session:
                obj: Vendor = transaction_session.query(Vendor).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDVendor read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDVendor update request")
            with session() as transaction_session:
                transaction_session.query(Vendor).filter(
                    Vendor.vendor_id == kwargs.get("vendor_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDVendor update function : {error}")
            raise error

    def delete(self, vendor_id: int):
        try:
            logging.info("CRUDVendor delete request")
            with session() as transaction_session:
                obj: Vendor = (
                    transaction_session.query(Vendor)
                    .filter(Vendor.vendor_id == vendor_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDVendor delete function : {error}")
            raise error
