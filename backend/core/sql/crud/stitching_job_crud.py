from sql import session, logger
from sql.orm_models.stitching_job import StitchingJob

logging = logger(__name__)


class CRUDStitchingJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDStitchingJob create request")
            job = StitchingJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStitchingJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDStitchingJob read request")
            with session() as transaction_session:
                obj: StitchingJob = transaction_session.query(StitchingJob).filter(StitchingJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDStitchingJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDStitchingJob read_all request")
            with session() as transaction_session:
                obj: StitchingJob = transaction_session.query(StitchingJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDStitchingJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDStitchingJob update request")
            with session() as transaction_session:
                transaction_session.query(StitchingJob).filter(StitchingJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDStitchingJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDStitchingJob delete request")
            with session() as transaction_session:
                obj: StitchingJob = transaction_session.query(StitchingJob).filter(StitchingJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStitchingJob delete function : {error}")
            raise error
