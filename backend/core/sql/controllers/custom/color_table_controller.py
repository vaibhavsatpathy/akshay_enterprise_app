from sql import logger
from sql.crud.color_table_crud import CRUDColorTable

logging = logger(__name__)


class ColorTableController:
    def __init__(self):
        self.CRUDColorTable = CRUDColorTable()

    def create_color_table_controller(self, request):
        """[Create a ColorTable record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ColorTable Data]
        """
        try:
            logging.info("executing create_color_table_controller function")
            create_color_table_request = request.dict(exclude_none=True)
            self.CRUDColorTable.create(**create_color_table_request)
            return create_color_table_request
        except Exception as error:
            logging.error(f"Error in create_color_table_controller function: {error}")
            raise error

    def update_color_table_controller(self, request):
        """[Update a ColorTable record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [ColorTable Data]
        """
        try:
            logging.info("executing update_color_table_controller function")
            update_color_table_request = request.dict(exclude_none=True)
            self.CRUDColorTable.update(**update_color_table_request)
            return update_color_table_request
        except Exception as error:
            logging.error(f"Error in update_color_table_controller function: {error}")
            raise error

    def get_all_color_table_controller(self):
        """[Get All ColorTable records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all ColorTable Records]
        """
        try:
            logging.info("executing get_all_color_table_controller function")
            return self.CRUDColorTable.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_color_table_controller function: {error}")
            raise error

    def get_color_table_controller(self, color_id: int):
        """[Get a ColorTable record Controller]

        Args:
            color_id (int): [Unique Identifier for a ColorTable]

        Raises:
            error: [Error]

        Returns:
            [type]: [ColorTable Record]
        """
        try:
            logging.info("executing get_color_table_controller function")
            return self.CRUDColorTable.read(color_id=color_id)
        except Exception as error:
            logging.error(f"Error in get_color_table_controller function: {error}")
            raise error

    def delete_color_table_controller(self, color_id: int):
        """[Controller to delete a ColorTable]

        Args:
            color_id (int): [Unique Identifier for a ColorTable]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted ColorTable details]
        """
        try:
            logging.info("executing delete_color_table_controller function")
            return self.CRUDColorTable.delete(color_id=color_id)
        except Exception as error:
            logging.error(f"Error in delete_color_table_controller function: {error}")
            raise error
