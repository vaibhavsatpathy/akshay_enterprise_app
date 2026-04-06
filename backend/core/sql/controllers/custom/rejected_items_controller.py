from sql import logger
from sql.crud.rejected_items_crud import CRUDRejectedItem

logging = logger(__name__)


class RejectedItemController:
    def __init__(self):
        self.CRUDRejectedItem = CRUDRejectedItem()

    def create_rejected_item_controller(self, request):
        """[Create a RejectedItem record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [RejectedItem Data]
        """
        try:
            logging.info("executing create_rejected_item_controller function")
            create_rejected_item_request = request.dict(exclude_none=True)
            self.CRUDRejectedItem.create(**create_rejected_item_request)
            return create_rejected_item_request
        except Exception as error:
            logging.error(f"Error in create_rejected_item_controller function: {error}")
            raise error

    def update_rejected_item_controller(self, request):
        """[Update a RejectedItem record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [RejectedItem Data]
        """
        try:
            logging.info("executing update_rejected_item_controller function")
            update_rejected_item_request = request.dict(exclude_none=True)
            self.CRUDRejectedItem.update(**update_rejected_item_request)
            return update_rejected_item_request
        except Exception as error:
            logging.error(f"Error in update_rejected_item_controller function: {error}")
            raise error

    def get_all_rejected_item_controller(self):
        """[Get All RejectedItem records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all RejectedItem Records]
        """
        try:
            logging.info("executing get_all_rejected_item_controller function")
            return self.CRUDRejectedItem.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_rejected_item_controller function: {error}")
            raise error

    def get_rejected_item_controller(self, rejected_id: int):
        """[Get a RejectedItem record Controller]

        Args:
            rejected_id (int): [Unique Identifier for a RejectedItem]

        Raises:
            error: [Error]

        Returns:
            [type]: [RejectedItem Record]
        """
        try:
            logging.info("executing get_rejected_item_controller function")
            return self.CRUDRejectedItem.read(rejected_id=rejected_id)
        except Exception as error:
            logging.error(f"Error in get_rejected_item_controller function: {error}")
            raise error

    def delete_rejected_item_controller(self, rejected_id: int):
        """[Controller to delete a RejectedItem]

        Args:
            rejected_id (int): [Unique Identifier for a RejectedItem]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted RejectedItem details]
        """
        try:
            logging.info("executing delete_rejected_item_controller function")
            return self.CRUDRejectedItem.delete(rejected_id=rejected_id)
        except Exception as error:
            logging.error(f"Error in delete_rejected_item_controller function: {error}")
            raise error
