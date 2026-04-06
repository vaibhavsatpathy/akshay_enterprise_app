from sql import logger
from sql.crud.block_types_crud import CRUDBlockType

logging = logger(__name__)


class BlockTypeController:
    def __init__(self):
        self.CRUDBlockType = CRUDBlockType()

    def create_block_type_controller(self, request):
        """[Create a BlockType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BlockType Data]
        """
        try:
            logging.info("executing create_block_type_controller function")
            create_block_type_request = request.dict(exclude_none=True)
            self.CRUDBlockType.create(**create_block_type_request)
            return create_block_type_request
        except Exception as error:
            logging.error(f"Error in create_block_type_controller function: {error}")
            raise error

    def update_block_type_controller(self, request):
        """[Update a BlockType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BlockType Data]
        """
        try:
            logging.info("executing update_block_type_controller function")
            update_block_type_request = request.dict(exclude_none=True)
            self.CRUDBlockType.update(**update_block_type_request)
            return update_block_type_request
        except Exception as error:
            logging.error(f"Error in update_block_type_controller function: {error}")
            raise error

    def get_all_block_type_controller(self):
        """[Get All BlockType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all BlockType Records]
        """
        try:
            logging.info("executing get_all_block_type_controller function")
            return self.CRUDBlockType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_block_type_controller function: {error}")
            raise error

    def get_block_type_controller(self, block_type_id: int):
        """[Get a BlockType record Controller]

        Args:
            block_type_id (int): [Unique Identifier for a BlockType]

        Raises:
            error: [Error]

        Returns:
            [type]: [BlockType Record]
        """
        try:
            logging.info("executing get_block_type_controller function")
            return self.CRUDBlockType.read(block_type_id=block_type_id)
        except Exception as error:
            logging.error(f"Error in get_block_type_controller function: {error}")
            raise error

    def delete_block_type_controller(self, block_type_id: int):
        """[Controller to delete a BlockType]

        Args:
            block_type_id (int): [Unique Identifier for a BlockType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted BlockType details]
        """
        try:
            logging.info("executing delete_block_type_controller function")
            return self.CRUDBlockType.delete(block_type_id=block_type_id)
        except Exception as error:
            logging.error(f"Error in delete_block_type_controller function: {error}")
            raise error
