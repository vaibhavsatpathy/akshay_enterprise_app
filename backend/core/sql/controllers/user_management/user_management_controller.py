from sql.crud.user_crud import CRUDUser
from sql.crud.user_roles_crud import CRUDUserRole
from commons.auth import encrypt_password, verify_hash_password, signJWT
from sql import logger

logging = logger(__name__)


class UserManagementController:
    def __init__(self):
        self.CRUDUser = CRUDUser()
        self.CRUDUserRole = CRUDUserRole()

    def register_user_controller(self, request):
        """[Controller to register new user]

        Args:
            request ([dict]): [create new user request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [authorization details]
        """
        try:
            logging.info("executing register new user function")
            password_hash = encrypt_password(password=request.password)
            user_obj = self.CRUDUser.read(user_name=request.user_name)
            if user_obj is not None:
                return {
                    "access_token": None,
                    "status": "User already exists",
                }
            user_request = {
                "user_name": request.user_name,
                "password": password_hash,
                "full_name": request.full_name,
                "email_id": request.email_id,
                "role_id": request.role_id,
            }
            self.CRUDUser.create(**user_request)
            access_token = signJWT(
                user_name=request.user_name,
                role_name=request.role_name,
                role_id=request.role_id,
            )
            return {
                "access_token": access_token,
                "token_type": "bearer",
            }
        except Exception as error:
            logging.error(f"Error in register_user_controller function: {error}")
            raise error

    def login_user_controller(self, request):
        """[Controller for user login]

        Args:
            request ([dict]): [user login details]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [authorization details]
        """
        try:
            logging.info("executing login user function")
            user_obj = self.CRUDUser.read(user_name=request.username)
            if verify_hash_password(
                plain_password=request.password,
                hashed_password=user_obj.get("password"),
            ):
                # Get role details
                role_obj = self.CRUDUserRole.read(role_id=user_obj.get("role_id"))
                access_token = signJWT(
                    user_name=request.username,
                    role_name=role_obj.get("role_name"),
                    role_id=user_obj.get("role_id"),
                )
                return {
                    "user_name": user_obj.get("user_name"),
                    "email": user_obj.get("email_id"),
                    "name": user_obj.get("full_name"),
                    "access_token": access_token,
                    "token_type": "bearer",
                }
            else:
                return None
        except Exception as error:
            logging.error(f"Error in login_user_controller function: {error}")
            raise error

    def forgot_password_controller(self, request):
        try:
            logging.info("executing forgot password function")
            user_obj = self.CRUDUser.read(user_name=request.user_name)
            password_hash = encrypt_password(password=request.new_password)
            if user_obj:
                update_request = {
                    "user_name": request.user_name,
                    "password": password_hash,
                }
                self.CRUDUser.update(**update_request)
                return {"status": "Password Updated"}
            else:
                return {"status": "Username doesn't exist"}
        except Exception as error:
            logging.error(f"Error in forgot_password_controller function: {error}")
            raise error

    def update_password_controller(self, request):
        try:
            logging.info("executing update password function")
            user_obj = self.CRUDUser.read(user_name=request.user_name)
            password_hash = encrypt_password(password=request.new_password)
            if user_obj:
                if verify_hash_password(
                    plain_password=request.old_password,
                    hashed_password=user_obj.get("password"),
                ):
                    update_request = {
                        "user_name": request.user_name,
                        "password": password_hash,
                    }
                    self.CRUDUser.update(**update_request)
                    return {"status": "Password Updated"}
                else:
                    return {"status": "Current password doesn't match"}
            else:
                return {"status": "Username does not exist"}
        except Exception as error:
            logging.error(f"Error in update_password_controller function: {error}")
            raise error

    def update_user_role_controller(self, request):
        """[Controller to update user role]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [Updated user details]
        """
        try:
            logging.info("executing update_user_role_controller function")
            logging.info("getting user role id")
            role_obj = self.CRUDUserRole.read_by_role(role_name=request.role_name)
            role_id = int(role_obj.get("role_id", 3))
            user_update_request = request.dict(exclude_none=True)
            user_update_request.update({"role_id": role_id})
            self.CRUDUser.update(**user_update_request)
            return user_update_request
        except Exception as error:
            logging.error(f"Error in update_user_role_controller function: {error}")
            raise error

    def delete_user_controller(self, user_name: str):
        """[Controller to delete a user]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted user details]
        """
        try:
            logging.info("executing delete_user_controller function")
            return self.CRUDUser.delete(user_name=user_name)
        except Exception as error:
            logging.error(f"Error in delete_user_controller function: {error}")
            raise {"error": "Invalid username or password"}

    def get_all_users_controller(self):
        """[Controller to get all users]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [list]: [list of all the users in the system]
        """
        try:
            logging.info("executing get_all_users_controller function")
            return self.CRUDUser.read_all()
        except Exception as error:
            logging.error(f"Error in get_all_users_controller function: {error}")
            raise {"error": "Invalid username or password"}

    def get_user_controller(self, user_name: str):
        """[Get User Details]

        Args:
            user_name (str): [Username of the user]

        Returns:
            [dict]: [User details]
        """
        try:
            logging.info("executing get_user_controller function")
            return self.CRUDUser.read(user_name=user_name)
        except Exception as error:
            logging.error(f"Error in get_user_controller function: {error}")
            raise {"error": "Invalid username or password"}
