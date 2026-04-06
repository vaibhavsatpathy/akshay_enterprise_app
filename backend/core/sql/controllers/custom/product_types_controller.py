from sql import logger
from sql.crud.product_types_crud import CRUDProductType

logging = logger(__name__)


class ProductTypeController:
    def __init__(self):
        self.CRUDProductType = CRUDProductType()

    def create_product_type_controller(self, request):
        """[Create a ProductType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductType Data]
        """
        try:
            logging.info("executing create_product_type_controller function")
            create_product_type_request = request.dict(exclude_none=True)
            self.CRUDProductType.create(**create_product_type_request)
            return create_product_type_request
        except Exception as error:
            logging.error(f"Error in create_product_type_controller function: {error}")
            raise error

    def update_product_type_controller(self, request):
        """[Update a ProductType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductType Data]
        """
        try:
            logging.info("executing update_product_type_controller function")
            update_product_type_request = request.dict(exclude_none=True)
            self.CRUDProductType.update(**update_product_type_request)
            return update_product_type_request
        except Exception as error:
            logging.error(f"Error in update_product_type_controller function: {error}")
            raise error

    def get_all_product_type_controller(self):
        """[Get All ProductType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductType Records]
        """
        try:
            logging.info("executing get_all_product_type_controller function")
            return self.CRUDProductType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_type_controller function: {error}")
            raise error

    def get_product_type_controller(self, product_type_id: int):
        """[Get a ProductType record Controller]

        Args:
            product_type_id (int): [Unique Identifier for a ProductType]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductType Record]
        """
        try:
            logging.info("executing get_product_type_controller function")
            return self.CRUDProductType.read(product_type_id=product_type_id)
        except Exception as error:
            logging.error(f"Error in get_product_type_controller function: {error}")
            raise error

    def delete_product_type_controller(self, product_type_id: int):
        """[Controller to delete a ProductType]

        Args:
            product_type_id (int): [Unique Identifier for a ProductType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductType details]
        """
        try:
            logging.info("executing delete_product_type_controller function")
            return self.CRUDProductType.delete(product_type_id=product_type_id)
        except Exception as error:
            logging.error(f"Error in delete_product_type_controller function: {error}")
            raise error
