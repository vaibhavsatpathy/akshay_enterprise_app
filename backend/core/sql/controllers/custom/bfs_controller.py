from sql import logger
from sql.crud.bfs_crud import CRUDBf

logging = logger(__name__)


class BfController:
    def __init__(self):
        self.CRUDBf = CRUDBf()

    def create_bf_controller(self, request):
        """[Create a Bf record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Bf Data]
        """
        try:
            logging.info("executing create_bf_controller function")
            create_bf_request = request.dict(exclude_none=True)
            crud_response = self.CRUDBf.create(**create_bf_request)
            return crud_response
        except Exception as error:
            logging.error(f"Error in create_bf_controller function: {error}")
            raise error

    def update_bf_controller(self, request):
        """[Update a Bf record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Bf Data]
        """
        try:
            logging.info("executing update_bf_controller function")
            update_bf_request = request.dict(exclude_none=True)
            self.CRUDBf.update(**update_bf_request)
            return update_bf_request
        except Exception as error:
            logging.error(f"Error in update_bf_controller function: {error}")
            raise error

    def get_all_bf_controller(self):
        """[Get All Bf records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Bf Records]
        """
        try:
            logging.info("executing get_all_bf_controller function")
            return self.CRUDBf.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_bf_controller function: {error}")
            raise error

    def get_bf_controller(self, bf_id: int):
        """[Get a Bf record Controller]

        Args:
            bf_id (int): [Unique Identifier for a Bf]

        Raises:
            error: [Error]

        Returns:
            [type]: [Bf Record]
        """
        try:
            logging.info("executing get_bf_controller function")
            return self.CRUDBf.read(bf_id=bf_id)
        except Exception as error:
            logging.error(f"Error in get_bf_controller function: {error}")
            raise error

    def delete_bf_controller(self, bf_id: int):
        """[Controller to delete a Bf]

        Args:
            bf_id (int): [Unique Identifier for a Bf]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Bf details]
        """
        try:
            logging.info("executing delete_bf_controller function")
            return self.CRUDBf.delete(bf_id=bf_id)
        except Exception as error:
            logging.error(f"Error in delete_bf_controller function: {error}")
            raise error
