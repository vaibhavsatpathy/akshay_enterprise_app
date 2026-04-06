from sql import logger
from sql.crud.stitching_pin_material_crud import CRUDStitchingPinMaterial

logging = logger(__name__)


class StitchingPinMaterialController:
    def __init__(self):
        self.CRUDStitchingPinMaterial = CRUDStitchingPinMaterial()

    def create_stitching_pin_material_controller(self, request):
        """[Create a StitchingPinMaterial record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingPinMaterial Data]
        """
        try:
            logging.info("executing create_stitching_pin_material_controller function")
            create_stitching_pin_material_request = request.dict(exclude_none=True)
            self.CRUDStitchingPinMaterial.create(**create_stitching_pin_material_request)
            return create_stitching_pin_material_request
        except Exception as error:
            logging.error(f"Error in create_stitching_pin_material_controller function: {error}")
            raise error

    def update_stitching_pin_material_controller(self, request):
        """[Update a StitchingPinMaterial record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingPinMaterial Data]
        """
        try:
            logging.info("executing update_stitching_pin_material_controller function")
            update_stitching_pin_material_request = request.dict(exclude_none=True)
            self.CRUDStitchingPinMaterial.update(**update_stitching_pin_material_request)
            return update_stitching_pin_material_request
        except Exception as error:
            logging.error(f"Error in update_stitching_pin_material_controller function: {error}")
            raise error

    def get_all_stitching_pin_material_controller(self):
        """[Get All StitchingPinMaterial records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all StitchingPinMaterial Records]
        """
        try:
            logging.info("executing get_all_stitching_pin_material_controller function")
            return self.CRUDStitchingPinMaterial.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_stitching_pin_material_controller function: {error}")
            raise error

    def get_stitching_pin_material_controller(self, material_id: int):
        """[Get a StitchingPinMaterial record Controller]

        Args:
            material_id (int): [Unique Identifier for a StitchingPinMaterial]

        Raises:
            error: [Error]

        Returns:
            [type]: [StitchingPinMaterial Record]
        """
        try:
            logging.info("executing get_stitching_pin_material_controller function")
            return self.CRUDStitchingPinMaterial.read(material_id=material_id)
        except Exception as error:
            logging.error(f"Error in get_stitching_pin_material_controller function: {error}")
            raise error

    def delete_stitching_pin_material_controller(self, material_id: int):
        """[Controller to delete a StitchingPinMaterial]

        Args:
            material_id (int): [Unique Identifier for a StitchingPinMaterial]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted StitchingPinMaterial details]
        """
        try:
            logging.info("executing delete_stitching_pin_material_controller function")
            return self.CRUDStitchingPinMaterial.delete(material_id=material_id)
        except Exception as error:
            logging.error(f"Error in delete_stitching_pin_material_controller function: {error}")
            raise error
