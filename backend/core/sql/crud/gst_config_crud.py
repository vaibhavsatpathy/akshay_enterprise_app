from sql import session, logger
from sql.orm_models.gst_config import GstConfig

logging = logger(__name__)


class CRUDGstConfig:
    def create(self, **kwargs):
        try:
            logging.info("CRUDGstConfig create request")
            gst_config = GstConfig(**kwargs)
            with session() as transaction_session:
                transaction_session.add(gst_config)
                transaction_session.commit()
                transaction_session.refresh(gst_config)
            return gst_config.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDGstConfig create function : {error}")
            raise error

    def read(self, gst_config_id: int):
        try:
            logging.info("CRUDGstConfig read request")
            with session() as transaction_session:
                obj: GstConfig = transaction_session.query(GstConfig).filter(GstConfig.gst_config_id == gst_config_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDGstConfig read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDGstConfig read_all request")
            with session() as transaction_session:
                obj: GstConfig = transaction_session.query(GstConfig).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDGstConfig read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDGstConfig update request")
            with session() as transaction_session:
                transaction_session.query(GstConfig).filter(GstConfig.gst_config_id == kwargs.get("gst_config_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDGstConfig update function : {error}")
            raise error

    def delete(self, gst_config_id: int):
        try:
            logging.info("CRUDGstConfig delete request")
            with session() as transaction_session:
                obj: GstConfig = transaction_session.query(GstConfig).filter(GstConfig.gst_config_id == gst_config_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDGstConfig delete function : {error}")
            raise error
