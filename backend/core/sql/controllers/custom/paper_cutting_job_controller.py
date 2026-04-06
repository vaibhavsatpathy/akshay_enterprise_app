from sql import logger
from sql.crud.paper_cutting_job_crud import CRUDPaperCuttingJob

logging = logger(__name__)


class PaperCuttingJobController:
    def __init__(self):
        self.CRUDPaperCuttingJob = CRUDPaperCuttingJob()

    def create_paper_cutting_job_controller(self, request):
        """[Create a PaperCuttingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PaperCuttingJob Data]
        """
        try:
            logging.info("executing create_paper_cutting_job_controller function")
            create_paper_cutting_job_request = request.dict(exclude_none=True)
            self.CRUDPaperCuttingJob.create(**create_paper_cutting_job_request)
            return create_paper_cutting_job_request
        except Exception as error:
            logging.error(f"Error in create_paper_cutting_job_controller function: {error}")
            raise error

    def update_paper_cutting_job_controller(self, request):
        """[Update a PaperCuttingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PaperCuttingJob Data]
        """
        try:
            logging.info("executing update_paper_cutting_job_controller function")
            update_paper_cutting_job_request = request.dict(exclude_none=True)
            self.CRUDPaperCuttingJob.update(**update_paper_cutting_job_request)
            return update_paper_cutting_job_request
        except Exception as error:
            logging.error(f"Error in update_paper_cutting_job_controller function: {error}")
            raise error

    def get_all_paper_cutting_job_controller(self):
        """[Get All PaperCuttingJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all PaperCuttingJob Records]
        """
        try:
            logging.info("executing get_all_paper_cutting_job_controller function")
            return self.CRUDPaperCuttingJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_paper_cutting_job_controller function: {error}")
            raise error

    def get_paper_cutting_job_controller(self, job_id: int):
        """[Get a PaperCuttingJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a PaperCuttingJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [PaperCuttingJob Record]
        """
        try:
            logging.info("executing get_paper_cutting_job_controller function")
            return self.CRUDPaperCuttingJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_paper_cutting_job_controller function: {error}")
            raise error

    def delete_paper_cutting_job_controller(self, job_id: int):
        """[Controller to delete a PaperCuttingJob]

        Args:
            job_id (int): [Unique Identifier for a PaperCuttingJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted PaperCuttingJob details]
        """
        try:
            logging.info("executing delete_paper_cutting_job_controller function")
            return self.CRUDPaperCuttingJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_paper_cutting_job_controller function: {error}")
            raise error
