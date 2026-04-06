from sql import session, logger
from sql.orm_models.bfs import Bf

logging = logger(__name__)


class CRUDBf:
    def create(self, **kwargs):
        """[CRUD function to create a new Bf record]"""
        try:
            logging.info("CRUDBf create request")
            bf = Bf(**kwargs)
            with session() as transaction_session:
                transaction_session.add(bf)
                transaction_session.commit()
                transaction_session.refresh(bf)
            return bf.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBf create function : {error}")
            raise error

    def read(self, bf_id: int):
        """[CRUD function to read a Bf record]"""
        try:
            logging.info("CRUDBf read request")
            with session() as transaction_session:
                obj: Bf = (
                    transaction_session.query(Bf).filter(Bf.bf_id == bf_id).first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDBf read function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read all Bf records]"""
        try:
            logging.info("CRUDBf read_all request")
            with session() as transaction_session:
                obj: Bf = transaction_session.query(Bf).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDBf read_all function : {error}")
            raise error

    def update(self, **kwargs):
        """[CRUD function to update a Bf record]"""
        try:
            logging.info("CRUDBf update request")
            with session() as transaction_session:
                transaction_session.query(Bf).filter(
                    Bf.bf_id == kwargs.get("bf_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDBf update function : {error}")
            raise error

    def delete(self, bf_id: int):
        """[CRUD function to delete a Bf record]"""
        try:
            logging.info("CRUDBf delete request")
            with session() as transaction_session:
                obj: Bf = (
                    transaction_session.query(Bf).filter(Bf.bf_id == bf_id).first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBf delete function : {error}")
            raise error
