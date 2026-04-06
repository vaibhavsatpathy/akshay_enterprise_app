from sql import logger
from sql.crud.offset_plate_crud import CRUDOffsetPlate

logging = logger(__name__)


class OffsetPlateController:
    def __init__(self):
        self.CRUDOffsetPlate = CRUDOffsetPlate()

    def create_offset_plate_controller(self, request):
        """[Create a OffsetPlate record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [OffsetPlate Data]
        """
        try:
            logging.info("executing create_offset_plate_controller function")
            create_offset_plate_request = request.dict(exclude_none=True)
            self.CRUDOffsetPlate.create(**create_offset_plate_request)
            return create_offset_plate_request
        except Exception as error:
            logging.error(f"Error in create_offset_plate_controller function: {error}")
            raise error

    def update_offset_plate_controller(self, request):
        """[Update a OffsetPlate record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [OffsetPlate Data]
        """
        try:
            logging.info("executing update_offset_plate_controller function")
            update_offset_plate_request = request.dict(exclude_none=True)
            self.CRUDOffsetPlate.update(**update_offset_plate_request)
            return update_offset_plate_request
        except Exception as error:
            logging.error(f"Error in update_offset_plate_controller function: {error}")
            raise error

    def get_all_offset_plate_controller(self):
        """[Get All OffsetPlate records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all OffsetPlate Records]
        """
        try:
            logging.info("executing get_all_offset_plate_controller function")
            return self.CRUDOffsetPlate.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_offset_plate_controller function: {error}")
            raise error

    def get_offset_plate_controller(self, plate_id: int):
        """[Get a OffsetPlate record Controller]

        Args:
            plate_id (int): [Unique Identifier for a OffsetPlate]

        Raises:
            error: [Error]

        Returns:
            [type]: [OffsetPlate Record]
        """
        try:
            logging.info("executing get_offset_plate_controller function")
            return self.CRUDOffsetPlate.read(plate_id=plate_id)
        except Exception as error:
            logging.error(f"Error in get_offset_plate_controller function: {error}")
            raise error

    def delete_offset_plate_controller(self, plate_id: int):
        """[Controller to delete a OffsetPlate]

        Args:
            plate_id (int): [Unique Identifier for a OffsetPlate]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted OffsetPlate details]
        """
        try:
            logging.info("executing delete_offset_plate_controller function")
            return self.CRUDOffsetPlate.delete(plate_id=plate_id)
        except Exception as error:
            logging.error(f"Error in delete_offset_plate_controller function: {error}")
            raise error
