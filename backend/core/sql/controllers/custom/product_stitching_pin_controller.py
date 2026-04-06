from sql import logger
from sql.crud.product_stitching_pin_crud import CRUDProductStitchingPin

logging = logger(__name__)


class ProductStitchingPinController:
    def __init__(self):
        self.CRUDProductStitchingPin = CRUDProductStitchingPin()

    def create_product_stitching_pin_controller(self, request):
        """[Create a ProductStitchingPin record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductStitchingPin Data]
        """
        try:
            logging.info("executing create_product_stitching_pin_controller function")
            create_product_stitching_pin_request = request.dict(exclude_none=True)
            self.CRUDProductStitchingPin.create(**create_product_stitching_pin_request)
            return create_product_stitching_pin_request
        except Exception as error:
            logging.error(f"Error in create_product_stitching_pin_controller function: {error}")
            raise error

    def update_product_stitching_pin_controller(self, request):
        """[Update a ProductStitchingPin record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductStitchingPin Data]
        """
        try:
            logging.info("executing update_product_stitching_pin_controller function")
            update_product_stitching_pin_request = request.dict(exclude_none=True)
            self.CRUDProductStitchingPin.update(**update_product_stitching_pin_request)
            return update_product_stitching_pin_request
        except Exception as error:
            logging.error(f"Error in update_product_stitching_pin_controller function: {error}")
            raise error

    def get_all_product_stitching_pin_controller(self):
        """[Get All ProductStitchingPin records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductStitchingPin Records]
        """
        try:
            logging.info("executing get_all_product_stitching_pin_controller function")
            return self.CRUDProductStitchingPin.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_stitching_pin_controller function: {error}")
            raise error

    def get_product_stitching_pin_controller(self, pin_id: int):
        """[Get a ProductStitchingPin record Controller]

        Args:
            pin_id (int): [Unique Identifier for a ProductStitchingPin]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductStitchingPin Record]
        """
        try:
            logging.info("executing get_product_stitching_pin_controller function")
            return self.CRUDProductStitchingPin.read(pin_id=pin_id)
        except Exception as error:
            logging.error(f"Error in get_product_stitching_pin_controller function: {error}")
            raise error

    def delete_product_stitching_pin_controller(self, pin_id: int):
        """[Controller to delete a ProductStitchingPin]

        Args:
            pin_id (int): [Unique Identifier for a ProductStitchingPin]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductStitchingPin details]
        """
        try:
            logging.info("executing delete_product_stitching_pin_controller function")
            return self.CRUDProductStitchingPin.delete(pin_id=pin_id)
        except Exception as error:
            logging.error(f"Error in delete_product_stitching_pin_controller function: {error}")
            raise error
