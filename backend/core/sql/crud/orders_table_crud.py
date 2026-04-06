from sql import session, logger
from sql.orm_models.orders_table import OrdersTable

logging = logger(__name__)


class CRUDOrdersTable:
    def create(self, **kwargs):
        try:
            logging.info("CRUDOrdersTable create request")
            order = OrdersTable(**kwargs)
            with session() as transaction_session:
                transaction_session.add(order)
                transaction_session.commit()
                transaction_session.refresh(order)
            return order.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDOrdersTable create function : {error}")
            raise error

    def read(self, order_id: int):
        try:
            logging.info("CRUDOrdersTable read request")
            with session() as transaction_session:
                obj: OrdersTable = (
                    transaction_session.query(OrdersTable)
                    .filter(OrdersTable.order_id == order_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDOrdersTable read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDOrdersTable read_all request")
            with session() as transaction_session:
                obj: OrdersTable = transaction_session.query(OrdersTable).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDOrdersTable read_all function : {error}")
            raise error

    def read_by_party(self, party_id: int):
        try:
            logging.info("CRUDOrdersTable read_by_party request")
            with session() as transaction_session:
                obj: OrdersTable = (
                    transaction_session.query(OrdersTable)
                    .filter(OrdersTable.party_id == party_id)
                    .all()
                )
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDOrdersTable read_by_party function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDOrdersTable update request")
            with session() as transaction_session:
                transaction_session.query(OrdersTable).filter(
                    OrdersTable.order_id == kwargs.get("order_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDOrdersTable update function : {error}")
            raise error

    def delete(self, order_id: int):
        try:
            logging.info("CRUDOrdersTable delete request")
            with session() as transaction_session:
                obj: OrdersTable = (
                    transaction_session.query(OrdersTable)
                    .filter(OrdersTable.order_id == order_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDOrdersTable delete function : {error}")
            raise error
