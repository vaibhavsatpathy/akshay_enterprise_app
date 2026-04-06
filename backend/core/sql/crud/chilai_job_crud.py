from sql import session, logger
from sql.orm_models.chilai_job import ChilaiJob

logging = logger(__name__)


class CRUDChilaiJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDChilaiJob create request")
            job = ChilaiJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDChilaiJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDChilaiJob read request")
            with session() as transaction_session:
                obj: ChilaiJob = transaction_session.query(ChilaiJob).filter(ChilaiJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDChilaiJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDChilaiJob read_all request")
            with session() as transaction_session:
                obj: ChilaiJob = transaction_session.query(ChilaiJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDChilaiJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDChilaiJob update request")
            with session() as transaction_session:
                transaction_session.query(ChilaiJob).filter(ChilaiJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDChilaiJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDChilaiJob delete request")
            with session() as transaction_session:
                obj: ChilaiJob = transaction_session.query(ChilaiJob).filter(ChilaiJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDChilaiJob delete function : {error}")
            raise error
