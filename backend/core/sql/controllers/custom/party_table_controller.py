from sql import logger
from sql.crud.party_table_crud import CRUDParty

logging = logger(__name__)


class PartyController:
    def __init__(self):
        self.CRUDParty = CRUDParty()

    def create_party_controller(self, request):
        """[Create a Party record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Party Data]
        """
        try:
            logging.info("executing create_party_controller function")
            create_party_request = request.dict(exclude_none=True)
            crud_respose = self.CRUDParty.create(**create_party_request)
            return crud_respose
        except Exception as error:
            logging.error(f"Error in create_party_controller function: {error}")
            raise error

    def update_party_controller(self, request):
        """[Update a Party record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Party Data]
        """
        try:
            logging.info("executing update_party_controller function")
            update_party_request = request.dict(exclude_none=True)
            self.CRUDParty.update(**update_party_request)
            return update_party_request
        except Exception as error:
            logging.error(f"Error in update_party_controller function: {error}")
            raise error

    def get_all_party_controller(self):
        """[Get All Party records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all Party Records]
        """
        try:
            logging.info("executing get_all_party_controller function")
            return self.CRUDParty.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_party_controller function: {error}")
            raise error

    def get_party_controller(self, party_id: int):
        """[Get a Party record Controller]

        Args:
            party_id (int): [Unique Identifier for a Party]

        Raises:
            error: [Error]

        Returns:
            [type]: [Party Record]
        """
        try:
            logging.info("executing get_party_controller function")
            return self.CRUDParty.read(party_id=party_id)
        except Exception as error:
            logging.error(f"Error in get_party_controller function: {error}")
            raise error

    def delete_party_controller(self, party_id: int):
        """[Controller to delete a Party]

        Args:
            party_id (int): [Unique Identifier for a Party]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted Party details]
        """
        try:
            logging.info("executing delete_party_controller function")
            return self.CRUDParty.delete(party_id=party_id)
        except Exception as error:
            logging.error(f"Error in delete_party_controller function: {error}")
            raise error
