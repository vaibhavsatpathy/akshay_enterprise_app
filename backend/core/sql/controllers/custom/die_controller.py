from sql import logger
from sql.crud.die_crud import CRUDDie

logging = logger(__name__)


class DieController:
    def __init__(self):
        self.CRUDDie = CRUDDie()

    def create_die_controller(self, request):
        """[Create a Die record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Die Data]
        """
        try:
            logging.info("executing create_die_controller function")
            create_die_request = request.dict(exclude_none=True)
            self.CRUDDie.create(**create_die_request)
            return create_die_request
        except Exception as error:
            logging.error(f"Error in create_die_controller function: {error}")
            raise error

    def update_die_controller(self, request):
        """[Update a Die record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Die Data]
        """
        try:
            logging.info("executing update_die_controller function")
            update_die_request = request.dict(exclude_none=True)
            self.CRUDDie.update(**update_die_request)
            return update_die_request
        except Exception as error:
            logging.error(f"Error in update_die_controller function: {error}")
            raise error

    def get_all_die_controller(self):
        """[Get All Die records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Die Records]
        """
        try:
            logging.info("executing get_all_die_controller function")
            return self.CRUDDie.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_die_controller function: {error}")
            raise error

    def get_die_controller(self, die_id: int):
        """[Get a Die record Controller]

        Args:
            die_id (int): [Unique Identifier for a Die]

        Raises:
            error: [Error]

        Returns:
            [type]: [Die Record]
        """
        try:
            logging.info("executing get_die_controller function")
            return self.CRUDDie.read(die_id=die_id)
        except Exception as error:
            logging.error(f"Error in get_die_controller function: {error}")
            raise error

    def delete_die_controller(self, die_id: int):
        """[Controller to delete a Die]

        Args:
            die_id (int): [Unique Identifier for a Die]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Die details]
        """
        try:
            logging.info("executing delete_die_controller function")
            return self.CRUDDie.delete(die_id=die_id)
        except Exception as error:
            logging.error(f"Error in delete_die_controller function: {error}")
            raise error
