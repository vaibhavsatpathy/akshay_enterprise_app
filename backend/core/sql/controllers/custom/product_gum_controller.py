from sql import logger
from sql.crud.product_gum_crud import CRUDProductGum

logging = logger(__name__)


class ProductGumController:
    def __init__(self):
        self.CRUDProductGum = CRUDProductGum()

    def create_product_gum_controller(self, request):
        """[Create a ProductGum record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductGum Data]
        """
        try:
            logging.info("executing create_product_gum_controller function")
            create_product_gum_request = request.dict(exclude_none=True)
            self.CRUDProductGum.create(**create_product_gum_request)
            return create_product_gum_request
        except Exception as error:
            logging.error(f"Error in create_product_gum_controller function: {error}")
            raise error

    def update_product_gum_controller(self, request):
        """[Update a ProductGum record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductGum Data]
        """
        try:
            logging.info("executing update_product_gum_controller function")
            update_product_gum_request = request.dict(exclude_none=True)
            self.CRUDProductGum.update(**update_product_gum_request)
            return update_product_gum_request
        except Exception as error:
            logging.error(f"Error in update_product_gum_controller function: {error}")
            raise error

    def get_all_product_gum_controller(self):
        """[Get All ProductGum records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductGum Records]
        """
        try:
            logging.info("executing get_all_product_gum_controller function")
            return self.CRUDProductGum.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_gum_controller function: {error}")
            raise error

    def get_product_gum_controller(self, gum_id: int):
        """[Get a ProductGum record Controller]

        Args:
            gum_id (int): [Unique Identifier for a ProductGum]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductGum Record]
        """
        try:
            logging.info("executing get_product_gum_controller function")
            return self.CRUDProductGum.read(gum_id=gum_id)
        except Exception as error:
            logging.error(f"Error in get_product_gum_controller function: {error}")
            raise error

    def delete_product_gum_controller(self, gum_id: int):
        """[Controller to delete a ProductGum]

        Args:
            gum_id (int): [Unique Identifier for a ProductGum]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductGum details]
        """
        try:
            logging.info("executing delete_product_gum_controller function")
            return self.CRUDProductGum.delete(gum_id=gum_id)
        except Exception as error:
            logging.error(f"Error in delete_product_gum_controller function: {error}")
            raise error
