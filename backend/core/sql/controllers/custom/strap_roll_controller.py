from sql import logger
from sql.crud.strap_roll_crud import CRUDStrapRoll

logging = logger(__name__)


class StrapRollController:
    def __init__(self):
        self.CRUDStrapRoll = CRUDStrapRoll()

    def create_strap_roll_controller(self, request):
        """[Create a StrapRoll record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StrapRoll Data]
        """
        try:
            logging.info("executing create_strap_roll_controller function")
            create_strap_roll_request = request.dict(exclude_none=True)
            self.CRUDStrapRoll.create(**create_strap_roll_request)
            return create_strap_roll_request
        except Exception as error:
            logging.error(f"Error in create_strap_roll_controller function: {error}")
            raise error

    def update_strap_roll_controller(self, request):
        """[Update a StrapRoll record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StrapRoll Data]
        """
        try:
            logging.info("executing update_strap_roll_controller function")
            update_strap_roll_request = request.dict(exclude_none=True)
            self.CRUDStrapRoll.update(**update_strap_roll_request)
            return update_strap_roll_request
        except Exception as error:
            logging.error(f"Error in update_strap_roll_controller function: {error}")
            raise error

    def get_all_strap_roll_controller(self):
        """[Get All StrapRoll records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all StrapRoll Records]
        """
        try:
            logging.info("executing get_all_strap_roll_controller function")
            return self.CRUDStrapRoll.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_strap_roll_controller function: {error}")
            raise error

    def get_strap_roll_controller(self, roll_id: int):
        """[Get a StrapRoll record Controller]

        Args:
            roll_id (int): [Unique Identifier for a StrapRoll]

        Raises:
            error: [Error]

        Returns:
            [type]: [StrapRoll Record]
        """
        try:
            logging.info("executing get_strap_roll_controller function")
            return self.CRUDStrapRoll.read(roll_id=roll_id)
        except Exception as error:
            logging.error(f"Error in get_strap_roll_controller function: {error}")
            raise error

    def delete_strap_roll_controller(self, roll_id: int):
        """[Controller to delete a StrapRoll]

        Args:
            roll_id (int): [Unique Identifier for a StrapRoll]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted StrapRoll details]
        """
        try:
            logging.info("executing delete_strap_roll_controller function")
            return self.CRUDStrapRoll.delete(roll_id=roll_id)
        except Exception as error:
            logging.error(f"Error in delete_strap_roll_controller function: {error}")
            raise error
