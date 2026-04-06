from sql import session, logger
from sql.orm_models.file_placing import FilePlacing

logging = logger(__name__)


class CRUDFilePlacing:
    def create(self, **kwargs):
        try:
            logging.info("CRUDFilePlacing create request")
            file = FilePlacing(**kwargs)
            with session() as transaction_session:
                transaction_session.add(file)
                transaction_session.commit()
                transaction_session.refresh(file)
            return file.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDFilePlacing create function : {error}")
            raise error

    def read(self, file_id: int):
        try:
            logging.info("CRUDFilePlacing read request")
            with session() as transaction_session:
                obj: FilePlacing = transaction_session.query(FilePlacing).filter(FilePlacing.file_id == file_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDFilePlacing read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDFilePlacing read_all request")
            with session() as transaction_session:
                obj: FilePlacing = transaction_session.query(FilePlacing).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDFilePlacing read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDFilePlacing update request")
            with session() as transaction_session:
                transaction_session.query(FilePlacing).filter(FilePlacing.file_id == kwargs.get("file_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDFilePlacing update function : {error}")
            raise error

    def delete(self, file_id: int):
        try:
            logging.info("CRUDFilePlacing delete request")
            with session() as transaction_session:
                obj: FilePlacing = transaction_session.query(FilePlacing).filter(FilePlacing.file_id == file_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDFilePlacing delete function : {error}")
            raise error
