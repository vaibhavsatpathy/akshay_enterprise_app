from sql import logger
from sql.crud.gum_types_crud import CRUDGumType

logging = logger(__name__)


class GumTypeController:
    def __init__(self):
        self.CRUDGumType = CRUDGumType()

    def create_gum_type_controller(self, request):
        """[Create a GumType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [GumType Data]
        """
        try:
            logging.info("executing create_gum_type_controller function")
            create_gum_type_request = request.dict(exclude_none=True)
            self.CRUDGumType.create(**create_gum_type_request)
            return create_gum_type_request
        except Exception as error:
            logging.error(f"Error in create_gum_type_controller function: {error}")
            raise error

    def update_gum_type_controller(self, request):
        """[Update a GumType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [GumType Data]
        """
        try:
            logging.info("executing update_gum_type_controller function")
            update_gum_type_request = request.dict(exclude_none=True)
            self.CRUDGumType.update(**update_gum_type_request)
            return update_gum_type_request
        except Exception as error:
            logging.error(f"Error in update_gum_type_controller function: {error}")
            raise error

    def get_all_gum_type_controller(self):
        """[Get All GumType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all GumType Records]
        """
        try:
            logging.info("executing get_all_gum_type_controller function")
            return self.CRUDGumType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_gum_type_controller function: {error}")
            raise error

    def get_gum_type_controller(self, gum_type_id: int):
        """[Get a GumType record Controller]

        Args:
            gum_type_id (int): [Unique Identifier for a GumType]

        Raises:
            error: [Error]

        Returns:
            [type]: [GumType Record]
        """
        try:
            logging.info("executing get_gum_type_controller function")
            return self.CRUDGumType.read(gum_type_id=gum_type_id)
        except Exception as error:
            logging.error(f"Error in get_gum_type_controller function: {error}")
            raise error

    def delete_gum_type_controller(self, gum_type_id: int):
        """[Controller to delete a GumType]

        Args:
            gum_type_id (int): [Unique Identifier for a GumType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted GumType details]
        """
        try:
            logging.info("executing delete_gum_type_controller function")
            return self.CRUDGumType.delete(gum_type_id=gum_type_id)
        except Exception as error:
            logging.error(f"Error in delete_gum_type_controller function: {error}")
            raise error
