from sql import logger
from sql.crud.printing_paper_offset_crud import CRUDPrintingPaperOffset

logging = logger(__name__)


class PrintingPaperOffsetController:
    def __init__(self):
        self.CRUDPrintingPaperOffset = CRUDPrintingPaperOffset()

    def create_printing_paper_offset_controller(self, request):
        """[Create a PrintingPaperOffset record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintingPaperOffset Data]
        """
        try:
            logging.info("executing create_printing_paper_offset_controller function")
            create_printing_paper_offset_request = request.dict(exclude_none=True)
            self.CRUDPrintingPaperOffset.create(**create_printing_paper_offset_request)
            return create_printing_paper_offset_request
        except Exception as error:
            logging.error(f"Error in create_printing_paper_offset_controller function: {error}")
            raise error

    def update_printing_paper_offset_controller(self, request):
        """[Update a PrintingPaperOffset record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintingPaperOffset Data]
        """
        try:
            logging.info("executing update_printing_paper_offset_controller function")
            update_printing_paper_offset_request = request.dict(exclude_none=True)
            self.CRUDPrintingPaperOffset.update(**update_printing_paper_offset_request)
            return update_printing_paper_offset_request
        except Exception as error:
            logging.error(f"Error in update_printing_paper_offset_controller function: {error}")
            raise error

    def get_all_printing_paper_offset_controller(self):
        """[Get All PrintingPaperOffset records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all PrintingPaperOffset Records]
        """
        try:
            logging.info("executing get_all_printing_paper_offset_controller function")
            return self.CRUDPrintingPaperOffset.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_printing_paper_offset_controller function: {error}")
            raise error

    def get_printing_paper_offset_controller(self, print_id: int):
        """[Get a PrintingPaperOffset record Controller]

        Args:
            print_id (int): [Unique Identifier for a PrintingPaperOffset]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintingPaperOffset Record]
        """
        try:
            logging.info("executing get_printing_paper_offset_controller function")
            return self.CRUDPrintingPaperOffset.read(print_id=print_id)
        except Exception as error:
            logging.error(f"Error in get_printing_paper_offset_controller function: {error}")
            raise error

    def delete_printing_paper_offset_controller(self, print_id: int):
        """[Controller to delete a PrintingPaperOffset]

        Args:
            print_id (int): [Unique Identifier for a PrintingPaperOffset]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted PrintingPaperOffset details]
        """
        try:
            logging.info("executing delete_printing_paper_offset_controller function")
            return self.CRUDPrintingPaperOffset.delete(print_id=print_id)
        except Exception as error:
            logging.error(f"Error in delete_printing_paper_offset_controller function: {error}")
            raise error
