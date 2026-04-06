from sql import logger
from sql.crud.plate_types_crud import CRUDPlateType

logging = logger(__name__)


class PlateTypeController:
    def __init__(self):
        self.CRUDPlateType = CRUDPlateType()

    def create_plate_type_controller(self, request):
        """[Create a PlateType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PlateType Data]
        """
        try:
            logging.info("executing create_plate_type_controller function")
            create_plate_type_request = request.dict(exclude_none=True)
            self.CRUDPlateType.create(**create_plate_type_request)
            return create_plate_type_request
        except Exception as error:
            logging.error(f"Error in create_plate_type_controller function: {error}")
            raise error

    def update_plate_type_controller(self, request):
        """[Update a PlateType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PlateType Data]
        """
        try:
            logging.info("executing update_plate_type_controller function")
            update_plate_type_request = request.dict(exclude_none=True)
            self.CRUDPlateType.update(**update_plate_type_request)
            return update_plate_type_request
        except Exception as error:
            logging.error(f"Error in update_plate_type_controller function: {error}")
            raise error

    def get_all_plate_type_controller(self):
        """[Get All PlateType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all PlateType Records]
        """
        try:
            logging.info("executing get_all_plate_type_controller function")
            return self.CRUDPlateType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_plate_type_controller function: {error}")
            raise error

    def get_plate_type_controller(self, plate_type_id: int):
        """[Get a PlateType record Controller]

        Args:
            plate_type_id (int): [Unique Identifier for a PlateType]

        Raises:
            error: [Error]

        Returns:
            [type]: [PlateType Record]
        """
        try:
            logging.info("executing get_plate_type_controller function")
            return self.CRUDPlateType.read(plate_type_id=plate_type_id)
        except Exception as error:
            logging.error(f"Error in get_plate_type_controller function: {error}")
            raise error

    def delete_plate_type_controller(self, plate_type_id: int):
        """[Controller to delete a PlateType]

        Args:
            plate_type_id (int): [Unique Identifier for a PlateType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted PlateType details]
        """
        try:
            logging.info("executing delete_plate_type_controller function")
            return self.CRUDPlateType.delete(plate_type_id=plate_type_id)
        except Exception as error:
            logging.error(f"Error in delete_plate_type_controller function: {error}")
            raise error
