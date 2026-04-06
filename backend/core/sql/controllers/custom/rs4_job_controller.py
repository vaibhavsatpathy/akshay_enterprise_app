from sql import logger
from sql.crud.rs4_job_crud import CRUDRs4Job

logging = logger(__name__)


class Rs4JobController:
    def __init__(self):
        self.CRUDRs4Job = CRUDRs4Job()

    def create_rs4_job_controller(self, request):
        """[Create a Rs4Job record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Rs4Job Data]
        """
        try:
            logging.info("executing create_rs4_job_controller function")
            create_rs4_job_request = request.dict(exclude_none=True)
            self.CRUDRs4Job.create(**create_rs4_job_request)
            return create_rs4_job_request
        except Exception as error:
            logging.error(f"Error in create_rs4_job_controller function: {error}")
            raise error

    def update_rs4_job_controller(self, request):
        """[Update a Rs4Job record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Rs4Job Data]
        """
        try:
            logging.info("executing update_rs4_job_controller function")
            update_rs4_job_request = request.dict(exclude_none=True)
            self.CRUDRs4Job.update(**update_rs4_job_request)
            return update_rs4_job_request
        except Exception as error:
            logging.error(f"Error in update_rs4_job_controller function: {error}")
            raise error

    def get_all_rs4_job_controller(self):
        """[Get All Rs4Job records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Rs4Job Records]
        """
        try:
            logging.info("executing get_all_rs4_job_controller function")
            return self.CRUDRs4Job.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_rs4_job_controller function: {error}")
            raise error

    def get_rs4_job_controller(self, job_id: int):
        """[Get a Rs4Job record Controller]

        Args:
            job_id (int): [Unique Identifier for a Rs4Job]

        Raises:
            error: [Error]

        Returns:
            [type]: [Rs4Job Record]
        """
        try:
            logging.info("executing get_rs4_job_controller function")
            return self.CRUDRs4Job.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_rs4_job_controller function: {error}")
            raise error

    def delete_rs4_job_controller(self, job_id: int):
        """[Controller to delete a Rs4Job]

        Args:
            job_id (int): [Unique Identifier for a Rs4Job]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Rs4Job details]
        """
        try:
            logging.info("executing delete_rs4_job_controller function")
            return self.CRUDRs4Job.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_rs4_job_controller function: {error}")
            raise error
