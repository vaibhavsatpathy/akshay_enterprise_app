from sql import logger
from sql.crud.product_ply_sheets_crud import CRUDProductPlySheet

logging = logger(__name__)


class ProductPlySheetController:
    def __init__(self):
        self.CRUDProductPlySheet = CRUDProductPlySheet()

    def create_product_ply_sheet_controller(self, request):
        """[Create a ProductPlySheet record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductPlySheet Data]
        """
        try:
            logging.info("executing create_product_ply_sheet_controller function")
            create_product_ply_sheet_request = request.dict(exclude_none=True)
            self.CRUDProductPlySheet.create(**create_product_ply_sheet_request)
            return create_product_ply_sheet_request
        except Exception as error:
            logging.error(f"Error in create_product_ply_sheet_controller function: {error}")
            raise error

    def update_product_ply_sheet_controller(self, request):
        """[Update a ProductPlySheet record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductPlySheet Data]
        """
        try:
            logging.info("executing update_product_ply_sheet_controller function")
            update_product_ply_sheet_request = request.dict(exclude_none=True)
            self.CRUDProductPlySheet.update(**update_product_ply_sheet_request)
            return update_product_ply_sheet_request
        except Exception as error:
            logging.error(f"Error in update_product_ply_sheet_controller function: {error}")
            raise error

    def get_all_product_ply_sheet_controller(self):
        """[Get All ProductPlySheet records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ProductPlySheet Records]
        """
        try:
            logging.info("executing get_all_product_ply_sheet_controller function")
            return self.CRUDProductPlySheet.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_product_ply_sheet_controller function: {error}")
            raise error

    def get_product_ply_sheet_controller(self, sheet_id: int):
        """[Get a ProductPlySheet record Controller]

        Args:
            sheet_id (int): [Unique Identifier for a ProductPlySheet]

        Raises:
            error: [Error]

        Returns:
            [type]: [ProductPlySheet Record]
        """
        try:
            logging.info("executing get_product_ply_sheet_controller function")
            return self.CRUDProductPlySheet.read(sheet_id=sheet_id)
        except Exception as error:
            logging.error(f"Error in get_product_ply_sheet_controller function: {error}")
            raise error

    def delete_product_ply_sheet_controller(self, sheet_id: int):
        """[Controller to delete a ProductPlySheet]

        Args:
            sheet_id (int): [Unique Identifier for a ProductPlySheet]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ProductPlySheet details]
        """
        try:
            logging.info("executing delete_product_ply_sheet_controller function")
            return self.CRUDProductPlySheet.delete(sheet_id=sheet_id)
        except Exception as error:
            logging.error(f"Error in delete_product_ply_sheet_controller function: {error}")
            raise error
