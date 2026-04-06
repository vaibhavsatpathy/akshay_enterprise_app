from sql import logger
from sql.crud.box_types_crud import CRUDBoxType

logging = logger(__name__)


class BoxTypeController:
    def __init__(self):
        self.CRUDBoxType = CRUDBoxType()

    def create_box_type_controller(self, request):
        """[Create a BoxType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BoxType Data]
        """
        try:
            logging.info("executing create_box_type_controller function")
            create_box_type_request = request.dict(exclude_none=True)
            self.CRUDBoxType.create(**create_box_type_request)
            return create_box_type_request
        except Exception as error:
            logging.error(f"Error in create_box_type_controller function: {error}")
            raise error

    def update_box_type_controller(self, request):
        """[Update a BoxType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BoxType Data]
        """
        try:
            logging.info("executing update_box_type_controller function")
            update_box_type_request = request.dict(exclude_none=True)
            self.CRUDBoxType.update(**update_box_type_request)
            return update_box_type_request
        except Exception as error:
            logging.error(f"Error in update_box_type_controller function: {error}")
            raise error

    def get_all_box_type_controller(self):
        """[Get All BoxType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all BoxType Records]
        """
        try:
            logging.info("executing get_all_box_type_controller function")
            return self.CRUDBoxType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_box_type_controller function: {error}")
            raise error

    def get_box_type_controller(self, box_type_id: int):
        """[Get a BoxType record Controller]

        Args:
            box_type_id (int): [Unique Identifier for a BoxType]

        Raises:
            error: [Error]

        Returns:
            [type]: [BoxType Record]
        """
        try:
            logging.info("executing get_box_type_controller function")
            return self.CRUDBoxType.read(box_type_id=box_type_id)
        except Exception as error:
            logging.error(f"Error in get_box_type_controller function: {error}")
            raise error

    def delete_box_type_controller(self, box_type_id: int):
        """[Controller to delete a BoxType]

        Args:
            box_type_id (int): [Unique Identifier for a BoxType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted BoxType details]
        """
        try:
            logging.info("executing delete_box_type_controller function")
            return self.CRUDBoxType.delete(box_type_id=box_type_id)
        except Exception as error:
            logging.error(f"Error in delete_box_type_controller function: {error}")
            raise error
