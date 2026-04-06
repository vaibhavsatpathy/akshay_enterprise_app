from datetime import datetime

from sql import session, logger
from sql.orm_models.party_table import Party

logging = logger(__name__)


class CRUDParty:
    def create(self, **kwargs):
        try:
            logging.info("CRUDParty create request")
            party = Party(**kwargs)
            party.created_at = datetime.now()
            party.updated_at = datetime.now()
            with session() as transaction_session:
                transaction_session.add(party)
                transaction_session.commit()
                transaction_session.refresh(party)
            return party.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDParty create function : {error}")
            raise error

    def read(self, party_id: int):
        try:
            logging.info("CRUDParty read request")
            with session() as transaction_session:
                obj: Party = (
                    transaction_session.query(Party)
                    .filter(Party.party_id == party_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDParty read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDParty read_all request")
            with session() as transaction_session:
                obj: Party = transaction_session.query(Party).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDParty read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDParty update request")
            with session() as transaction_session:
                transaction_session.query(Party).filter(
                    Party.party_id == kwargs.get("party_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDParty update function : {error}")
            raise error

    def delete(self, party_id: int):
        try:
            logging.info("CRUDParty delete request")
            with session() as transaction_session:
                obj: Party = (
                    transaction_session.query(Party)
                    .filter(Party.party_id == party_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDParty delete function : {error}")
            raise error
