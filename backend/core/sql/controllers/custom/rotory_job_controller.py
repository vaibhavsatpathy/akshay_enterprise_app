from sql import logger
from sql.crud.rotory_job_crud import CRUDRotoryJob

logging = logger(__name__)


class RotoryJobController:
    def __init__(self):
        self.CRUDRotoryJob = CRUDRotoryJob()

    def create_rotory_job_controller(self, request):
        """[Create a RotoryJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [RotoryJob Data]
        """
        try:
            logging.info("executing create_rotory_job_controller function")
            create_rotory_job_request = request.dict(exclude_none=True)
            self.CRUDRotoryJob.create(**create_rotory_job_request)
            return create_rotory_job_request
        except Exception as error:
            logging.error(f"Error in create_rotory_job_controller function: {error}")
            raise error

    def update_rotory_job_controller(self, request):
        """[Update a RotoryJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [RotoryJob Data]
        """
        try:
            logging.info("executing update_rotory_job_controller function")
            update_rotory_job_request = request.dict(exclude_none=True)
            self.CRUDRotoryJob.update(**update_rotory_job_request)
            return update_rotory_job_request
        except Exception as error:
            logging.error(f"Error in update_rotory_job_controller function: {error}")
            raise error

    def get_all_rotory_job_controller(self):
        """[Get All RotoryJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all RotoryJob Records]
        """
        try:
            logging.info("executing get_all_rotory_job_controller function")
            return self.CRUDRotoryJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_rotory_job_controller function: {error}")
            raise error

    def get_rotory_job_controller(self, job_id: int):
        """[Get a RotoryJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a RotoryJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [RotoryJob Record]
        """
        try:
            logging.info("executing get_rotory_job_controller function")
            return self.CRUDRotoryJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_rotory_job_controller function: {error}")
            raise error

    def delete_rotory_job_controller(self, job_id: int):
        """[Controller to delete a RotoryJob]

        Args:
            job_id (int): [Unique Identifier for a RotoryJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted RotoryJob details]
        """
        try:
            logging.info("executing delete_rotory_job_controller function")
            return self.CRUDRotoryJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_rotory_job_controller function: {error}")
            raise error
