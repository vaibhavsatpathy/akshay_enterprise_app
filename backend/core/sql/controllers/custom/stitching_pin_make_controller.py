from sql import logger
from sql.crud.stitching_pin_make_crud import CRUDStitchingPinMake

logging = logger(__name__)


class StitchingPinMakeController:
    def __init__(self):
        self.CRUDStitchingPinMake = CRUDStitchingPinMake()

    def create_stitching_pin_make_controller(self, request):
        """[Create a StitchingPinMake record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingPinMake Data]
        """
        try:
            logging.info("executing create_stitching_pin_make_controller function")
            create_stitching_pin_make_request = request.dict(exclude_none=True)
            self.CRUDStitchingPinMake.create(**create_stitching_pin_make_request)
            return create_stitching_pin_make_request
        except Exception as error:
            logging.error(f"Error in create_stitching_pin_make_controller function: {error}")
            raise error

    def update_stitching_pin_make_controller(self, request):
        """[Update a StitchingPinMake record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingPinMake Data]
        """
        try:
            logging.info("executing update_stitching_pin_make_controller function")
            update_stitching_pin_make_request = request.dict(exclude_none=True)
            self.CRUDStitchingPinMake.update(**update_stitching_pin_make_request)
            return update_stitching_pin_make_request
        except Exception as error:
            logging.error(f"Error in update_stitching_pin_make_controller function: {error}")
            raise error

    def get_all_stitching_pin_make_controller(self):
        """[Get All StitchingPinMake records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all StitchingPinMake Records]
        """
        try:
            logging.info("executing get_all_stitching_pin_make_controller function")
            return self.CRUDStitchingPinMake.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_stitching_pin_make_controller function: {error}")
            raise error

    def get_stitching_pin_make_controller(self, make_id: int):
        """[Get a StitchingPinMake record Controller]

        Args:
            make_id (int): [Unique Identifier for a StitchingPinMake]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingPinMake Record]
        """
        try:
            logging.info("executing get_stitching_pin_make_controller function")
            return self.CRUDStitchingPinMake.read(make_id=make_id)
        except Exception as error:
            logging.error(f"Error in get_stitching_pin_make_controller function: {error}")
            raise error

    def delete_stitching_pin_make_controller(self, make_id: int):
        """[Controller to delete a StitchingPinMake]

        Args:
            make_id (int): [Unique Identifier for a StitchingPinMake]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted StitchingPinMake details]
        """
        try:
            logging.info("executing delete_stitching_pin_make_controller function")
            return self.CRUDStitchingPinMake.delete(make_id=make_id)
        except Exception as error:
            logging.error(f"Error in delete_stitching_pin_make_controller function: {error}")
            raise error
