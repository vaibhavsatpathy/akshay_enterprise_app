from sql import logger
from sql.crud.stitching_job_crud import CRUDStitchingJob

logging = logger(__name__)


class StitchingJobController:
    def __init__(self):
        self.CRUDStitchingJob = CRUDStitchingJob()

    def create_stitching_job_controller(self, request):
        """[Create a StitchingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingJob Data]
        """
        try:
            logging.info("executing create_stitching_job_controller function")
            create_stitching_job_request = request.dict(exclude_none=True)
            self.CRUDStitchingJob.create(**create_stitching_job_request)
            return create_stitching_job_request
        except Exception as error:
            logging.error(f"Error in create_stitching_job_controller function: {error}")
            raise error

    def update_stitching_job_controller(self, request):
        """[Update a StitchingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingJob Data]
        """
        try:
            logging.info("executing update_stitching_job_controller function")
            update_stitching_job_request = request.dict(exclude_none=True)
            self.CRUDStitchingJob.update(**update_stitching_job_request)
            return update_stitching_job_request
        except Exception as error:
            logging.error(f"Error in update_stitching_job_controller function: {error}")
            raise error

    def get_all_stitching_job_controller(self):
        """[Get All StitchingJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all StitchingJob Records]
        """
        try:
            logging.info("executing get_all_stitching_job_controller function")
            return self.CRUDStitchingJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_stitching_job_controller function: {error}")
            raise error

    def get_stitching_job_controller(self, job_id: int):
        """[Get a StitchingJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a StitchingJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingJob Record]
        """
        try:
            logging.info("executing get_stitching_job_controller function")
            return self.CRUDStitchingJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_stitching_job_controller function: {error}")
            raise error

    def delete_stitching_job_controller(self, job_id: int):
        """[Controller to delete a StitchingJob]

        Args:
            job_id (int): [Unique Identifier for a StitchingJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted StitchingJob details]
        """
        try:
            logging.info("executing delete_stitching_job_controller function")
            return self.CRUDStitchingJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_stitching_job_controller function: {error}")
            raise error
