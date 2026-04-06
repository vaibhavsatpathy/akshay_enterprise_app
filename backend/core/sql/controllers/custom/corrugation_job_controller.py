from sql import logger
from sql.crud.corrugation_job_crud import CRUDCorrugationJob

logging = logger(__name__)


class CorrugationJobController:
    def __init__(self):
        self.CRUDCorrugationJob = CRUDCorrugationJob()

    def create_corrugation_job_controller(self, request):
        """[Create a CorrugationJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [CorrugationJob Data]
        """
        try:
            logging.info("executing create_corrugation_job_controller function")
            create_corrugation_job_request = request.dict(exclude_none=True)
            self.CRUDCorrugationJob.create(**create_corrugation_job_request)
            return create_corrugation_job_request
        except Exception as error:
            logging.error(f"Error in create_corrugation_job_controller function: {error}")
            raise error

    def update_corrugation_job_controller(self, request):
        """[Update a CorrugationJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [CorrugationJob Data]
        """
        try:
            logging.info("executing update_corrugation_job_controller function")
            update_corrugation_job_request = request.dict(exclude_none=True)
            self.CRUDCorrugationJob.update(**update_corrugation_job_request)
            return update_corrugation_job_request
        except Exception as error:
            logging.error(f"Error in update_corrugation_job_controller function: {error}")
            raise error

    def get_all_corrugation_job_controller(self):
        """[Get All CorrugationJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all CorrugationJob Records]
        """
        try:
            logging.info("executing get_all_corrugation_job_controller function")
            return self.CRUDCorrugationJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_corrugation_job_controller function: {error}")
            raise error

    def get_corrugation_job_controller(self, job_id: int):
        """[Get a CorrugationJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a CorrugationJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [CorrugationJob Record]
        """
        try:
            logging.info("executing get_corrugation_job_controller function")
            return self.CRUDCorrugationJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_corrugation_job_controller function: {error}")
            raise error

    def delete_corrugation_job_controller(self, job_id: int):
        """[Controller to delete a CorrugationJob]

        Args:
            job_id (int): [Unique Identifier for a CorrugationJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted CorrugationJob details]
        """
        try:
            logging.info("executing delete_corrugation_job_controller function")
            return self.CRUDCorrugationJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_corrugation_job_controller function: {error}")
            raise error
