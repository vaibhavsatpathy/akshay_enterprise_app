from sql import logger
from sql.crud.binding_cloth_crud import CRUDBindingCloth

logging = logger(__name__)


class BindingClothController:
    def __init__(self):
        self.CRUDBindingCloth = CRUDBindingCloth()

    def create_binding_cloth_controller(self, request):
        """[Create a BindingCloth record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BindingCloth Data]
        """
        try:
            logging.info("executing create_binding_cloth_controller function")
            create_binding_cloth_request = request.dict(exclude_none=True)
            self.CRUDBindingCloth.create(**create_binding_cloth_request)
            return create_binding_cloth_request
        except Exception as error:
            logging.error(f"Error in create_binding_cloth_controller function: {error}")
            raise error

    def update_binding_cloth_controller(self, request):
        """[Update a BindingCloth record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [BindingCloth Data]
        """
        try:
            logging.info("executing update_binding_cloth_controller function")
            update_binding_cloth_request = request.dict(exclude_none=True)
            self.CRUDBindingCloth.update(**update_binding_cloth_request)
            return update_binding_cloth_request
        except Exception as error:
            logging.error(f"Error in update_binding_cloth_controller function: {error}")
            raise error

    def get_all_binding_cloth_controller(self):
        """[Get All BindingCloth records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all BindingCloth Records]
        """
        try:
            logging.info("executing get_all_binding_cloth_controller function")
            return self.CRUDBindingCloth.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_binding_cloth_controller function: {error}")
            raise error

    def get_binding_cloth_controller(self, cloth_id: int):
        """[Get a BindingCloth record Controller]

        Args:
            cloth_id (int): [Unique Identifier for a BindingCloth]

        Raises:
            error: [Error]

        Returns:
            [type]: [BindingCloth Record]
        """
        try:
            logging.info("executing get_binding_cloth_controller function")
            return self.CRUDBindingCloth.read(cloth_id=cloth_id)
        except Exception as error:
            logging.error(f"Error in get_binding_cloth_controller function: {error}")
            raise error

    def delete_binding_cloth_controller(self, cloth_id: int):
        """[Controller to delete a BindingCloth]

        Args:
            cloth_id (int): [Unique Identifier for a BindingCloth]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted BindingCloth details]
        """
        try:
            logging.info("executing delete_binding_cloth_controller function")
            return self.CRUDBindingCloth.delete(cloth_id=cloth_id)
        except Exception as error:
            logging.error(f"Error in delete_binding_cloth_controller function: {error}")
            raise error
