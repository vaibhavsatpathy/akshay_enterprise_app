from datetime import datetime
from sql import session, logger
from sql.orm_models.inventory import Inventory

logging = logger(__name__)


class CRUDInventory:
    def create(self, **kwargs):
        try:
            logging.info("CRUDInventory create request")
            inventory = Inventory(**kwargs)
            inventory.created_at = datetime.now()
            inventory.updated_at = datetime.now()
            with session() as transaction_session:
                transaction_session.add(inventory)
                transaction_session.commit()
                transaction_session.refresh(inventory)
            return inventory.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDInventory create function : {error}")
            raise error

    def read(self, inventory_id: int):
        try:
            logging.info("CRUDInventory read request")
            with session() as transaction_session:
                obj: Inventory = (
                    transaction_session.query(Inventory)
                    .filter(Inventory.inventory_id == inventory_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDInventory read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDInventory read_all request")
            with session() as transaction_session:
                obj: Inventory = transaction_session.query(Inventory).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDInventory read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDInventory update request")
            with session() as transaction_session:
                transaction_session.query(Inventory).filter(
                    Inventory.inventory_id == kwargs.get("inventory_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDInventory update function : {error}")
            raise error

    def delete(self, inventory_id: int):
        try:
            logging.info("CRUDInventory delete request")
            with session() as transaction_session:
                obj: Inventory = (
                    transaction_session.query(Inventory)
                    .filter(Inventory.inventory_id == inventory_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDInventory delete function : {error}")
            raise error
