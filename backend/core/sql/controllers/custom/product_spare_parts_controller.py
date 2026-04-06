from sql import logger
from sql.crud.product_spare_parts_crud import CRUDProductSparePart

logging = logger(__name__)


class ProductSparePartController:
    def __init__(self):
        self.CRUDProductSparePart = CRUDProductSparePart()

    def create_product_spare_part_controller(self, request):
        """[Create a ProductSparePart record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductSparePart Data]
        """
        try:
            logging.info("executing create_product_spare_part_controller function")
            create_product_spare_part_request = request.dict(exclude_none=True)
            self.CRUDProductSparePart.create(**create_product_spare_part_request)
            return create_product_spare_part_request
        except Exception as error:
            logging.error(f"Error in create_product_spare_part_controller function: {error}")
            raise error

    def update_product_spare_part_controller(self, request):
        """[Update a ProductSparePart record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductSparePart Data]
        """
        try:
            logging.info("executing update_product_spare_part_controller function")
            update_product_spare_part_request = request.dict(exclude_none=True)
            self.CRUDProductSparePart.update(**update_product_spare_part_request)
            return update_product_spare_part_request
        except Exception as error:
            logging.error(f"Error in update_product_spare_part_controller function: {error}")
            raise error

    def get_all_product_spare_part_controller(self):
        """[Get All ProductSparePart records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductSparePart Records]
        """
        try:
            logging.info("executing get_all_product_spare_part_controller function")
            return self.CRUDProductSparePart.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_spare_part_controller function: {error}")
            raise error

    def get_product_spare_part_controller(self, part_id: int):
        """[Get a ProductSparePart record Controller]

        Args:
            part_id (int): [Unique Identifier for a ProductSparePart]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductSparePart Record]
        """
        try:
            logging.info("executing get_product_spare_part_controller function")
            return self.CRUDProductSparePart.read(part_id=part_id)
        except Exception as error:
            logging.error(f"Error in get_product_spare_part_controller function: {error}")
            raise error

    def delete_product_spare_part_controller(self, part_id: int):
        """[Controller to delete a ProductSparePart]

        Args:
            part_id (int): [Unique Identifier for a ProductSparePart]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductSparePart details]
        """
        try:
            logging.info("executing delete_product_spare_part_controller function")
            return self.CRUDProductSparePart.delete(part_id=part_id)
        except Exception as error:
            logging.error(f"Error in delete_product_spare_part_controller function: {error}")
            raise error
