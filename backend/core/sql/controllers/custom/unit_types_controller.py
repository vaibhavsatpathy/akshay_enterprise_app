from sql import logger
from sql.crud.unit_types_crud import CRUDUnitType

logging = logger(__name__)


class UnitTypeController:
    def __init__(self):
        self.CRUDUnitType = CRUDUnitType()

    def create_unit_type_controller(self, request):
        """[Create a UnitType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [UnitType Data]
        """
        try:
            logging.info("executing create_unit_type_controller function")
            create_unit_type_request = request.dict(exclude_none=True)
            self.CRUDUnitType.create(**create_unit_type_request)
            return create_unit_type_request
        except Exception as error:
            logging.error(f"Error in create_unit_type_controller function: {error}")
            raise error

    def update_unit_type_controller(self, request):
        """[Update a UnitType record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [UnitType Data]
        """
        try:
            logging.info("executing update_unit_type_controller function")
            update_unit_type_request = request.dict(exclude_none=True)
            self.CRUDUnitType.update(**update_unit_type_request)
            return update_unit_type_request
        except Exception as error:
            logging.error(f"Error in update_unit_type_controller function: {error}")
            raise error

    def get_all_unit_type_controller(self):
        """[Get All UnitType records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all UnitType Records]
        """
        try:
            logging.info("executing get_all_unit_type_controller function")
            return self.CRUDUnitType.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_unit_type_controller function: {error}")
            raise error

    def get_unit_type_controller(self, unit_type_id: int):
        """[Get a UnitType record Controller]

        Args:
            unit_type_id (int): [Unique Identifier for a UnitType]

        Raises:
            error: [Error]

        Returns:
            [type]: [UnitType Record]
        """
        try:
            logging.info("executing get_unit_type_controller function")
            return self.CRUDUnitType.read(unit_type_id=unit_type_id)
        except Exception as error:
            logging.error(f"Error in get_unit_type_controller function: {error}")
            raise error

    def delete_unit_type_controller(self, unit_type_id: int):
        """[Controller to delete a UnitType]

        Args:
            unit_type_id (int): [Unique Identifier for a UnitType]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted UnitType details]
        """
        try:
            logging.info("executing delete_unit_type_controller function")
            return self.CRUDUnitType.delete(unit_type_id=unit_type_id)
        except Exception as error:
            logging.error(f"Error in delete_unit_type_controller function: {error}")
            raise error
