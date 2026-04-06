from sql import session, logger
from sql.orm_models.printing_job import PrintingJob

logging = logger(__name__)


class CRUDPrintingJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDPrintingJob create request")
            job = PrintingJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPrintingJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDPrintingJob read request")
            with session() as transaction_session:
                obj: PrintingJob = transaction_session.query(PrintingJob).filter(PrintingJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDPrintingJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDPrintingJob read_all request")
            with session() as transaction_session:
                obj: PrintingJob = transaction_session.query(PrintingJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDPrintingJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDPrintingJob update request")
            with session() as transaction_session:
                transaction_session.query(PrintingJob).filter(PrintingJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDPrintingJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDPrintingJob delete request")
            with session() as transaction_session:
                obj: PrintingJob = transaction_session.query(PrintingJob).filter(PrintingJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDPrintingJob delete function : {error}")
            raise error
