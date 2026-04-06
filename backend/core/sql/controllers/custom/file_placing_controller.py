from sql import logger
from sql.crud.file_placing_crud import CRUDFilePlacing

logging = logger(__name__)


class FilePlacingController:
    def __init__(self):
        self.CRUDFilePlacing = CRUDFilePlacing()

    def create_file_placing_controller(self, request):
        """[Create a FilePlacing record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [FilePlacing Data]
        """
        try:
            logging.info("executing create_file_placing_controller function")
            create_file_placing_request = request.dict(exclude_none=True)
            self.CRUDFilePlacing.create(**create_file_placing_request)
            return create_file_placing_request
        except Exception as error:
            logging.error(f"Error in create_file_placing_controller function: {error}")
            raise error

    def update_file_placing_controller(self, request):
        """[Update a FilePlacing record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [FilePlacing Data]
        """
        try:
            logging.info("executing update_file_placing_controller function")
            update_file_placing_request = request.dict(exclude_none=True)
            self.CRUDFilePlacing.update(**update_file_placing_request)
            return update_file_placing_request
        except Exception as error:
            logging.error(f"Error in update_file_placing_controller function: {error}")
            raise error

    def get_all_file_placing_controller(self):
        """[Get All FilePlacing records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all FilePlacing Records]
        """
        try:
            logging.info("executing get_all_file_placing_controller function")
            return self.CRUDFilePlacing.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_file_placing_controller function: {error}")
            raise error

    def get_file_placing_controller(self, file_id: int):
        """[Get a FilePlacing record Controller]

        Args:
            file_id (int): [Unique Identifier for a FilePlacing]

        Raises:
            error: [Error]

        Returns:
            [type]: [FilePlacing Record]
        """
        try:
            logging.info("executing get_file_placing_controller function")
            return self.CRUDFilePlacing.read(file_id=file_id)
        except Exception as error:
            logging.error(f"Error in get_file_placing_controller function: {error}")
            raise error

    def delete_file_placing_controller(self, file_id: int):
        """[Controller to delete a FilePlacing]

        Args:
            file_id (int): [Unique Identifier for a FilePlacing]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted FilePlacing details]
        """
        try:
            logging.info("executing delete_file_placing_controller function")
            return self.CRUDFilePlacing.delete(file_id=file_id)
        except Exception as error:
            logging.error(f"Error in delete_file_placing_controller function: {error}")
            raise error
