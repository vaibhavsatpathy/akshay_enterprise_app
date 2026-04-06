from sql import logger
from sql.crud.block_print_colors_crud import CRUDBlockPrintColor

logging = logger(__name__)


class BlockPrintColorController:
    def __init__(self):
        self.CRUDBlockPrintColor = CRUDBlockPrintColor()

    def create_block_print_color_controller(self, request):
        """[Create a BlockPrintColor record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BlockPrintColor Data]
        """
        try:
            logging.info("executing create_block_print_color_controller function")
            create_block_print_color_request = request.dict(exclude_none=True)
            self.CRUDBlockPrintColor.create(**create_block_print_color_request)
            return create_block_print_color_request
        except Exception as error:
            logging.error(f"Error in create_block_print_color_controller function: {error}")
            raise error

    def update_block_print_color_controller(self, request):
        """[Update a BlockPrintColor record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BlockPrintColor Data]
        """
        try:
            logging.info("executing update_block_print_color_controller function")
            update_block_print_color_request = request.dict(exclude_none=True)
            self.CRUDBlockPrintColor.update(**update_block_print_color_request)
            return update_block_print_color_request
        except Exception as error:
            logging.error(f"Error in update_block_print_color_controller function: {error}")
            raise error

    def get_all_block_print_color_controller(self):
        """[Get All BlockPrintColor records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all BlockPrintColor Records]
        """
        try:
            logging.info("executing get_all_block_print_color_controller function")
            return self.CRUDBlockPrintColor.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_block_print_color_controller function: {error}")
            raise error

    def get_block_print_color_controller(self, color_id: int):
        """[Get a BlockPrintColor record Controller]

        Args:
            color_id (int): [Unique Identifier for a BlockPrintColor]

        Raises:
            error: [Error]

        Returns:
            [type]: [BlockPrintColor Record]
        """
        try:
            logging.info("executing get_block_print_color_controller function")
            return self.CRUDBlockPrintColor.read(color_id=color_id)
        except Exception as error:
            logging.error(f"Error in get_block_print_color_controller function: {error}")
            raise error

    def delete_block_print_color_controller(self, color_id: int):
        """[Controller to delete a BlockPrintColor]

        Args:
            color_id (int): [Unique Identifier for a BlockPrintColor]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted BlockPrintColor details]
        """
        try:
            logging.info("executing delete_block_print_color_controller function")
            return self.CRUDBlockPrintColor.delete(color_id=color_id)
        except Exception as error:
            logging.error(f"Error in delete_block_print_color_controller function: {error}")
            raise error
