from sql import logger
from sql.crud.printing_job_crud import CRUDPrintingJob

logging = logger(__name__)


class PrintingJobController:
    def __init__(self):
        self.CRUDPrintingJob = CRUDPrintingJob()

    def create_printing_job_controller(self, request):
        """[Create a PrintingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintingJob Data]
        """
        try:
            logging.info("executing create_printing_job_controller function")
            create_printing_job_request = request.dict(exclude_none=True)
            self.CRUDPrintingJob.create(**create_printing_job_request)
            return create_printing_job_request
        except Exception as error:
            logging.error(f"Error in create_printing_job_controller function: {error}")
            raise error

    def update_printing_job_controller(self, request):
        """[Update a PrintingJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintingJob Data]
        """
        try:
            logging.info("executing update_printing_job_controller function")
            update_printing_job_request = request.dict(exclude_none=True)
            self.CRUDPrintingJob.update(**update_printing_job_request)
            return update_printing_job_request
        except Exception as error:
            logging.error(f"Error in update_printing_job_controller function: {error}")
            raise error

    def get_all_printing_job_controller(self):
        """[Get All PrintingJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all PrintingJob Records]
        """
        try:
            logging.info("executing get_all_printing_job_controller function")
            return self.CRUDPrintingJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_printing_job_controller function: {error}")
            raise error

    def get_printing_job_controller(self, job_id: int):
        """[Get a PrintingJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a PrintingJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [PrintingJob Record]
        """
        try:
            logging.info("executing get_printing_job_controller function")
            return self.CRUDPrintingJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_printing_job_controller function: {error}")
            raise error

    def delete_printing_job_controller(self, job_id: int):
        """[Controller to delete a PrintingJob]

        Args:
            job_id (int): [Unique Identifier for a PrintingJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted PrintingJob details]
        """
        try:
            logging.info("executing delete_printing_job_controller function")
            return self.CRUDPrintingJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_printing_job_controller function: {error}")
            raise error
