from sql import logger
from sql.crud.die_punching_job_crud import CRUDDiePunchingJob

logging = logger(__name__)


class DiePunchingJobController:
    def __init__(self):
        self.CRUDDiePunchingJob = CRUDDiePunchingJob()

    def create_die_punching_job_controller(self, request):
        """[Create a DiePunchingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [DiePunchingJob Data]
        """
        try:
            logging.info("executing create_die_punching_job_controller function")
            create_die_punching_job_request = request.dict(exclude_none=True)
            self.CRUDDiePunchingJob.create(**create_die_punching_job_request)
            return create_die_punching_job_request
        except Exception as error:
            logging.error(f"Error in create_die_punching_job_controller function: {error}")
            raise error

    def update_die_punching_job_controller(self, request):
        """[Update a DiePunchingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [DiePunchingJob Data]
        """
        try:
            logging.info("executing update_die_punching_job_controller function")
            update_die_punching_job_request = request.dict(exclude_none=True)
            self.CRUDDiePunchingJob.update(**update_die_punching_job_request)
            return update_die_punching_job_request
        except Exception as error:
            logging.error(f"Error in update_die_punching_job_controller function: {error}")
            raise error

    def get_all_die_punching_job_controller(self):
        """[Get All DiePunchingJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all DiePunchingJob Records]
        """
        try:
            logging.info("executing get_all_die_punching_job_controller function")
            return self.CRUDDiePunchingJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_die_punching_job_controller function: {error}")
            raise error

    def get_die_punching_job_controller(self, job_id: int):
        """[Get a DiePunchingJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a DiePunchingJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [DiePunchingJob Record]
        """
        try:
            logging.info("executing get_die_punching_job_controller function")
            return self.CRUDDiePunchingJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_die_punching_job_controller function: {error}")
            raise error

    def delete_die_punching_job_controller(self, job_id: int):
        """[Controller to delete a DiePunchingJob]

        Args:
            job_id (int): [Unique Identifier for a DiePunchingJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted DiePunchingJob details]
        """
        try:
            logging.info("executing delete_die_punching_job_controller function")
            return self.CRUDDiePunchingJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_die_punching_job_controller function: {error}")
            raise error
