from sql import logger
from sql.crud.flute_types_crud import CRUDFluteType

logging = logger(__name__)


class FluteTypeController:
    def __init__(self):
        self.CRUDFluteType = CRUDFluteType()

    def create_flute_type_controller(self, request):
        """[Create a FluteType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [FluteType Data]
        """
        try:
            logging.info("executing create_flute_type_controller function")
            create_flute_type_request = request.dict(exclude_none=True)
            self.CRUDFluteType.create(**create_flute_type_request)
            return create_flute_type_request
        except Exception as error:
            logging.error(f"Error in create_flute_type_controller function: {error}")
            raise error

    def update_flute_type_controller(self, request):
        """[Update a FluteType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [FluteType Data]
        """
        try:
            logging.info("executing update_flute_type_controller function")
            update_flute_type_request = request.dict(exclude_none=True)
            self.CRUDFluteType.update(**update_flute_type_request)
            return update_flute_type_request
        except Exception as error:
            logging.error(f"Error in update_flute_type_controller function: {error}")
            raise error

    def get_all_flute_type_controller(self):
        """[Get All FluteType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all FluteType Records]
        """
        try:
            logging.info("executing get_all_flute_type_controller function")
            return self.CRUDFluteType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_flute_type_controller function: {error}")
            raise error

    def get_flute_type_controller(self, flute_type_id: int):
        """[Get a FluteType record Controller]

        Args:
            flute_type_id (int): [Unique Identifier for a FluteType]

        Raises:
            error: [Error]

        Returns:
            [type]: [FluteType Record]
        """
        try:
            logging.info("executing get_flute_type_controller function")
            return self.CRUDFluteType.read(flute_type_id=flute_type_id)
        except Exception as error:
            logging.error(f"Error in get_flute_type_controller function: {error}")
            raise error

    def delete_flute_type_controller(self, flute_type_id: int):
        """[Controller to delete a FluteType]

        Args:
            flute_type_id (int): [Unique Identifier for a FluteType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted FluteType details]
        """
        try:
            logging.info("executing delete_flute_type_controller function")
            return self.CRUDFluteType.delete(flute_type_id=flute_type_id)
        except Exception as error:
            logging.error(f"Error in delete_flute_type_controller function: {error}")
            raise error
