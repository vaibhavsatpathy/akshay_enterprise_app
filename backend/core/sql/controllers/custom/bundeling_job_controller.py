from sql import logger
from sql.crud.bundeling_job_crud import CRUDBundelingJob

logging = logger(__name__)


class BundelingJobController:
    def __init__(self):
        self.CRUDBundelingJob = CRUDBundelingJob()

    def create_bundeling_job_controller(self, request):
        """[Create a BundelingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BundelingJob Data]
        """
        try:
            logging.info("executing create_bundeling_job_controller function")
            create_bundeling_job_request = request.dict(exclude_none=True)
            self.CRUDBundelingJob.create(**create_bundeling_job_request)
            return create_bundeling_job_request
        except Exception as error:
            logging.error(f"Error in create_bundeling_job_controller function: {error}")
            raise error

    def update_bundeling_job_controller(self, request):
        """[Update a BundelingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BundelingJob Data]
        """
        try:
            logging.info("executing update_bundeling_job_controller function")
            update_bundeling_job_request = request.dict(exclude_none=True)
            self.CRUDBundelingJob.update(**update_bundeling_job_request)
            return update_bundeling_job_request
        except Exception as error:
            logging.error(f"Error in update_bundeling_job_controller function: {error}")
            raise error

    def get_all_bundeling_job_controller(self):
        """[Get All BundelingJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all BundelingJob Records]
        """
        try:
            logging.info("executing get_all_bundeling_job_controller function")
            return self.CRUDBundelingJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_bundeling_job_controller function: {error}")
            raise error

    def get_bundeling_job_controller(self, job_id: int):
        """[Get a BundelingJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a BundelingJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [BundelingJob Record]
        """
        try:
            logging.info("executing get_bundeling_job_controller function")
            return self.CRUDBundelingJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_bundeling_job_controller function: {error}")
            raise error

    def delete_bundeling_job_controller(self, job_id: int):
        """[Controller to delete a BundelingJob]

        Args:
            job_id (int): [Unique Identifier for a BundelingJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted BundelingJob details]
        """
        try:
            logging.info("executing delete_bundeling_job_controller function")
            return self.CRUDBundelingJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_bundeling_job_controller function: {error}")
            raise error
