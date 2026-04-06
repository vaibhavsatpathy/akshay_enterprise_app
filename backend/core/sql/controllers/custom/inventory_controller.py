from sql import logger
from sql.crud.inventory_crud import CRUDInventory

logging = logger(__name__)


class InventoryController:
    def __init__(self):
        self.CRUDInventory = CRUDInventory()

    def create_inventory_controller(self, request):
        """[Create a Inventory record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Inventory Data]
        """
        try:
            logging.info("executing create_inventory_controller function")
            create_inventory_request = request.dict(exclude_none=True)
            crud_response = self.CRUDInventory.create(**create_inventory_request)
            return crud_response
        except Exception as error:
            logging.error(f"Error in create_inventory_controller function: {error}")
            raise error

    def update_inventory_controller(self, request):
        """[Update a Inventory record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Inventory Data]
        """
        try:
            logging.info("executing update_inventory_controller function")
            update_inventory_request = request.dict(exclude_none=True)
            self.CRUDInventory.update(**update_inventory_request)
            return update_inventory_request
        except Exception as error:
            logging.error(f"Error in update_inventory_controller function: {error}")
            raise error

    def get_all_inventory_controller(self):
        """[Get All Inventory records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Inventory Records]
        """
        try:
            logging.info("executing get_all_inventory_controller function")
            return self.CRUDInventory.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_inventory_controller function: {error}")
            raise error

    def get_inventory_controller(self, inventory_id: int):
        """[Get a Inventory record Controller]

        Args:
            inventory_id (int): [Unique Identifier for a Inventory]

        Raises:
            error: [Error]

        Returns:
            [type]: [Inventory Record]
        """
        try:
            logging.info("executing get_inventory_controller function")
            return self.CRUDInventory.read(inventory_id=inventory_id)
        except Exception as error:
            logging.error(f"Error in get_inventory_controller function: {error}")
            raise error

    def delete_inventory_controller(self, inventory_id: int):
        """[Controller to delete a Inventory]

        Args:
            inventory_id (int): [Unique Identifier for a Inventory]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Inventory details]
        """
        try:
            logging.info("executing delete_inventory_controller function")
            return self.CRUDInventory.delete(inventory_id=inventory_id)
        except Exception as error:
            logging.error(f"Error in delete_inventory_controller function: {error}")
            raise error
