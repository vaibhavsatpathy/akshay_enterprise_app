from sql import session, logger
from sql.orm_models.single_two_pieces_type import SingleTwoPiecesType

logging = logger(__name__)


class CRUDSingleTwoPiecesType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDSingleTwoPiecesType create request")
            single_two_pieces_type = SingleTwoPiecesType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(single_two_pieces_type)
                transaction_session.commit()
                transaction_session.refresh(single_two_pieces_type)
            return single_two_pieces_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDSingleTwoPiecesType create function : {error}")
            raise error

    def read(self, single_two_pieces_type_id: int):
        try:
            logging.info("CRUDSingleTwoPiecesType read request")
            with session() as transaction_session:
                obj: SingleTwoPiecesType = transaction_session.query(SingleTwoPiecesType).filter(SingleTwoPiecesType.single_two_pieces_type_id == single_two_pieces_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDSingleTwoPiecesType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDSingleTwoPiecesType read_all request")
            with session() as transaction_session:
                obj: SingleTwoPiecesType = transaction_session.query(SingleTwoPiecesType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDSingleTwoPiecesType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDSingleTwoPiecesType update request")
            with session() as transaction_session:
                transaction_session.query(SingleTwoPiecesType).filter(SingleTwoPiecesType.single_two_pieces_type_id == kwargs.get("single_two_pieces_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDSingleTwoPiecesType update function : {error}")
            raise error

    def delete(self, single_two_pieces_type_id: int):
        try:
            logging.info("CRUDSingleTwoPiecesType delete request")
            with session() as transaction_session:
                obj: SingleTwoPiecesType = transaction_session.query(SingleTwoPiecesType).filter(SingleTwoPiecesType.single_two_pieces_type_id == single_two_pieces_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDSingleTwoPiecesType delete function : {error}")
            raise error
