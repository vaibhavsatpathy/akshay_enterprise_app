from sql import logger
from sql.crud.roll_types_crud import CRUDRollType

logging = logger(__name__)


class RollTypeController:
    def __init__(self):
        self.CRUDRollType = CRUDRollType()

    def create_roll_type_controller(self, request):
        """[Create a RollType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [RollType Data]
        """
        try:
            logging.info("executing create_roll_type_controller function")
            create_roll_type_request = request.dict(exclude_none=True)
            self.CRUDRollType.create(**create_roll_type_request)
            return create_roll_type_request
        except Exception as error:
            logging.error(f"Error in create_roll_type_controller function: {error}")
            raise error

    def update_roll_type_controller(self, request):
        """[Update a RollType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [RollType Data]
        """
        try:
            logging.info("executing update_roll_type_controller function")
            update_roll_type_request = request.dict(exclude_none=True)
            self.CRUDRollType.update(**update_roll_type_request)
            return update_roll_type_request
        except Exception as error:
            logging.error(f"Error in update_roll_type_controller function: {error}")
            raise error

    def get_all_roll_type_controller(self):
        """[Get All RollType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all RollType Records]
        """
        try:
            logging.info("executing get_all_roll_type_controller function")
            return self.CRUDRollType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_roll_type_controller function: {error}")
            raise error

    def get_roll_type_controller(self, roll_type_id: int):
        """[Get a RollType record Controller]

        Args:
            roll_type_id (int): [Unique Identifier for a RollType]

        Raises:
            error: [Error]

        Returns:
            [type]: [RollType Record]
        """
        try:
            logging.info("executing get_roll_type_controller function")
            return self.CRUDRollType.read(roll_type_id=roll_type_id)
        except Exception as error:
            logging.error(f"Error in get_roll_type_controller function: {error}")
            raise error

    def delete_roll_type_controller(self, roll_type_id: int):
        """[Controller to delete a RollType]

        Args:
            roll_type_id (int): [Unique Identifier for a RollType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted RollType details]
        """
        try:
            logging.info("executing delete_roll_type_controller function")
            return self.CRUDRollType.delete(roll_type_id=roll_type_id)
        except Exception as error:
            logging.error(f"Error in delete_roll_type_controller function: {error}")
            raise error
