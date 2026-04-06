from sql import session, logger
from sql.orm_models.paper_cutting_job import PaperCuttingJob

logging = logger(__name__)


class CRUDPaperCuttingJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDPaperCuttingJob create request")
            job = PaperCuttingJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPaperCuttingJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDPaperCuttingJob read request")
            with session() as transaction_session:
                obj: PaperCuttingJob = transaction_session.query(PaperCuttingJob).filter(PaperCuttingJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDPaperCuttingJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDPaperCuttingJob read_all request")
            with session() as transaction_session:
                obj: PaperCuttingJob = transaction_session.query(PaperCuttingJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDPaperCuttingJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDPaperCuttingJob update request")
            with session() as transaction_session:
                transaction_session.query(PaperCuttingJob).filter(PaperCuttingJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDPaperCuttingJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDPaperCuttingJob delete request")
            with session() as transaction_session:
                obj: PaperCuttingJob = transaction_session.query(PaperCuttingJob).filter(PaperCuttingJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPaperCuttingJob delete function : {error}")
            raise error
