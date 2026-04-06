from sql import logger
from sql.crud.products_crud import CRUDProduct

logging = logger(__name__)


class ProductController:
    def __init__(self):
        self.CRUDProduct = CRUDProduct()

    def create_product_controller(self, request):
        """[Create a Product record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Product Data]
        """
        try:
            logging.info("executing create_product_controller function")
            create_product_request = request.dict(exclude_none=True)
            self.CRUDProduct.create(**create_product_request)
            return create_product_request
        except Exception as error:
            logging.error(f"Error in create_product_controller function: {error}")
            raise error

    def update_product_controller(self, request):
        """[Update a Product record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Product Data]
        """
        try:
            logging.info("executing update_product_controller function")
            update_product_request = request.dict(exclude_none=True)
            self.CRUDProduct.update(**update_product_request)
            return update_product_request
        except Exception as error:
            logging.error(f"Error in update_product_controller function: {error}")
            raise error

    def get_all_product_controller(self):
        """[Get All Product records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Product Records]
        """
        try:
            logging.info("executing get_all_product_controller function")
            return self.CRUDProduct.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_controller function: {error}")
            raise error

    def get_product_controller(self, product_id: int):
        """[Get a Product record Controller]

        Args:
            product_id (int): [Unique Identifier for a Product]

        Raises:
            error: [Error]

        Returns:
            [type]: [Product Record]
        """
        try:
            logging.info("executing get_product_controller function")
            return self.CRUDProduct.read(product_id=product_id)
        except Exception as error:
            logging.error(f"Error in get_product_controller function: {error}")
            raise error

    def delete_product_controller(self, product_id: int):
        """[Controller to delete a Product]

        Args:
            product_id (int): [Unique Identifier for a Product]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Product details]
        """
        try:
            logging.info("executing delete_product_controller function")
            return self.CRUDProduct.delete(product_id=product_id)
        except Exception as error:
            logging.error(f"Error in delete_product_controller function: {error}")
            raise error
