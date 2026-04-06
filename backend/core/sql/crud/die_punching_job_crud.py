from sql import session, logger
from sql.orm_models.die_punching_job import DiePunchingJob

logging = logger(__name__)


class CRUDDiePunchingJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDDiePunchingJob create request")
            job = DiePunchingJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDDiePunchingJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDDiePunchingJob read request")
            with session() as transaction_session:
                obj: DiePunchingJob = transaction_session.query(DiePunchingJob).filter(DiePunchingJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDDiePunchingJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDDiePunchingJob read_all request")
            with session() as transaction_session:
                obj: DiePunchingJob = transaction_session.query(DiePunchingJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDDiePunchingJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDDiePunchingJob update request")
            with session() as transaction_session:
                transaction_session.query(DiePunchingJob).filter(DiePunchingJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDDiePunchingJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDDiePunchingJob delete request")
            with session() as transaction_session:
                obj: DiePunchingJob = transaction_session.query(DiePunchingJob).filter(DiePunchingJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDDiePunchingJob delete function : {error}")
            raise error
