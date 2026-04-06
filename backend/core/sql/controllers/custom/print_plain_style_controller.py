from sql import logger
from sql.crud.print_plain_style_crud import CRUDPrintPlainStyle

logging = logger(__name__)


class PrintPlainStyleController:
    def __init__(self):
        self.CRUDPrintPlainStyle = CRUDPrintPlainStyle()

    def create_print_plain_style_controller(self, request):
        """[Create a PrintPlainStyle record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintPlainStyle Data]
        """
        try:
            logging.info("executing create_print_plain_style_controller function")
            create_print_plain_style_request = request.dict(exclude_none=True)
            self.CRUDPrintPlainStyle.create(**create_print_plain_style_request)
            return create_print_plain_style_request
        except Exception as error:
            logging.error(f"Error in create_print_plain_style_controller function: {error}")
            raise error

    def update_print_plain_style_controller(self, request):
        """[Update a PrintPlainStyle record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintPlainStyle Data]
        """
        try:
            logging.info("executing update_print_plain_style_controller function")
            update_print_plain_style_request = request.dict(exclude_none=True)
            self.CRUDPrintPlainStyle.update(**update_print_plain_style_request)
            return update_print_plain_style_request
        except Exception as error:
            logging.error(f"Error in update_print_plain_style_controller function: {error}")
            raise error

    def get_all_print_plain_style_controller(self):
        """[Get All PrintPlainStyle records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all PrintPlainStyle Records]
        """
        try:
            logging.info("executing get_all_print_plain_style_controller function")
            return self.CRUDPrintPlainStyle.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_print_plain_style_controller function: {error}")
            raise error

    def get_print_plain_style_controller(self, print_plain_style_id: int):
        """[Get a PrintPlainStyle record Controller]

        Args:
            print_plain_style_id (int): [Unique Identifier for a PrintPlainStyle]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintPlainStyle Record]
        """
        try:
            logging.info("executing get_print_plain_style_controller function")
            return self.CRUDPrintPlainStyle.read(print_plain_style_id=print_plain_style_id)
        except Exception as error:
            logging.error(f"Error in get_print_plain_style_controller function: {error}")
            raise error

    def delete_print_plain_style_controller(self, print_plain_style_id: int):
        """[Controller to delete a PrintPlainStyle]

        Args:
            print_plain_style_id (int): [Unique Identifier for a PrintPlainStyle]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted PrintPlainStyle details]
        """
        try:
            logging.info("executing delete_print_plain_style_controller function")
            return self.CRUDPrintPlainStyle.delete(print_plain_style_id=print_plain_style_id)
        except Exception as error:
            logging.error(f"Error in delete_print_plain_style_controller function: {error}")
            raise error
