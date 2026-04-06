from sql import session, logger
from sql.orm_models.side_pasting_job import SidePastingJob

logging = logger(__name__)


class CRUDSidePastingJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDSidePastingJob create request")
            job = SidePastingJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDSidePastingJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDSidePastingJob read request")
            with session() as transaction_session:
                obj: SidePastingJob = transaction_session.query(SidePastingJob).filter(SidePastingJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDSidePastingJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDSidePastingJob read_all request")
            with session() as transaction_session:
                obj: SidePastingJob = transaction_session.query(SidePastingJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDSidePastingJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDSidePastingJob update request")
            with session() as transaction_session:
                transaction_session.query(SidePastingJob).filter(SidePastingJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDSidePastingJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDSidePastingJob delete request")
            with session() as transaction_session:
                obj: SidePastingJob = transaction_session.query(SidePastingJob).filter(SidePastingJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDSidePastingJob delete function : {error}")
            raise error
