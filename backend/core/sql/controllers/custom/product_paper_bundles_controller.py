from sql import logger
from sql.crud.product_paper_bundles_crud import CRUDProductPaperBundle

logging = logger(__name__)


class ProductPaperBundleController:
    def __init__(self):
        self.CRUDProductPaperBundle = CRUDProductPaperBundle()

    def create_product_paper_bundle_controller(self, request):
        """[Create a ProductPaperBundle record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductPaperBundle Data]
        """
        try:
            logging.info("executing create_product_paper_bundle_controller function")
            create_product_paper_bundle_request = request.dict(exclude_none=True)
            self.CRUDProductPaperBundle.create(**create_product_paper_bundle_request)
            return create_product_paper_bundle_request
        except Exception as error:
            logging.error(f"Error in create_product_paper_bundle_controller function: {error}")
            raise error

    def update_product_paper_bundle_controller(self, request):
        """[Update a ProductPaperBundle record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductPaperBundle Data]
        """
        try:
            logging.info("executing update_product_paper_bundle_controller function")
            update_product_paper_bundle_request = request.dict(exclude_none=True)
            self.CRUDProductPaperBundle.update(**update_product_paper_bundle_request)
            return update_product_paper_bundle_request
        except Exception as error:
            logging.error(f"Error in update_product_paper_bundle_controller function: {error}")
            raise error

    def get_all_product_paper_bundle_controller(self):
        """[Get All ProductPaperBundle records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductPaperBundle Records]
        """
        try:
            logging.info("executing get_all_product_paper_bundle_controller function")
            return self.CRUDProductPaperBundle.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_paper_bundle_controller function: {error}")
            raise error

    def get_product_paper_bundle_controller(self, bundle_id: int):
        """[Get a ProductPaperBundle record Controller]

        Args:
            bundle_id (int): [Unique Identifier for a ProductPaperBundle]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductPaperBundle Record]
        """
        try:
            logging.info("executing get_product_paper_bundle_controller function")
            return self.CRUDProductPaperBundle.read(bundle_id=bundle_id)
        except Exception as error:
            logging.error(f"Error in get_product_paper_bundle_controller function: {error}")
            raise error

    def delete_product_paper_bundle_controller(self, bundle_id: int):
        """[Controller to delete a ProductPaperBundle]

        Args:
            bundle_id (int): [Unique Identifier for a ProductPaperBundle]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductPaperBundle details]
        """
        try:
            logging.info("executing delete_product_paper_bundle_controller function")
            return self.CRUDProductPaperBundle.delete(bundle_id=bundle_id)
        except Exception as error:
            logging.error(f"Error in delete_product_paper_bundle_controller function: {error}")
            raise error
