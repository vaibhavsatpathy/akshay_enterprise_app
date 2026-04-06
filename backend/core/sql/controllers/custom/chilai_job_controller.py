from sql import logger
from sql.crud.chilai_job_crud import CRUDChilaiJob

logging = logger(__name__)


class ChilaiJobController:
    def __init__(self):
        self.CRUDChilaiJob = CRUDChilaiJob()

    def create_chilai_job_controller(self, request):
        """[Create a ChilaiJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ChilaiJob Data]
        """
        try:
            logging.info("executing create_chilai_job_controller function")
            create_chilai_job_request = request.dict(exclude_none=True)
            self.CRUDChilaiJob.create(**create_chilai_job_request)
            return create_chilai_job_request
        except Exception as error:
            logging.error(f"Error in create_chilai_job_controller function: {error}")
            raise error

    def update_chilai_job_controller(self, request):
        """[Update a ChilaiJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ChilaiJob Data]
        """
        try:
            logging.info("executing update_chilai_job_controller function")
            update_chilai_job_request = request.dict(exclude_none=True)
            self.CRUDChilaiJob.update(**update_chilai_job_request)
            return update_chilai_job_request
        except Exception as error:
            logging.error(f"Error in update_chilai_job_controller function: {error}")
            raise error

    def get_all_chilai_job_controller(self):
        """[Get All ChilaiJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ChilaiJob Records]
        """
        try:
            logging.info("executing get_all_chilai_job_controller function")
            return self.CRUDChilaiJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_chilai_job_controller function: {error}")
            raise error

    def get_chilai_job_controller(self, job_id: int):
        """[Get a ChilaiJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a ChilaiJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [ChilaiJob Record]
        """
        try:
            logging.info("executing get_chilai_job_controller function")
            return self.CRUDChilaiJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_chilai_job_controller function: {error}")
            raise error

    def delete_chilai_job_controller(self, job_id: int):
        """[Controller to delete a ChilaiJob]

        Args:
            job_id (int): [Unique Identifier for a ChilaiJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ChilaiJob details]
        """
        try:
            logging.info("executing delete_chilai_job_controller function")
            return self.CRUDChilaiJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_chilai_job_controller function: {error}")
            raise error
