from sql import logger
from sql.crud.rejected_item_types_crud import CRUDRejectedItemType

logging = logger(__name__)


class RejectedItemTypeController:
    def __init__(self):
        self.CRUDRejectedItemType = CRUDRejectedItemType()

    def create_rejected_item_type_controller(self, request):
        """[Create a RejectedItemType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [RejectedItemType Data]
        """
        try:
            logging.info("executing create_rejected_item_type_controller function")
            create_rejected_item_type_request = request.dict(exclude_none=True)
            self.CRUDRejectedItemType.create(**create_rejected_item_type_request)
            return create_rejected_item_type_request
        except Exception as error:
            logging.error(f"Error in create_rejected_item_type_controller function: {error}")
            raise error

    def update_rejected_item_type_controller(self, request):
        """[Update a RejectedItemType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [RejectedItemType Data]
        """
        try:
            logging.info("executing update_rejected_item_type_controller function")
            update_rejected_item_type_request = request.dict(exclude_none=True)
            self.CRUDRejectedItemType.update(**update_rejected_item_type_request)
            return update_rejected_item_type_request
        except Exception as error:
            logging.error(f"Error in update_rejected_item_type_controller function: {error}")
            raise error

    def get_all_rejected_item_type_controller(self):
        """[Get All RejectedItemType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all RejectedItemType Records]
        """
        try:
            logging.info("executing get_all_rejected_item_type_controller function")
            return self.CRUDRejectedItemType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_rejected_item_type_controller function: {error}")
            raise error

    def get_rejected_item_type_controller(self, rejected_item_type_id: int):
        """[Get a RejectedItemType record Controller]

        Args:
            rejected_item_type_id (int): [Unique Identifier for a RejectedItemType]

        Raises:
            error: [Error]

        Returns:
            [type]: [RejectedItemType Record]
        """
        try:
            logging.info("executing get_rejected_item_type_controller function")
            return self.CRUDRejectedItemType.read(rejected_item_type_id=rejected_item_type_id)
        except Exception as error:
            logging.error(f"Error in get_rejected_item_type_controller function: {error}")
            raise error

    def delete_rejected_item_type_controller(self, rejected_item_type_id: int):
        """[Controller to delete a RejectedItemType]

        Args:
            rejected_item_type_id (int): [Unique Identifier for a RejectedItemType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted RejectedItemType details]
        """
        try:
            logging.info("executing delete_rejected_item_type_controller function")
            return self.CRUDRejectedItemType.delete(rejected_item_type_id=rejected_item_type_id)
        except Exception as error:
            logging.error(f"Error in delete_rejected_item_type_controller function: {error}")
            raise error
