from sql import logger
from sql.crud.paper_types_crud import CRUDPaperType

logging = logger(__name__)


class PaperTypeController:
    def __init__(self):
        self.CRUDPaperType = CRUDPaperType()

    def create_paper_type_controller(self, request):
        """[Create a PaperType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PaperType Data]
        """
        try:
            logging.info("executing create_paper_type_controller function")
            create_paper_type_request = request.dict(exclude_none=True)
            self.CRUDPaperType.create(**create_paper_type_request)
            return create_paper_type_request
        except Exception as error:
            logging.error(f"Error in create_paper_type_controller function: {error}")
            raise error

    def update_paper_type_controller(self, request):
        """[Update a PaperType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [PaperType Data]
        """
        try:
            logging.info("executing update_paper_type_controller function")
            update_paper_type_request = request.dict(exclude_none=True)
            self.CRUDPaperType.update(**update_paper_type_request)
            return update_paper_type_request
        except Exception as error:
            logging.error(f"Error in update_paper_type_controller function: {error}")
            raise error

    def get_all_paper_type_controller(self):
        """[Get All PaperType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all PaperType Records]
        """
        try:
            logging.info("executing get_all_paper_type_controller function")
            return self.CRUDPaperType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_paper_type_controller function: {error}")
            raise error

    def get_paper_type_controller(self, paper_type_id: int):
        """[Get a PaperType record Controller]

        Args:
            paper_type_id (int): [Unique Identifier for a PaperType]

        Raises:
            error: [Error]

        Returns:
            [type]: [PaperType Record]
        """
        try:
            logging.info("executing get_paper_type_controller function")
            return self.CRUDPaperType.read(paper_type_id=paper_type_id)
        except Exception as error:
            logging.error(f"Error in get_paper_type_controller function: {error}")
            raise error

    def delete_paper_type_controller(self, paper_type_id: int):
        """[Controller to delete a PaperType]

        Args:
            paper_type_id (int): [Unique Identifier for a PaperType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted PaperType details]
        """
        try:
            logging.info("executing delete_paper_type_controller function")
            return self.CRUDPaperType.delete(paper_type_id=paper_type_id)
        except Exception as error:
            logging.error(f"Error in delete_paper_type_controller function: {error}")
            raise error
