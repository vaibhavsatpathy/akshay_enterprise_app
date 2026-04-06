from sql import logger
from sql.crud.product_flutes_crud import CRUDProductFlute

logging = logger(__name__)


class ProductFluteController:
    def __init__(self):
        self.CRUDProductFlute = CRUDProductFlute()

    def create_product_flute_controller(self, request):
        """[Create a ProductFlute record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductFlute Data]
        """
        try:
            logging.info("executing create_product_flute_controller function")
            create_product_flute_request = request.dict(exclude_none=True)
            self.CRUDProductFlute.create(**create_product_flute_request)
            return create_product_flute_request
        except Exception as error:
            logging.error(f"Error in create_product_flute_controller function: {error}")
            raise error

    def update_product_flute_controller(self, request):
        """[Update a ProductFlute record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductFlute Data]
        """
        try:
            logging.info("executing update_product_flute_controller function")
            update_product_flute_request = request.dict(exclude_none=True)
            self.CRUDProductFlute.update(**update_product_flute_request)
            return update_product_flute_request
        except Exception as error:
            logging.error(f"Error in update_product_flute_controller function: {error}")
            raise error

    def get_all_product_flute_controller(self):
        """[Get All ProductFlute records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductFlute Records]
        """
        try:
            logging.info("executing get_all_product_flute_controller function")
            return self.CRUDProductFlute.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_flute_controller function: {error}")
            raise error

    def get_product_flute_controller(self, flute_id: int):
        """[Get a ProductFlute record Controller]

        Args:
            flute_id (int): [Unique Identifier for a ProductFlute]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductFlute Record]
        """
        try:
            logging.info("executing get_product_flute_controller function")
            return self.CRUDProductFlute.read(flute_id=flute_id)
        except Exception as error:
            logging.error(f"Error in get_product_flute_controller function: {error}")
            raise error

    def delete_product_flute_controller(self, flute_id: int):
        """[Controller to delete a ProductFlute]

        Args:
            flute_id (int): [Unique Identifier for a ProductFlute]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductFlute details]
        """
        try:
            logging.info("executing delete_product_flute_controller function")
            return self.CRUDProductFlute.delete(flute_id=flute_id)
        except Exception as error:
            logging.error(f"Error in delete_product_flute_controller function: {error}")
            raise error
