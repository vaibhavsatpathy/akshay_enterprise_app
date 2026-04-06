from sql import session, logger
from sql.orm_models.dispatch_table import DispatchTable

logging = logger(__name__)


class CRUDDispatchTable:
    def create(self, **kwargs):
        try:
            logging.info("CRUDDispatchTable create request")
            dispatch = DispatchTable(**kwargs)
            with session() as transaction_session:
                transaction_session.add(dispatch)
                transaction_session.commit()
                transaction_session.refresh(dispatch)
            return dispatch.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDDispatchTable create function : {error}")
            raise error

    def read(self, id: int):
        try:
            logging.info("CRUDDispatchTable read request")
            with session() as transaction_session:
                obj: DispatchTable = (
                    transaction_session.query(DispatchTable)
                    .filter(DispatchTable.id == id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDDispatchTable read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDDispatchTable read_all request")
            with session() as transaction_session:
                obj: DispatchTable = transaction_session.query(DispatchTable).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDDispatchTable read_all function : {error}")
            raise error

    def read_by_order(self, order_id: int):
        try:
            logging.info("CRUDDispatchTable read_by_order request")
            with session() as transaction_session:
                obj: DispatchTable = (
                    transaction_session.query(DispatchTable)
                    .filter(DispatchTable.order_id == order_id)
                    .all()
                )
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(
                f"Error in CRUDDispatchTable read_by_order function : {error}"
            )
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDDispatchTable update request")
            with session() as transaction_session:
                transaction_session.query(DispatchTable).filter(
                    DispatchTable.id == kwargs.get("id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDDispatchTable update function : {error}")
            raise error

    def delete(self, id: int):
        try:
            logging.info("CRUDDispatchTable delete request")
            with session() as transaction_session:
                obj: DispatchTable = (
                    transaction_session.query(DispatchTable)
                    .filter(DispatchTable.id == id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDDispatchTable delete function : {error}")
            raise error
