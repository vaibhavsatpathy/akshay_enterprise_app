from sql import session, logger
from sql.orm_models.slot_job import SlotJob

logging = logger(__name__)


class CRUDSlotJob:
    def create(self, **kwargs):
        try:
            logging.info("CRUDSlotJob create request")
            job = SlotJob(**kwargs)
            with session() as transaction_session:
                transaction_session.add(job)
                transaction_session.commit()
                transaction_session.refresh(job)
            return job.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDSlotJob create function : {error}")
            raise error

    def read(self, job_id: int):
        try:
            logging.info("CRUDSlotJob read request")
            with session() as transaction_session:
                obj: SlotJob = transaction_session.query(SlotJob).filter(SlotJob.job_id == job_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDSlotJob read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDSlotJob read_all request")
            with session() as transaction_session:
                obj: SlotJob = transaction_session.query(SlotJob).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDSlotJob read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDSlotJob update request")
            with session() as transaction_session:
                transaction_session.query(SlotJob).filter(SlotJob.job_id == kwargs.get("job_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDSlotJob update function : {error}")
            raise error

    def delete(self, job_id: int):
        try:
            logging.info("CRUDSlotJob delete request")
            with session() as transaction_session:
                obj: SlotJob = transaction_session.query(SlotJob).filter(SlotJob.job_id == job_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDSlotJob delete function : {error}")
            raise error
