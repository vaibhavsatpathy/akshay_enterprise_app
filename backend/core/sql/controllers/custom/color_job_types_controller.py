from sql import logger
from sql.crud.color_job_types_crud import CRUDColorJobType

logging = logger(__name__)


class ColorJobTypeController:
    def __init__(self):
        self.CRUDColorJobType = CRUDColorJobType()

    def create_color_job_type_controller(self, request):
        """[Create a ColorJobType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ColorJobType Data]
        """
        try:
            logging.info("executing create_color_job_type_controller function")
            create_color_job_type_request = request.dict(exclude_none=True)
            self.CRUDColorJobType.create(**create_color_job_type_request)
            return create_color_job_type_request
        except Exception as error:
            logging.error(f"Error in create_color_job_type_controller function: {error}")
            raise error

    def update_color_job_type_controller(self, request):
        """[Update a ColorJobType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ColorJobType Data]
        """
        try:
            logging.info("executing update_color_job_type_controller function")
            update_color_job_type_request = request.dict(exclude_none=True)
            self.CRUDColorJobType.update(**update_color_job_type_request)
            return update_color_job_type_request
        except Exception as error:
            logging.error(f"Error in update_color_job_type_controller function: {error}")
            raise error

    def get_all_color_job_type_controller(self):
        """[Get All ColorJobType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ColorJobType Records]
        """
        try:
            logging.info("executing get_all_color_job_type_controller function")
            return self.CRUDColorJobType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_color_job_type_controller function: {error}")
            raise error

    def get_color_job_type_controller(self, color_job_type_id: int):
        """[Get a ColorJobType record Controller]

        Args:
            color_job_type_id (int): [Unique Identifier for a ColorJobType]

        Raises:
            error: [Error]

        Returns:
            [type]: [ColorJobType Record]
        """
        try:
            logging.info("executing get_color_job_type_controller function")
            return self.CRUDColorJobType.read(color_job_type_id=color_job_type_id)
        except Exception as error:
            logging.error(f"Error in get_color_job_type_controller function: {error}")
            raise error

    def delete_color_job_type_controller(self, color_job_type_id: int):
        """[Controller to delete a ColorJobType]

        Args:
            color_job_type_id (int): [Unique Identifier for a ColorJobType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ColorJobType details]
        """
        try:
            logging.info("executing delete_color_job_type_controller function")
            return self.CRUDColorJobType.delete(color_job_type_id=color_job_type_id)
        except Exception as error:
            logging.error(f"Error in delete_color_job_type_controller function: {error}")
            raise error
