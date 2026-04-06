from sql import logger
from sql.crud.dispatch_table_crud import CRUDDispatchTable

logging = logger(__name__)


class DispatchTableController:
    def __init__(self):
        self.CRUDDispatchTable = CRUDDispatchTable()

    def create_dispatch_controller(self, request):
        """[Create a DispatchTable record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [DispatchTable Data]
        """
        try:
            logging.info("executing create_dispatch_controller function")
            create_dispatch_request = request.dict(exclude_none=True)
            self.CRUDDispatchTable.create(**create_dispatch_request)
            return create_dispatch_request
        except Exception as error:
            logging.error(f"Error in create_dispatch_controller function: {error}")
            raise error

    def update_dispatch_controller(self, request):
        """[Update a DispatchTable record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [DispatchTable Data]
        """
        try:
            logging.info("executing update_dispatch_controller function")
            update_dispatch_request = request.dict(exclude_none=True)
            self.CRUDDispatchTable.update(**update_dispatch_request)
            return update_dispatch_request
        except Exception as error:
            logging.error(f"Error in update_dispatch_controller function: {error}")
            raise error

    def get_all_dispatch_controller(self):
        """[Get All DispatchTable records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all DispatchTable Records]
        """
        try:
            logging.info("executing get_all_dispatch_controller function")
            return self.CRUDDispatchTable.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_dispatch_controller function: {error}")
            raise error

    def get_dispatch_controller(self, id: int):
        """[Get a DispatchTable record Controller]

        Args:
            id (int): [Unique Identifier for a DispatchTable]

        Raises:
            error: [Error]

        Returns:
            [type]: [DispatchTable Record]
        """
        try:
            logging.info("executing get_dispatch_controller function")
            return self.CRUDDispatchTable.read(id=id)
        except Exception as error:
            logging.error(f"Error in get_dispatch_controller function: {error}")
            raise error

    def delete_dispatch_controller(self, id: int):
        """[Controller to delete a DispatchTable]

        Args:
            id (int): [Unique Identifier for a DispatchTable]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted DispatchTable details]
        """
        try:
            logging.info("executing delete_dispatch_controller function")
            return self.CRUDDispatchTable.delete(id=id)
        except Exception as error:
            logging.error(f"Error in delete_dispatch_controller function: {error}")
            raise error
