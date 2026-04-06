from sql import logger
from sql.crud.side_pasting_job_crud import CRUDSidePastingJob

logging = logger(__name__)


class SidePastingJobController:
    def __init__(self):
        self.CRUDSidePastingJob = CRUDSidePastingJob()

    def create_side_pasting_job_controller(self, request):
        """[Create a SidePastingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [SidePastingJob Data]
        """
        try:
            logging.info("executing create_side_pasting_job_controller function")
            create_side_pasting_job_request = request.dict(exclude_none=True)
            self.CRUDSidePastingJob.create(**create_side_pasting_job_request)
            return create_side_pasting_job_request
        except Exception as error:
            logging.error(f"Error in create_side_pasting_job_controller function: {error}")
            raise error

    def update_side_pasting_job_controller(self, request):
        """[Update a SidePastingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [SidePastingJob Data]
        """
        try:
            logging.info("executing update_side_pasting_job_controller function")
            update_side_pasting_job_request = request.dict(exclude_none=True)
            self.CRUDSidePastingJob.update(**update_side_pasting_job_request)
            return update_side_pasting_job_request
        except Exception as error:
            logging.error(f"Error in update_side_pasting_job_controller function: {error}")
            raise error

    def get_all_side_pasting_job_controller(self):
        """[Get All SidePastingJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all SidePastingJob Records]
        """
        try:
            logging.info("executing get_all_side_pasting_job_controller function")
            return self.CRUDSidePastingJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_side_pasting_job_controller function: {error}")
            raise error

    def get_side_pasting_job_controller(self, job_id: int):
        """[Get a SidePastingJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a SidePastingJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [SidePastingJob Record]
        """
        try:
            logging.info("executing get_side_pasting_job_controller function")
            return self.CRUDSidePastingJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_side_pasting_job_controller function: {error}")
            raise error

    def delete_side_pasting_job_controller(self, job_id: int):
        """[Controller to delete a SidePastingJob]

        Args:
            job_id (int): [Unique Identifier for a SidePastingJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted SidePastingJob details]
        """
        try:
            logging.info("executing delete_side_pasting_job_controller function")
            return self.CRUDSidePastingJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_side_pasting_job_controller function: {error}")
            raise error
