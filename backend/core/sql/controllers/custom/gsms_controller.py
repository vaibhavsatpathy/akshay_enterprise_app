from sql import logger
from sql.crud.gsms_crud import CRUDGsm

logging = logger(__name__)


class GsmController:
    def __init__(self):
        self.CRUDGsm = CRUDGsm()

    def create_gsm_controller(self, request):
        """[Create a Gsm record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Gsm Data]
        """
        try:
            logging.info("executing create_gsm_controller function")
            create_gsm_request = request.dict(exclude_none=True)
            crud_response = self.CRUDGsm.create(**create_gsm_request)
            return crud_response
        except Exception as error:
            logging.error(f"Error in create_gsm_controller function: {error}")
            raise error

    def update_gsm_controller(self, request):
        """[Update a Gsm record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Gsm Data]
        """
        try:
            logging.info("executing update_gsm_controller function")
            update_gsm_request = request.dict(exclude_none=True)
            self.CRUDGsm.update(**update_gsm_request)
            return update_gsm_request
        except Exception as error:
            logging.error(f"Error in update_gsm_controller function: {error}")
            raise error

    def get_all_gsm_controller(self):
        """[Get All Gsm records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Gsm Records]
        """
        try:
            logging.info("executing get_all_gsm_controller function")
            return self.CRUDGsm.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_gsm_controller function: {error}")
            raise error

    def get_gsm_controller(self, gsm_id: int):
        """[Get a Gsm record Controller]

        Args:
            gsm_id (int): [Unique Identifier for a Gsm]

        Raises:
            error: [Error]

        Returns:
            [type]: [Gsm Record]
        """
        try:
            logging.info("executing get_gsm_controller function")
            return self.CRUDGsm.read(gsm_id=gsm_id)
        except Exception as error:
            logging.error(f"Error in get_gsm_controller function: {error}")
            raise error

    def delete_gsm_controller(self, gsm_id: int):
        """[Controller to delete a Gsm]

        Args:
            gsm_id (int): [Unique Identifier for a Gsm]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Gsm details]
        """
        try:
            logging.info("executing delete_gsm_controller function")
            return self.CRUDGsm.delete(gsm_id=gsm_id)
        except Exception as error:
            logging.error(f"Error in delete_gsm_controller function: {error}")
            raise error
