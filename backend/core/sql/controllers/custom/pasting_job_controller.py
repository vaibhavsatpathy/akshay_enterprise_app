from sql import logger
from sql.crud.pasting_job_crud import CRUDPastingJob

logging = logger(__name__)


class PastingJobController:
    def __init__(self):
        self.CRUDPastingJob = CRUDPastingJob()

    def create_pasting_job_controller(self, request):
        """[Create a PastingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PastingJob Data]
        """
        try:
            logging.info("executing create_pasting_job_controller function")
            create_pasting_job_request = request.dict(exclude_none=True)
            self.CRUDPastingJob.create(**create_pasting_job_request)
            return create_pasting_job_request
        except Exception as error:
            logging.error(f"Error in create_pasting_job_controller function: {error}")
            raise error

    def update_pasting_job_controller(self, request):
        """[Update a PastingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PastingJob Data]
        """
        try:
            logging.info("executing update_pasting_job_controller function")
            update_pasting_job_request = request.dict(exclude_none=True)
            self.CRUDPastingJob.update(**update_pasting_job_request)
            return update_pasting_job_request
        except Exception as error:
            logging.error(f"Error in update_pasting_job_controller function: {error}")
            raise error

    def get_all_pasting_job_controller(self):
        """[Get All PastingJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all PastingJob Records]
        """
        try:
            logging.info("executing get_all_pasting_job_controller function")
            return self.CRUDPastingJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_pasting_job_controller function: {error}")
            raise error

    def get_pasting_job_controller(self, job_id: int):
        """[Get a PastingJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a PastingJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [PastingJob Record]
        """
        try:
            logging.info("executing get_pasting_job_controller function")
            return self.CRUDPastingJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_pasting_job_controller function: {error}")
            raise error

    def delete_pasting_job_controller(self, job_id: int):
        """[Controller to delete a PastingJob]

        Args:
            job_id (int): [Unique Identifier for a PastingJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted PastingJob details]
        """
        try:
            logging.info("executing delete_pasting_job_controller function")
            return self.CRUDPastingJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_pasting_job_controller function: {error}")
            raise error
