from sql import logger
from sql.crud.gst_config_crud import CRUDGstConfig

logging = logger(__name__)


class GstConfigController:
    def __init__(self):
        self.CRUDGstConfig = CRUDGstConfig()

    def create_gst_config_controller(self, request):
        """[Create a GstConfig record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [GstConfig Data]
        """
        try:
            logging.info("executing create_gst_config_controller function")
            create_gst_config_request = request.dict(exclude_none=True)
            self.CRUDGstConfig.create(**create_gst_config_request)
            return create_gst_config_request
        except Exception as error:
            logging.error(f"Error in create_gst_config_controller function: {error}")
            raise error

    def update_gst_config_controller(self, request):
        """[Update a GstConfig record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [GstConfig Data]
        """
        try:
            logging.info("executing update_gst_config_controller function")
            update_gst_config_request = request.dict(exclude_none=True)
            self.CRUDGstConfig.update(**update_gst_config_request)
            return update_gst_config_request
        except Exception as error:
            logging.error(f"Error in update_gst_config_controller function: {error}")
            raise error

    def get_all_gst_config_controller(self):
        """[Get All GstConfig records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all GstConfig Records]
        """
        try:
            logging.info("executing get_all_gst_config_controller function")
            return self.CRUDGstConfig.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_gst_config_controller function: {error}")
            raise error

    def get_gst_config_controller(self, gst_config_id: int):
        """[Get a GstConfig record Controller]

        Args:
            gst_config_id (int): [Unique Identifier for a GstConfig]

        Raises:
            error: [Error]

        Returns:
            [type]: [GstConfig Record]
        """
        try:
            logging.info("executing get_gst_config_controller function")
            return self.CRUDGstConfig.read(gst_config_id=gst_config_id)
        except Exception as error:
            logging.error(f"Error in get_gst_config_controller function: {error}")
            raise error

    def delete_gst_config_controller(self, gst_config_id: int):
        """[Controller to delete a GstConfig]

        Args:
            gst_config_id (int): [Unique Identifier for a GstConfig]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted GstConfig details]
        """
        try:
            logging.info("executing delete_gst_config_controller function")
            return self.CRUDGstConfig.delete(gst_config_id=gst_config_id)
        except Exception as error:
            logging.error(f"Error in delete_gst_config_controller function: {error}")
            raise error
