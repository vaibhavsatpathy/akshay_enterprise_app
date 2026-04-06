from sql import logger
from sql.crud.single_two_pieces_type_crud import CRUDSingleTwoPiecesType

logging = logger(__name__)


class SingleTwoPiecesTypeController:
    def __init__(self):
        self.CRUDSingleTwoPiecesType = CRUDSingleTwoPiecesType()

    def create_single_two_pieces_type_controller(self, request):
        """[Create a SingleTwoPiecesType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [SingleTwoPiecesType Data]
        """
        try:
            logging.info("executing create_single_two_pieces_type_controller function")
            create_single_two_pieces_type_request = request.dict(exclude_none=True)
            self.CRUDSingleTwoPiecesType.create(**create_single_two_pieces_type_request)
            return create_single_two_pieces_type_request
        except Exception as error:
            logging.error(f"Error in create_single_two_pieces_type_controller function: {error}")
            raise error

    def update_single_two_pieces_type_controller(self, request):
        """[Update a SingleTwoPiecesType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [SingleTwoPiecesType Data]
        """
        try:
            logging.info("executing update_single_two_pieces_type_controller function")
            update_single_two_pieces_type_request = request.dict(exclude_none=True)
            self.CRUDSingleTwoPiecesType.update(**update_single_two_pieces_type_request)
            return update_single_two_pieces_type_request
        except Exception as error:
            logging.error(f"Error in update_single_two_pieces_type_controller function: {error}")
            raise error

    def get_all_single_two_pieces_type_controller(self):
        """[Get All SingleTwoPiecesType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all SingleTwoPiecesType Records]
        """
        try:
            logging.info("executing get_all_single_two_pieces_type_controller function")
            return self.CRUDSingleTwoPiecesType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_single_two_pieces_type_controller function: {error}")
            raise error

    def get_single_two_pieces_type_controller(self, single_two_pieces_type_id: int):
        """[Get a SingleTwoPiecesType record Controller]

        Args:
            single_two_pieces_type_id (int): [Unique Identifier for a SingleTwoPiecesType]

        Raises:
            error: [Error]

        Returns:
            [type]: [SingleTwoPiecesType Record]
        """
        try:
            logging.info("executing get_single_two_pieces_type_controller function")
            return self.CRUDSingleTwoPiecesType.read(single_two_pieces_type_id=single_two_pieces_type_id)
        except Exception as error:
            logging.error(f"Error in get_single_two_pieces_type_controller function: {error}")
            raise error

    def delete_single_two_pieces_type_controller(self, single_two_pieces_type_id: int):
        """[Controller to delete a SingleTwoPiecesType]

        Args:
            single_two_pieces_type_id (int): [Unique Identifier for a SingleTwoPiecesType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted SingleTwoPiecesType details]
        """
        try:
            logging.info("executing delete_single_two_pieces_type_controller function")
            return self.CRUDSingleTwoPiecesType.delete(single_two_pieces_type_id=single_two_pieces_type_id)
        except Exception as error:
            logging.error(f"Error in delete_single_two_pieces_type_controller function: {error}")
            raise error
