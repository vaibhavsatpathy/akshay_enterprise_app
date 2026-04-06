from sql import session, logger
from sql.orm_models.bundeling_job import BundelingJob

logging = logger(__name__)


class CRUDBundelingJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDBundelingJob create request")
            job = BundelingJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBundelingJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDBundelingJob read request")
            with session() as transaction_session:
                obj: BundelingJob = transaction_session.query(BundelingJob).filter(BundelingJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDBundelingJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDBundelingJob read_all request")
            with session() as transaction_session:
                obj: BundelingJob = transaction_session.query(BundelingJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDBundelingJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDBundelingJob update request")
            with session() as transaction_session:
                transaction_session.query(BundelingJob).filter(BundelingJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDBundelingJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDBundelingJob delete request")
            with session() as transaction_session:
                obj: BundelingJob = transaction_session.query(BundelingJob).filter(BundelingJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBundelingJob delete function : {error}")
            raise error
