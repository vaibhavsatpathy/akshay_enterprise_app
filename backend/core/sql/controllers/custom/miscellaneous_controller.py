from sql import logger
from sql.crud.miscellaneous_crud import CRUDMiscellaneous

logging = logger(__name__)


class MiscellaneousController:
    def __init__(self):
        self.CRUDMiscellaneous = CRUDMiscellaneous()

    def create_miscellaneous_controller(self, request):
        """[Create a Miscellaneous record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Miscellaneous Data]
        """
        try:
            logging.info("executing create_miscellaneous_controller function")
            create_miscellaneous_request = request.dict(exclude_none=True)
            self.CRUDMiscellaneous.create(**create_miscellaneous_request)
            return create_miscellaneous_request
        except Exception as error:
            logging.error(f"Error in create_miscellaneous_controller function: {error}")
            raise error

    def update_miscellaneous_controller(self, request):
        """[Update a Miscellaneous record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Miscellaneous Data]
        """
        try:
            logging.info("executing update_miscellaneous_controller function")
            update_miscellaneous_request = request.dict(exclude_none=True)
            self.CRUDMiscellaneous.update(**update_miscellaneous_request)
            return update_miscellaneous_request
        except Exception as error:
            logging.error(f"Error in update_miscellaneous_controller function: {error}")
            raise error

    def get_all_miscellaneous_controller(self):
        """[Get All Miscellaneous records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Miscellaneous Records]
        """
        try:
            logging.info("executing get_all_miscellaneous_controller function")
            return self.CRUDMiscellaneous.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_miscellaneous_controller function: {error}")
            raise error

    def get_miscellaneous_controller(self, misc_id: int):
        """[Get a Miscellaneous record Controller]

        Args:
            misc_id (int): [Unique Identifier for a Miscellaneous]

        Raises:
            error: [Error]

        Returns:
            [type]: [Miscellaneous Record]
        """
        try:
            logging.info("executing get_miscellaneous_controller function")
            return self.CRUDMiscellaneous.read(misc_id=misc_id)
        except Exception as error:
            logging.error(f"Error in get_miscellaneous_controller function: {error}")
            raise error

    def delete_miscellaneous_controller(self, misc_id: int):
        """[Controller to delete a Miscellaneous]

        Args:
            misc_id (int): [Unique Identifier for a Miscellaneous]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Miscellaneous details]
        """
        try:
            logging.info("executing delete_miscellaneous_controller function")
            return self.CRUDMiscellaneous.delete(misc_id=misc_id)
        except Exception as error:
            logging.error(f"Error in delete_miscellaneous_controller function: {error}")
            raise error
