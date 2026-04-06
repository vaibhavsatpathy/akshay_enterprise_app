from sql import logger
from sql.crud.vendors_crud import CRUDVendor

logging = logger(__name__)


class VendorController:
    def __init__(self):
        self.CRUDVendor = CRUDVendor()

    def create_vendor_controller(self, request):
        """[Create a Vendor record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Vendor Data]
        """
        try:
            logging.info("executing create_vendor_controller function")
            create_vendor_request = request.dict(exclude_none=True)
            crud_response = self.CRUDVendor.create(**create_vendor_request)
            return crud_response
        except Exception as error:
            logging.error(f"Error in create_vendor_controller function: {error}")
            raise error

    def update_vendor_controller(self, request):
        """[Update a Vendor record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Vendor Data]
        """
        try:
            logging.info("executing update_vendor_controller function")
            update_vendor_request = request.dict(exclude_none=True)
            self.CRUDVendor.update(**update_vendor_request)
            return update_vendor_request
        except Exception as error:
            logging.error(f"Error in update_vendor_controller function: {error}")
            raise error

    def get_all_vendor_controller(self):
        """[Get All Vendor records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Vendor Records]
        """
        try:
            logging.info("executing get_all_vendor_controller function")
            return self.CRUDVendor.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_vendor_controller function: {error}")
            raise error

    def get_vendor_controller(self, vendor_id: int):
        """[Get a Vendor record Controller]

        Args:
            vendor_id (int): [Unique Identifier for a Vendor]

        Raises:
            error: [Error]

        Returns:
            [type]: [Vendor Record]
        """
        try:
            logging.info("executing get_vendor_controller function")
            return self.CRUDVendor.read(vendor_id=vendor_id)
        except Exception as error:
            logging.error(f"Error in get_vendor_controller function: {error}")
            raise error

    def delete_vendor_controller(self, vendor_id: int):
        """[Controller to delete a Vendor]

        Args:
            vendor_id (int): [Unique Identifier for a Vendor]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Vendor details]
        """
        try:
            logging.info("executing delete_vendor_controller function")
            return self.CRUDVendor.delete(vendor_id=vendor_id)
        except Exception as error:
            logging.error(f"Error in delete_vendor_controller function: {error}")
            raise error
