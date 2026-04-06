from sql import logger
from sql.crud.product_papers_crud import CRUDProductPaper

logging = logger(__name__)


class ProductPaperController:
    def __init__(self):
        self.CRUDProductPaper = CRUDProductPaper()

    def create_product_paper_controller(self, request):
        """[Create a ProductPaper record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductPaper Data]
        """
        try:
            logging.info("executing create_product_paper_controller function")
            create_product_paper_request = request.dict(exclude_none=True)
            self.CRUDProductPaper.create(**create_product_paper_request)
            return create_product_paper_request
        except Exception as error:
            logging.error(f"Error in create_product_paper_controller function: {error}")
            raise error

    def update_product_paper_controller(self, request):
        """[Update a ProductPaper record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductPaper Data]
        """
        try:
            logging.info("executing update_product_paper_controller function")
            update_product_paper_request = request.dict(exclude_none=True)
            self.CRUDProductPaper.update(**update_product_paper_request)
            return update_product_paper_request
        except Exception as error:
            logging.error(f"Error in update_product_paper_controller function: {error}")
            raise error

    def get_all_product_paper_controller(self):
        """[Get All ProductPaper records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductPaper Records]
        """
        try:
            logging.info("executing get_all_product_paper_controller function")
            return self.CRUDProductPaper.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_paper_controller function: {error}")
            raise error

    def get_product_paper_controller(self, gross_id: int):
        """[Get a ProductPaper record Controller]

        Args:
            gross_id (int): [Unique Identifier for a ProductPaper]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductPaper Record]
        """
        try:
            logging.info("executing get_product_paper_controller function")
            return self.CRUDProductPaper.read(gross_id=gross_id)
        except Exception as error:
            logging.error(f"Error in get_product_paper_controller function: {error}")
            raise error

    def delete_product_paper_controller(self, gross_id: int):
        """[Controller to delete a ProductPaper]

        Args:
            gross_id (int): [Unique Identifier for a ProductPaper]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductPaper details]
        """
        try:
            logging.info("executing delete_product_paper_controller function")
            return self.CRUDProductPaper.delete(gross_id=gross_id)
        except Exception as error:
            logging.error(f"Error in delete_product_paper_controller function: {error}")
            raise error
