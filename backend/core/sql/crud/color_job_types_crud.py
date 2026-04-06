from sql import session, logger
from sql.orm_models.color_job_types import ColorJobType

logging = logger(__name__)


class CRUDColorJobType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDColorJobType create request")
            color_job_type = ColorJobType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(color_job_type)
                transaction_session.commit()
                transaction_session.refresh(color_job_type)
            return color_job_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDColorJobType create function : {error}")
            raise error

    def read(self, color_job_type_id: int):
        try:
            logging.info("CRUDColorJobType read request")
            with session() as transaction_session:
                obj: ColorJobType = transaction_session.query(ColorJobType).filter(ColorJobType.color_job_type_id == color_job_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDColorJobType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDColorJobType read_all request")
            with session() as transaction_session:
                obj: ColorJobType = transaction_session.query(ColorJobType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDColorJobType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDColorJobType update request")
            with session() as transaction_session:
                transaction_session.query(ColorJobType).filter(ColorJobType.color_job_type_id == kwargs.get("color_job_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDColorJobType update function : {error}")
            raise error

    def delete(self, color_job_type_id: int):
        try:
            logging.info("CRUDColorJobType delete request")
            with session() as transaction_session:
                obj: ColorJobType = transaction_session.query(ColorJobType).filter(ColorJobType.color_job_type_id == color_job_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDColorJobType delete function : {error}")
            raise error
