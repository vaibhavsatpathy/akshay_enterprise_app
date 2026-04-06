from sql import logger
from sql.crud.slot_job_crud import CRUDSlotJob

logging = logger(__name__)


class SlotJobController:
    def __init__(self):
        self.CRUDSlotJob = CRUDSlotJob()

    def create_slot_job_controller(self, request):
        """[Create a SlotJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [SlotJob Data]
        """
        try:
            logging.info("executing create_slot_job_controller function")
            create_slot_job_request = request.dict(exclude_none=True)
            self.CRUDSlotJob.create(**create_slot_job_request)
            return create_slot_job_request
        except Exception as error:
            logging.error(f"Error in create_slot_job_controller function: {error}")
            raise error

    def update_slot_job_controller(self, request):
        """[Update a SlotJob record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [SlotJob Data]
        """
        try:
            logging.info("executing update_slot_job_controller function")
            update_slot_job_request = request.dict(exclude_none=True)
            self.CRUDSlotJob.update(**update_slot_job_request)
            return update_slot_job_request
        except Exception as error:
            logging.error(f"Error in update_slot_job_controller function: {error}")
            raise error

    def get_all_slot_job_controller(self):
        """[Get All SlotJob records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all SlotJob Records]
        """
        try:
            logging.info("executing get_all_slot_job_controller function")
            return self.CRUDSlotJob.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_slot_job_controller function: {error}")
            raise error

    def get_slot_job_controller(self, job_id: int):
        """[Get a SlotJob record Controller]

        Args:
            job_id (int): [Unique Identifier for a SlotJob]

        Raises:
            error: [Error]

        Returns:
            [type]: [SlotJob Record]
        """
        try:
            logging.info("executing get_slot_job_controller function")
            return self.CRUDSlotJob.read(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in get_slot_job_controller function: {error}")
            raise error

    def delete_slot_job_controller(self, job_id: int):
        """[Controller to delete a SlotJob]

        Args:
            job_id (int): [Unique Identifier for a SlotJob]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted SlotJob details]
        """
        try:
            logging.info("executing delete_slot_job_controller function")
            return self.CRUDSlotJob.delete(job_id=job_id)
        except Exception as error:
            logging.error(f"Error in delete_slot_job_controller function: {error}")
            raise error
