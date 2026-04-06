from sql import logger
from sql.crud.printing_paper_block_screen_crud import CRUDPrintingPaperBlockScreen

logging = logger(__name__)


class PrintingPaperBlockScreenController:
    def __init__(self):
        self.CRUDPrintingPaperBlockScreen = CRUDPrintingPaperBlockScreen()

    def create_printing_paper_block_screen_controller(self, request):
        """[Create a PrintingPaperBlockScreen record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintingPaperBlockScreen Data]
        """
        try:
            logging.info("executing create_printing_paper_block_screen_controller function")
            create_printing_paper_block_screen_request = request.dict(exclude_none=True)
            self.CRUDPrintingPaperBlockScreen.create(**create_printing_paper_block_screen_request)
            return create_printing_paper_block_screen_request
        except Exception as error:
            logging.error(f"Error in create_printing_paper_block_screen_controller function: {error}")
            raise error

    def update_printing_paper_block_screen_controller(self, request):
        """[Update a PrintingPaperBlockScreen record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintingPaperBlockScreen Data]
        """
        try:
            logging.info("executing update_printing_paper_block_screen_controller function")
            update_printing_paper_block_screen_request = request.dict(exclude_none=True)
            self.CRUDPrintingPaperBlockScreen.update(**update_printing_paper_block_screen_request)
            return update_printing_paper_block_screen_request
        except Exception as error:
            logging.error(f"Error in update_printing_paper_block_screen_controller function: {error}")
            raise error

    def get_all_printing_paper_block_screen_controller(self):
        """[Get All PrintingPaperBlockScreen records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all PrintingPaperBlockScreen Records]
        """
        try:
            logging.info("executing get_all_printing_paper_block_screen_controller function")
            return self.CRUDPrintingPaperBlockScreen.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_printing_paper_block_screen_controller function: {error}")
            raise error

    def get_printing_paper_block_screen_controller(self, print_id: int):
        """[Get a PrintingPaperBlockScreen record Controller]

        Args:
            print_id (int): [Unique Identifier for a PrintingPaperBlockScreen]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintingPaperBlockScreen Record]
        """
        try:
            logging.info("executing get_printing_paper_block_screen_controller function")
            return self.CRUDPrintingPaperBlockScreen.read(print_id=print_id)
        except Exception as error:
            logging.error(f"Error in get_printing_paper_block_screen_controller function: {error}")
            raise error

    def delete_printing_paper_block_screen_controller(self, print_id: int):
        """[Controller to delete a PrintingPaperBlockScreen]

        Args:
            print_id (int): [Unique Identifier for a PrintingPaperBlockScreen]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted PrintingPaperBlockScreen details]
        """
        try:
            logging.info("executing delete_printing_paper_block_screen_controller function")
            return self.CRUDPrintingPaperBlockScreen.delete(print_id=print_id)
        except Exception as error:
            logging.error(f"Error in delete_printing_paper_block_screen_controller function: {error}")
            raise error
