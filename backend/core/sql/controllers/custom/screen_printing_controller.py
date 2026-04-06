from sql import logger
from sql.crud.screen_printing_crud import CRUDScreenPrinting

logging = logger(__name__)


class ScreenPrintingController:
    def __init__(self):
        self.CRUDScreenPrinting = CRUDScreenPrinting()

    def create_screen_printing_controller(self, request):
        """[Create a ScreenPrinting record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ScreenPrinting Data]
        """
        try:
            logging.info("executing create_screen_printing_controller function")
            create_screen_printing_request = request.dict(exclude_none=True)
            self.CRUDScreenPrinting.create(**create_screen_printing_request)
            return create_screen_printing_request
        except Exception as error:
            logging.error(f"Error in create_screen_printing_controller function: {error}")
            raise error

    def update_screen_printing_controller(self, request):
        """[Update a ScreenPrinting record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ScreenPrinting Data]
        """
        try:
            logging.info("executing update_screen_printing_controller function")
            update_screen_printing_request = request.dict(exclude_none=True)
            self.CRUDScreenPrinting.update(**update_screen_printing_request)
            return update_screen_printing_request
        except Exception as error:
            logging.error(f"Error in update_screen_printing_controller function: {error}")
            raise error

    def get_all_screen_printing_controller(self):
        """[Get All ScreenPrinting records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ScreenPrinting Records]
        """
        try:
            logging.info("executing get_all_screen_printing_controller function")
            return self.CRUDScreenPrinting.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_screen_printing_controller function: {error}")
            raise error

    def get_screen_printing_controller(self, print_id: int):
        """[Get a ScreenPrinting record Controller]

        Args:
            print_id (int): [Unique Identifier for a ScreenPrinting]

        Raises:
            error: [Error]

        Returns:
            [type]: [ScreenPrinting Record]
        """
        try:
            logging.info("executing get_screen_printing_controller function")
            return self.CRUDScreenPrinting.read(print_id=print_id)
        except Exception as error:
            logging.error(f"Error in get_screen_printing_controller function: {error}")
            raise error

    def delete_screen_printing_controller(self, print_id: int):
        """[Controller to delete a ScreenPrinting]

        Args:
            print_id (int): [Unique Identifier for a ScreenPrinting]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ScreenPrinting details]
        """
        try:
            logging.info("executing delete_screen_printing_controller function")
            return self.CRUDScreenPrinting.delete(print_id=print_id)
        except Exception as error:
            logging.error(f"Error in delete_screen_printing_controller function: {error}")
            raise error
