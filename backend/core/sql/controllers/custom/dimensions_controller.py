from sql import logger
from sql.crud.dimensions_crud import CRUDDimension

logging = logger(__name__)


class DimensionController:
    def __init__(self):
        self.CRUDDimension = CRUDDimension()

    def create_dimension_controller(self, request):
        """[Create a Dimension record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Dimension Data]
        """
        try:
            logging.info("executing create_dimension_controller function")
            create_dimension_request = request.dict(exclude_none=True)
            crud_response = self.CRUDDimension.create(**create_dimension_request)
            return crud_response
        except Exception as error:
            logging.error(f"Error in create_dimension_controller function: {error}")
            raise error

    def update_dimension_controller(self, request):
        """[Update a Dimension record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Dimension Data]
        """
        try:
            logging.info("executing update_dimension_controller function")
            update_dimension_request = request.dict(exclude_none=True)
            self.CRUDDimension.update(**update_dimension_request)
            return update_dimension_request
        except Exception as error:
            logging.error(f"Error in update_dimension_controller function: {error}")
            raise error

    def get_all_dimension_controller(self):
        """[Get All Dimension records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Dimension Records]
        """
        try:
            logging.info("executing get_all_dimension_controller function")
            return self.CRUDDimension.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_dimension_controller function: {error}")
            raise error

    def get_dimension_controller(self, dimension_id: int):
        """[Get a Dimension record Controller]

        Args:
            dimension_id (int): [Unique Identifier for a Dimension]

        Raises:
            error: [Error]

        Returns:
            [type]: [Dimension Record]
        """
        try:
            logging.info("executing get_dimension_controller function")
            return self.CRUDDimension.read(dimension_id=dimension_id)
        except Exception as error:
            logging.error(f"Error in get_dimension_controller function: {error}")
            raise error

    def delete_dimension_controller(self, dimension_id: int):
        """[Controller to delete a Dimension]

        Args:
            dimension_id (int): [Unique Identifier for a Dimension]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Dimension details]
        """
        try:
            logging.info("executing delete_dimension_controller function")
            return self.CRUDDimension.delete(dimension_id=dimension_id)
        except Exception as error:
            logging.error(f"Error in delete_dimension_controller function: {error}")
            raise error
