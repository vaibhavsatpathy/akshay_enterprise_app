from sql import session, logger
from sql.orm_models.pasting_job import PastingJob

logging = logger(__name__)


class CRUDPastingJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDPastingJob create request")
            job = PastingJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPastingJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDPastingJob read request")
            with session() as transaction_session:
                obj: PastingJob = transaction_session.query(PastingJob).filter(PastingJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDPastingJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDPastingJob read_all request")
            with session() as transaction_session:
                obj: PastingJob = transaction_session.query(PastingJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDPastingJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDPastingJob update request")
            with session() as transaction_session:
                transaction_session.query(PastingJob).filter(PastingJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDPastingJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDPastingJob delete request")
            with session() as transaction_session:
                obj: PastingJob = transaction_session.query(PastingJob).filter(PastingJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPastingJob delete function : {error}")
            raise error
