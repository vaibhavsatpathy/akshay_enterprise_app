from datetime import datetime

from sql import session, logger
from sql.orm_models.dimensions import Dimension

logging = logger(__name__)


class CRUDDimension:
    def create(self, **kwargs):
        """[CRUD function to create a new Dimension record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDimension create request")
            dimension = Dimension(**kwargs)
            dimension.created_at = datetime.now()
            dimension.updated_at = datetime.now()
            with session() as transaction_session:
                transaction_session.add(dimension)
                transaction_session.commit()
                transaction_session.refresh(dimension)
            return dimension.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDDimension create function : {error}")
            raise error

    def read(self, dimension_id: int):
        """[CRUD function to read a Dimension record]

        Args:
            dimension_id (int): [Dimension ID to filter the record]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [dimension record matching the criteria]
        """
        try:
            logging.info("CRUDDimension read request")
            with session() as transaction_session:
                obj: Dimension = (
                    transaction_session.query(Dimension)
                    .filter(Dimension.dimension_id == dimension_id)
                    .first()
                )
            if obj is not None:
                return obj.__dict__
            else:
                return None
        except Exception as error:
            logging.error(f"Error in CRUDDimension read function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read all Dimension records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all dimension records]
        """
        try:
            logging.info("CRUDDimension read_all request")
            with session() as transaction_session:
                obj: Dimension = transaction_session.query(Dimension).all()
            if obj is not None:
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            logging.error(f"Error in CRUDDimension read_all function : {error}")
            raise error

    def update(self, **kwargs):
        """[CRUD function to update a Dimension record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDimension update request")
            with session() as transaction_session:
                obj: Dimension = (
                    transaction_session.query(Dimension)
                    .filter(Dimension.dimension_id == kwargs.get("dimension_id"))
                    .update(kwargs, synchronize_session=False)
                )
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDDimension update function : {error}")
            raise error

    def delete(self, dimension_id: int):
        """[CRUD function to delete a Dimension record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDimension delete request")
            with session() as transaction_session:
                obj: Dimension = (
                    transaction_session.query(Dimension)
                    .filter(Dimension.dimension_id == dimension_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDDimension delete function : {error}")
            raise error
