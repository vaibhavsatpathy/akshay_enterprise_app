from sql import session, logger
from sql.orm_models.rotory_job import RotoryJob

logging = logger(__name__)


class CRUDRotoryJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDRotoryJob create request")
            job = RotoryJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRotoryJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDRotoryJob read request")
            with session() as transaction_session:
                obj: RotoryJob = transaction_session.query(RotoryJob).filter(RotoryJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDRotoryJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDRotoryJob read_all request")
            with session() as transaction_session:
                obj: RotoryJob = transaction_session.query(RotoryJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDRotoryJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDRotoryJob update request")
            with session() as transaction_session:
                transaction_session.query(RotoryJob).filter(RotoryJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDRotoryJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDRotoryJob delete request")
            with session() as transaction_session:
                obj: RotoryJob = transaction_session.query(RotoryJob).filter(RotoryJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRotoryJob delete function : {error}")
            raise error
