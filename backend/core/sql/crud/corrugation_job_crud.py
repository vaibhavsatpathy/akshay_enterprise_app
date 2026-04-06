from sql import session, logger
from sql.orm_models.corrugation_job import CorrugationJob

logging = logger(__name__)


class CRUDCorrugationJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDCorrugationJob create request")
            job = CorrugationJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDCorrugationJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDCorrugationJob read request")
            with session() as transaction_session:
                obj: CorrugationJob = transaction_session.query(CorrugationJob).filter(CorrugationJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDCorrugationJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDCorrugationJob read_all request")
            with session() as transaction_session:
                obj: CorrugationJob = transaction_session.query(CorrugationJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDCorrugationJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDCorrugationJob update request")
            with session() as transaction_session:
                transaction_session.query(CorrugationJob).filter(CorrugationJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDCorrugationJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDCorrugationJob delete request")
            with session() as transaction_session:
                obj: CorrugationJob = transaction_session.query(CorrugationJob).filter(CorrugationJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDCorrugationJob delete function : {error}")
            raise error
