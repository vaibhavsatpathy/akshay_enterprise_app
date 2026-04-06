from sql import logger
from sql.crud.transporters_crud import CRUDTransporter

logging = logger(__name__)


class TransporterController:
    def __init__(self):
        self.CRUDTransporter = CRUDTransporter()

    def create_transporter_controller(self, request):
        """[Create a Transporter record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Transporter Data]
        """
        try:
            logging.info("executing create_transporter_controller function")
            create_transporter_request = request.dict(exclude_none=True)
            crud_response = self.CRUDTransporter.create(**create_transporter_request)
            return crud_response
        except Exception as error:
            logging.error(f"Error in create_transporter_controller function: {error}")
            raise error

    def update_transporter_controller(self, request):
        """[Update a Transporter record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Transporter Data]
        """
        try:
            logging.info("executing update_transporter_controller function")
            update_transporter_request = request.dict(exclude_none=True)
            self.CRUDTransporter.update(**update_transporter_request)
            return update_transporter_request
        except Exception as error:
            logging.error(f"Error in update_transporter_controller function: {error}")
            raise error

    def get_all_transporter_controller(self):
        """[Get All Transporter records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Transporter Records]
        """
        try:
            logging.info("executing get_all_transporter_controller function")
            return self.CRUDTransporter.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_transporter_controller function: {error}")
            raise error

    def get_transporter_controller(self, transporter_id: int):
        """[Get a Transporter record Controller]

        Args:
            transporter_id (int): [Unique Identifier for a Transporter]

        Raises:
            error: [Error]

        Returns:
            [type]: [Transporter Record]
        """
        try:
            logging.info("executing get_transporter_controller function")
            return self.CRUDTransporter.read(transporter_id=transporter_id)
        except Exception as error:
            logging.error(f"Error in get_transporter_controller function: {error}")
            raise error

    def delete_transporter_controller(self, transporter_id: int):
        """[Controller to delete a Transporter]

        Args:
            transporter_id (int): [Unique Identifier for a Transporter]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Transporter details]
        """
        try:
            logging.info("executing delete_transporter_controller function")
            return self.CRUDTransporter.delete(transporter_id=transporter_id)
        except Exception as error:
            logging.error(f"Error in delete_transporter_controller function: {error}")
            raise error
