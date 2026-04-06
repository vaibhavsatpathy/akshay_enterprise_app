from sql import logger
from sql.crud.shades_crud import CRUDShade

logging = logger(__name__)


class ShadeController:
    def __init__(self):
        self.CRUDShade = CRUDShade()

    def create_shade_controller(self, request):
        """[Create a Shade record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Shade Data]
        """
        try:
            logging.info("executing create_shade_controller function")
            create_shade_request = request.dict(exclude_none=True)
            crud_response = self.CRUDShade.create(**create_shade_request)
            return crud_response
        except Exception as error:
            logging.error(f"Error in create_shade_controller function: {error}")
            raise error

    def update_shade_controller(self, request):
        """[Update a Shade record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Shade Data]
        """
        try:
            logging.info("executing update_shade_controller function")
            update_shade_request = request.dict(exclude_none=True)
            self.CRUDShade.update(**update_shade_request)
            return update_shade_request
        except Exception as error:
            logging.error(f"Error in update_shade_controller function: {error}")
            raise error

    def get_all_shade_controller(self):
        """[Get All Shade records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Shade Records]
        """
        try:
            logging.info("executing get_all_shade_controller function")
            return self.CRUDShade.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_shade_controller function: {error}")
            raise error

    def get_shade_controller(self, shade_id: int):
        """[Get a Shade record Controller]

        Args:
            shade_id (int): [Unique Identifier for a Shade]

        Raises:
            error: [Error]

        Returns:
            [type]: [Shade Record]
        """
        try:
            logging.info("executing get_shade_controller function")
            return self.CRUDShade.read(shade_id=shade_id)
        except Exception as error:
            logging.error(f"Error in get_shade_controller function: {error}")
            raise error

    def delete_shade_controller(self, shade_id: int):
        """[Controller to delete a Shade]

        Args:
            shade_id (int): [Unique Identifier for a Shade]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Shade details]
        """
        try:
            logging.info("executing delete_shade_controller function")
            return self.CRUDShade.delete(shade_id=shade_id)
        except Exception as error:
            logging.error(f"Error in delete_shade_controller function: {error}")
            raise error
