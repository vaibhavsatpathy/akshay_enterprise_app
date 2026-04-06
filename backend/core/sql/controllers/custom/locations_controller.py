from sql import logger
from sql.crud.locations_crud import CRUDLocation

logging = logger(__name__)


class LocationController:
    def __init__(self):
        self.CRUDLocation = CRUDLocation()

    def create_location_controller(self, request):
        """[Create a Location record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Location Data]
        """
        try:
            logging.info("executing create_location_controller function")
            create_location_request = request.dict(exclude_none=True)
            crud_response = self.CRUDLocation.create(**create_location_request)
            return crud_response
        except Exception as error:
            logging.error(f"Error in create_location_controller function: {error}")
            raise error

    def update_location_controller(self, request):
        """[Update a Location record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Location Data]
        """
        try:
            logging.info("executing update_location_controller function")
            update_location_request = request.dict(exclude_none=True)
            self.CRUDLocation.update(**update_location_request)
            return update_location_request
        except Exception as error:
            logging.error(f"Error in update_location_controller function: {error}")
            raise error

    def get_all_location_controller(self):
        """[Get All Location records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Location Records]
        """
        try:
            logging.info("executing get_all_location_controller function")
            return self.CRUDLocation.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_location_controller function: {error}")
            raise error

    def get_location_controller(self, location_id: int):
        """[Get a Location record Controller]

        Args:
            location_id (int): [Unique Identifier for a Location]

        Raises:
            error: [Error]

        Returns:
            [type]: [Location Record]
        """
        try:
            logging.info("executing get_location_controller function")
            return self.CRUDLocation.read(location_id=location_id)
        except Exception as error:
            logging.error(f"Error in get_location_controller function: {error}")
            raise error

    def delete_location_controller(self, location_id: int):
        """[Controller to delete a Location]

        Args:
            location_id (int): [Unique Identifier for a Location]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Location details]
        """
        try:
            logging.info("executing delete_location_controller function")
            return self.CRUDLocation.delete(location_id=location_id)
        except Exception as error:
            logging.error(f"Error in delete_location_controller function: {error}")
            raise error
