from sql import logger
from sql.crud.orders_table_crud import CRUDOrdersTable

logging = logger(__name__)


class OrdersTableController:
    def __init__(self):
        self.CRUDOrdersTable = CRUDOrdersTable()

    def create_order_controller(self, request):
        """[Create a OrdersTable record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [OrdersTable Data]
        """
        try:
            logging.info("executing create_order_controller function")
            create_order_request = request.dict(exclude_none=True)
            self.CRUDOrdersTable.create(**create_order_request)
            return create_order_request
        except Exception as error:
            logging.error(f"Error in create_order_controller function: {error}")
            raise error

    def update_order_controller(self, request):
        """[Update a OrdersTable record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [OrdersTable Data]
        """
        try:
            logging.info("executing update_order_controller function")
            update_order_request = request.dict(exclude_none=True)
            self.CRUDOrdersTable.update(**update_order_request)
            return update_order_request
        except Exception as error:
            logging.error(f"Error in update_order_controller function: {error}")
            raise error

    def get_all_order_controller(self):
        """[Get All OrdersTable records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all OrdersTable Records]
        """
        try:
            logging.info("executing get_all_order_controller function")
            return self.CRUDOrdersTable.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_order_controller function: {error}")
            raise error

    def get_order_controller(self, order_id: int):
        """[Get a OrdersTable record Controller]

        Args:
            order_id (int): [Unique Identifier for a OrdersTable]

        Raises:
            error: [Error]

        Returns:
            [type]: [OrdersTable Record]
        """
        try:
            logging.info("executing get_order_controller function")
            return self.CRUDOrdersTable.read(order_id=order_id)
        except Exception as error:
            logging.error(f"Error in get_order_controller function: {error}")
            raise error

    def delete_order_controller(self, order_id: int):
        """[Controller to delete a OrdersTable]

        Args:
            order_id (int): [Unique Identifier for a OrdersTable]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted OrdersTable details]
        """
        try:
            logging.info("executing delete_order_controller function")
            return self.CRUDOrdersTable.delete(order_id=order_id)
        except Exception as error:
            logging.error(f"Error in delete_order_controller function: {error}")
            raise error
