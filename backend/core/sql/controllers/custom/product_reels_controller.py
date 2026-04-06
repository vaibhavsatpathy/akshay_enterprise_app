from sql import logger
from sql.crud.product_reels_crud import CRUDProductReel

logging = logger(__name__)


class ProductReelController:
    def __init__(self):
        self.CRUDProductReel = CRUDProductReel()

    def create_product_reel_controller(self, request):
        """[Create a ProductReel record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductReel Data]
        """
        try:
            logging.info("executing create_product_reel_controller function")
            create_product_reel_request = request.dict(exclude_none=True)
            self.CRUDProductReel.create(**create_product_reel_request)
            return create_product_reel_request
        except Exception as error:
            logging.error(f"Error in create_product_reel_controller function: {error}")
            raise error

    def update_product_reel_controller(self, request):
        """[Update a ProductReel record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductReel Data]
        """
        try:
            logging.info("executing update_product_reel_controller function")
            update_product_reel_request = request.dict(exclude_none=True)
            self.CRUDProductReel.update(**update_product_reel_request)
            return update_product_reel_request
        except Exception as error:
            logging.error(f"Error in update_product_reel_controller function: {error}")
            raise error

    def get_all_product_reel_controller(self):
        """[Get All ProductReel records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductReel Records]
        """
        try:
            logging.info("executing get_all_product_reel_controller function")
            return self.CRUDProductReel.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_reel_controller function: {error}")
            raise error

    def get_product_reel_controller(self, reel_id: int):
        """[Get a ProductReel record Controller]

        Args:
            reel_id (int): [Unique Identifier for a ProductReel]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductReel Record]
        """
        try:
            logging.info("executing get_product_reel_controller function")
            return self.CRUDProductReel.read(reel_id=reel_id)
        except Exception as error:
            logging.error(f"Error in get_product_reel_controller function: {error}")
            raise error

    def delete_product_reel_controller(self, reel_id: int):
        """[Controller to delete a ProductReel]

        Args:
            reel_id (int): [Unique Identifier for a ProductReel]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductReel details]
        """
        try:
            logging.info("executing delete_product_reel_controller function")
            return self.CRUDProductReel.delete(reel_id=reel_id)
        except Exception as error:
            logging.error(f"Error in delete_product_reel_controller function: {error}")
            raise error
