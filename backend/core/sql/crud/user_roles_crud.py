from sql import session, logger
from sql.orm_models.user_roles import UserRole

logging = logger(__name__)


class CRUDUserRole:
    def create(self, **kwargs):
        """[CRUD function to create a new UserRole record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDUserRole create request")
            user_role = UserRole(**kwargs)
            with session() as transaction_session:
                transaction_session.add(user_role)
                transaction_session.commit()
                transaction_session.refresh(user_role)
            return user_role.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDUserRole create function : {error}")
            raise error

    def read(self, role_id: int):
        """[CRUD function to read UserRole records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [user role records]
        """
        try:
            logging.info("CRUDUserRole read request")
            with session() as transaction_session:
                obj: UserRole = (
                    transaction_session.query(UserRole)
                    .filter(UserRole.role_id == role_id)
                    .first()
                )
            if obj is not None:
                return obj.__dict__
            else:
                return None
        except Exception as error:
            logging.error(f"Error in CRUDUserRole read function : {error}")
            raise error

    def read_by_role(self, role_name: str):
        """[CRUD function to read UserRole records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [user role records]
        """
        try:
            logging.info("CRUDUserRole read request")
            with session() as transaction_session:
                obj: UserRole = (
                    transaction_session.query(UserRole)
                    .filter(UserRole.role_name == role_name)
                    .first()
                )
            if obj is not None:
                return obj.__dict__
            else:
                return None
        except Exception as error:
            logging.error(f"Error in CRUDUserRole read function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read all User role records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all user role records]
        """
        try:
            logging.info("CRUDUserRole read_all request")
            with session() as transaction_session:
                obj: UserRole = transaction_session.query(UserRole).all()
            if obj is not None:
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            logging.error(f"Error in CRUDUserRole read_all function : {error}")
            raise error

    def update(self, **kwargs):
        """[CRUD function to update a UserRole record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDUserRole update request")
            with session() as transaction_session:
                obj: UserRole = (
                    transaction_session.query(UserRole)
                    .filter(UserRole.role_name == kwargs.get("role_name"))
                    .update(kwargs, synchronize_session=False)
                )
            transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDUserRole update function : {error}")
            raise error

    def delete(self, role_id: int):
        """[CRUD function to delete a UserRole record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDUserRole deletee request")
            with session() as transaction_session:
                obj: UserRole = (
                    transaction_session.query(UserRole)
                    .filter(UserRole.role_id == role_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDUserRole delete function : {error}")
            raise error
