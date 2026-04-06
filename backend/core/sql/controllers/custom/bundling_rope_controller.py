from sql import logger
from sql.crud.bundling_rope_crud import CRUDBundlingRope

logging = logger(__name__)


class BundlingRopeController:
    def __init__(self):
        self.CRUDBundlingRope = CRUDBundlingRope()

    def create_bundling_rope_controller(self, request):
        """[Create a BundlingRope record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BundlingRope Data]
        """
        try:
            logging.info("executing create_bundling_rope_controller function")
            create_bundling_rope_request = request.dict(exclude_none=True)
            self.CRUDBundlingRope.create(**create_bundling_rope_request)
            return create_bundling_rope_request
        except Exception as error:
            logging.error(f"Error in create_bundling_rope_controller function: {error}")
            raise error

    def update_bundling_rope_controller(self, request):
        """[Update a BundlingRope record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BundlingRope Data]
        """
        try:
            logging.info("executing update_bundling_rope_controller function")
            update_bundling_rope_request = request.dict(exclude_none=True)
            self.CRUDBundlingRope.update(**update_bundling_rope_request)
            return update_bundling_rope_request
        except Exception as error:
            logging.error(f"Error in update_bundling_rope_controller function: {error}")
            raise error

    def get_all_bundling_rope_controller(self):
        """[Get All BundlingRope records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all BundlingRope Records]
        """
        try:
            logging.info("executing get_all_bundling_rope_controller function")
            return self.CRUDBundlingRope.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_bundling_rope_controller function: {error}")
            raise error

    def get_bundling_rope_controller(self, bundle_id: int):
        """[Get a BundlingRope record Controller]

        Args:
            bundle_id (int): [Unique Identifier for a BundlingRope]

        Raises:
            error: [Error]

        Returns:
            [type]: [BundlingRope Record]
        """
        try:
            logging.info("executing get_bundling_rope_controller function")
            return self.CRUDBundlingRope.read(bundle_id=bundle_id)
        except Exception as error:
            logging.error(f"Error in get_bundling_rope_controller function: {error}")
            raise error

    def delete_bundling_rope_controller(self, bundle_id: int):
        """[Controller to delete a BundlingRope]

        Args:
            bundle_id (int): [Unique Identifier for a BundlingRope]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted BundlingRope details]
        """
        try:
            logging.info("executing delete_bundling_rope_controller function")
            return self.CRUDBundlingRope.delete(bundle_id=bundle_id)
        except Exception as error:
            logging.error(f"Error in delete_bundling_rope_controller function: {error}")
            raise error
