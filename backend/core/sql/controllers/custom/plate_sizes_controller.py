from sql import logger
from sql.crud.plate_sizes_crud import CRUDPlateSize

logging = logger(__name__)


class PlateSizeController:
    def __init__(self):
        self.CRUDPlateSize = CRUDPlateSize()

    def create_plate_size_controller(self, request):
        """[Create a PlateSize record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PlateSize Data]
        """
        try:
            logging.info("executing create_plate_size_controller function")
            create_plate_size_request = request.dict(exclude_none=True)
            self.CRUDPlateSize.create(**create_plate_size_request)
            return create_plate_size_request
        except Exception as error:
            logging.error(f"Error in create_plate_size_controller function: {error}")
            raise error

    def update_plate_size_controller(self, request):
        """[Update a PlateSize record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PlateSize Data]
        """
        try:
            logging.info("executing update_plate_size_controller function")
            update_plate_size_request = request.dict(exclude_none=True)
            self.CRUDPlateSize.update(**update_plate_size_request)
            return update_plate_size_request
        except Exception as error:
            logging.error(f"Error in update_plate_size_controller function: {error}")
            raise error

    def get_all_plate_size_controller(self):
        """[Get All PlateSize records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all PlateSize Records]
        """
        try:
            logging.info("executing get_all_plate_size_controller function")
            return self.CRUDPlateSize.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_plate_size_controller function: {error}")
            raise error

    def get_plate_size_controller(self, plate_size_id: int):
        """[Get a PlateSize record Controller]

        Args:
            plate_size_id (int): [Unique Identifier for a PlateSize]

        Raises:
            error: [Error]

        Returns:
            [type]: [PlateSize Record]
        """
        try:
            logging.info("executing get_plate_size_controller function")
            return self.CRUDPlateSize.read(plate_size_id=plate_size_id)
        except Exception as error:
            logging.error(f"Error in get_plate_size_controller function: {error}")
            raise error

    def delete_plate_size_controller(self, plate_size_id: int):
        """[Controller to delete a PlateSize]

        Args:
            plate_size_id (int): [Unique Identifier for a PlateSize]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted PlateSize details]
        """
        try:
            logging.info("executing delete_plate_size_controller function")
            return self.CRUDPlateSize.delete(plate_size_id=plate_size_id)
        except Exception as error:
            logging.error(f"Error in delete_plate_size_controller function: {error}")
            raise error
