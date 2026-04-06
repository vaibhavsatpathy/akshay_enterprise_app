from sql import session, logger
from sql.orm_models.rs4_job import Rs4Job

logging = logger(__name__)


class CRUDRs4Job:
    def create(self, **kwargs):
        try:
            logging.info("CRUDRs4Job create request")
            job = Rs4Job(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRs4Job create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDRs4Job read request")
            with session() as transaction_session:
                obj: Rs4Job = transaction_session.query(Rs4Job).filter(Rs4Job.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDRs4Job read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDRs4Job read_all request")
            with session() as transaction_session:
                obj: Rs4Job = transaction_session.query(Rs4Job).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDRs4Job read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDRs4Job update request")
            with session() as transaction_session:
                transaction_session.query(Rs4Job).filter(Rs4Job.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDRs4Job update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDRs4Job delete request")
            with session() as transaction_session:
                obj: Rs4Job = transaction_session.query(Rs4Job).filter(Rs4Job.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDRs4Job delete function : {error}")
            raise error
