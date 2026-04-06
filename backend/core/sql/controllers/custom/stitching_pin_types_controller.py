from sql import logger
from sql.crud.stitching_pin_types_crud import CRUDStitchingPinType

logging = logger(__name__)


class StitchingPinTypeController:
    def __init__(self):
        self.CRUDStitchingPinType = CRUDStitchingPinType()

    def create_stitching_pin_type_controller(self, request):
        """[Create a StitchingPinType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingPinType Data]
        """
        try:
            logging.info("executing create_stitching_pin_type_controller function")
            create_stitching_pin_type_request = request.dict(exclude_none=True)
            self.CRUDStitchingPinType.create(**create_stitching_pin_type_request)
            return create_stitching_pin_type_request
        except Exception as error:
            logging.error(f"Error in create_stitching_pin_type_controller function: {error}")
            raise error

    def update_stitching_pin_type_controller(self, request):
        """[Update a StitchingPinType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingPinType Data]
        """
        try:
            logging.info("executing update_stitching_pin_type_controller function")
            update_stitching_pin_type_request = request.dict(exclude_none=True)
            self.CRUDStitchingPinType.update(**update_stitching_pin_type_request)
            return update_stitching_pin_type_request
        except Exception as error:
            logging.error(f"Error in update_stitching_pin_type_controller function: {error}")
            raise error

    def get_all_stitching_pin_type_controller(self):
        """[Get All StitchingPinType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all StitchingPinType Records]
        """
        try:
            logging.info("executing get_all_stitching_pin_type_controller function")
            return self.CRUDStitchingPinType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_stitching_pin_type_controller function: {error}")
            raise error

    def get_stitching_pin_type_controller(self, pin_type_id: int):
        """[Get a StitchingPinType record Controller]

        Args:
            pin_type_id (int): [Unique Identifier for a StitchingPinType]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingPinType Record]
        """
        try:
            logging.info("executing get_stitching_pin_type_controller function")
            return self.CRUDStitchingPinType.read(pin_type_id=pin_type_id)
        except Exception as error:
            logging.error(f"Error in get_stitching_pin_type_controller function: {error}")
            raise error

    def delete_stitching_pin_type_controller(self, pin_type_id: int):
        """[Controller to delete a StitchingPinType]

        Args:
            pin_type_id (int): [Unique Identifier for a StitchingPinType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted StitchingPinType details]
        """
        try:
            logging.info("executing delete_stitching_pin_type_controller function")
            return self.CRUDStitchingPinType.delete(pin_type_id=pin_type_id)
        except Exception as error:
            logging.error(f"Error in delete_stitching_pin_type_controller function: {error}")
            raise error
