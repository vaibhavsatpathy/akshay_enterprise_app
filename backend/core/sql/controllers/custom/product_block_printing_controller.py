from sql import logger
from sql.crud.product_block_printing_crud import CRUDProductBlockPrinting

logging = logger(__name__)


class ProductBlockPrintingController:
    def __init__(self):
        self.CRUDProductBlockPrinting = CRUDProductBlockPrinting()

    def create_product_block_printing_controller(self, request):
        """[Create a ProductBlockPrinting record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductBlockPrinting Data]
        """
        try:
            logging.info("executing create_product_block_printing_controller function")
            create_product_block_printing_request = request.dict(exclude_none=True)
            self.CRUDProductBlockPrinting.create(**create_product_block_printing_request)
            return create_product_block_printing_request
        except Exception as error:
            logging.error(f"Error in create_product_block_printing_controller function: {error}")
            raise error

    def update_product_block_printing_controller(self, request):
        """[Update a ProductBlockPrinting record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductBlockPrinting Data]
        """
        try:
            logging.info("executing update_product_block_printing_controller function")
            update_product_block_printing_request = request.dict(exclude_none=True)
            self.CRUDProductBlockPrinting.update(**update_product_block_printing_request)
            return update_product_block_printing_request
        except Exception as error:
            logging.error(f"Error in update_product_block_printing_controller function: {error}")
            raise error

    def get_all_product_block_printing_controller(self):
        """[Get All ProductBlockPrinting records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductBlockPrinting Records]
        """
        try:
            logging.info("executing get_all_product_block_printing_controller function")
            return self.CRUDProductBlockPrinting.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_block_printing_controller function: {error}")
            raise error

    def get_product_block_printing_controller(self, print_id: int):
        """[Get a ProductBlockPrinting record Controller]

        Args:
            print_id (int): [Unique Identifier for a ProductBlockPrinting]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductBlockPrinting Record]
        """
        try:
            logging.info("executing get_product_block_printing_controller function")
            return self.CRUDProductBlockPrinting.read(print_id=print_id)
        except Exception as error:
            logging.error(f"Error in get_product_block_printing_controller function: {error}")
            raise error

    def delete_product_block_printing_controller(self, print_id: int):
        """[Controller to delete a ProductBlockPrinting]

        Args:
            print_id (int): [Unique Identifier for a ProductBlockPrinting]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductBlockPrinting details]
        """
        try:
            logging.info("executing delete_product_block_printing_controller function")
            return self.CRUDProductBlockPrinting.delete(print_id=print_id)
        except Exception as error:
            logging.error(f"Error in delete_product_block_printing_controller function: {error}")
            raise error
