from sql import logger
from sql.crud.layer_types_crud import CRUDLayerType

logging = logger(__name__)


class LayerTypeController:
    def __init__(self):
        self.CRUDLayerType = CRUDLayerType()

    def create_layer_type_controller(self, request):
        """[Create a LayerType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [LayerType Data]
        """
        try:
            logging.info("executing create_layer_type_controller function")
            create_layer_type_request = request.dict(exclude_none=True)
            self.CRUDLayerType.create(**create_layer_type_request)
            return create_layer_type_request
        except Exception as error:
            logging.error(f"Error in create_layer_type_controller function: {error}")
            raise error

    def update_layer_type_controller(self, request):
        """[Update a LayerType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [LayerType Data]
        """
        try:
            logging.info("executing update_layer_type_controller function")
            update_layer_type_request = request.dict(exclude_none=True)
            self.CRUDLayerType.update(**update_layer_type_request)
            return update_layer_type_request
        except Exception as error:
            logging.error(f"Error in update_layer_type_controller function: {error}")
            raise error

    def get_all_layer_type_controller(self):
        """[Get All LayerType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all LayerType Records]
        """
        try:
            logging.info("executing get_all_layer_type_controller function")
            return self.CRUDLayerType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_layer_type_controller function: {error}")
            raise error

    def get_layer_type_controller(self, layer_type_id: int):
        """[Get a LayerType record Controller]

        Args:
            layer_type_id (int): [Unique Identifier for a LayerType]

        Raises:
            error: [Error]

        Returns:
            [type]: [LayerType Record]
        """
        try:
            logging.info("executing get_layer_type_controller function")
            return self.CRUDLayerType.read(layer_type_id=layer_type_id)
        except Exception as error:
            logging.error(f"Error in get_layer_type_controller function: {error}")
            raise error

    def delete_layer_type_controller(self, layer_type_id: int):
        """[Controller to delete a LayerType]

        Args:
            layer_type_id (int): [Unique Identifier for a LayerType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted LayerType details]
        """
        try:
            logging.info("executing delete_layer_type_controller function")
            return self.CRUDLayerType.delete(layer_type_id=layer_type_id)
        except Exception as error:
            logging.error(f"Error in delete_layer_type_controller function: {error}")
            raise error
