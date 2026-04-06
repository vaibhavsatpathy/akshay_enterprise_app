from sql import logger
from sql.crud.file_types_crud import CRUDFileType

logging = logger(__name__)


class FileTypeController:
    def __init__(self):
        self.CRUDFileType = CRUDFileType()

    def create_file_type_controller(self, request):
        """[Create a FileType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [FileType Data]
        """
        try:
            logging.info("executing create_file_type_controller function")
            create_file_type_request = request.dict(exclude_none=True)
            self.CRUDFileType.create(**create_file_type_request)
            return create_file_type_request
        except Exception as error:
            logging.error(f"Error in create_file_type_controller function: {error}")
            raise error

    def update_file_type_controller(self, request):
        """[Update a FileType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [FileType Data]
        """
        try:
            logging.info("executing update_file_type_controller function")
            update_file_type_request = request.dict(exclude_none=True)
            self.CRUDFileType.update(**update_file_type_request)
            return update_file_type_request
        except Exception as error:
            logging.error(f"Error in update_file_type_controller function: {error}")
            raise error

    def get_all_file_type_controller(self):
        """[Get All FileType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all FileType Records]
        """
        try:
            logging.info("executing get_all_file_type_controller function")
            return self.CRUDFileType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_file_type_controller function: {error}")
            raise error

    def get_file_type_controller(self, file_type_id: int):
        """[Get a FileType record Controller]

        Args:
            file_type_id (int): [Unique Identifier for a FileType]

        Raises:
            error: [Error]

        Returns:
            [type]: [FileType Record]
        """
        try:
            logging.info("executing get_file_type_controller function")
            return self.CRUDFileType.read(file_type_id=file_type_id)
        except Exception as error:
            logging.error(f"Error in get_file_type_controller function: {error}")
            raise error

    def delete_file_type_controller(self, file_type_id: int):
        """[Controller to delete a FileType]

        Args:
            file_type_id (int): [Unique Identifier for a FileType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted FileType details]
        """
        try:
            logging.info("executing delete_file_type_controller function")
            return self.CRUDFileType.delete(file_type_id=file_type_id)
        except Exception as error:
            logging.error(f"Error in delete_file_type_controller function: {error}")
            raise error
