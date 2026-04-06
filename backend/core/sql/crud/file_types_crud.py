from sql import session, logger
from sql.orm_models.file_types import FileType

logging = logger(__name__)


class CRUDFileType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDFileType create request")
            file_type = FileType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(file_type)
                transaction_session.commit()
                transaction_session.refresh(file_type)
            return file_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDFileType create function : {error}")
            raise error

    def read(self, file_type_id: int):
        try:
            logging.info("CRUDFileType read request")
            with session() as transaction_session:
                obj: FileType = transaction_session.query(FileType).filter(FileType.file_type_id == file_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDFileType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDFileType read_all request")
            with session() as transaction_session:
                obj: FileType = transaction_session.query(FileType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDFileType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDFileType update request")
            with session() as transaction_session:
                transaction_session.query(FileType).filter(FileType.file_type_id == kwargs.get("file_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDFileType update function : {error}")
            raise error

    def delete(self, file_type_id: int):
        try:
            logging.info("CRUDFileType delete request")
            with session() as transaction_session:
                obj: FileType = transaction_session.query(FileType).filter(FileType.file_type_id == file_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDFileType delete function : {error}")
            raise error
