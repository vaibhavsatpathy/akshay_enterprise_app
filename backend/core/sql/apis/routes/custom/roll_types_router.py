from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.roll_types_request import RollTypeCreate, RollTypeUpdate
from sql.apis.schemas.responses.custom.roll_types_response import RollTypeResponse
from sql.controllers.custom.roll_types_controller import RollTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
roll_types_router = APIRouter()


@roll_types_router.post(
    "/corrugation/roll-types/create",
    response_model=RollTypeResponse,
)
async def create_roll_type(
    create_request: RollTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new RollType record]

    Args:
        create_request (RollTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RollTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/roll-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = RollTypeController().create_roll_type_controller(
                request=create_request
            )
            return RollTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/roll-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@roll_types_router.post(
    "/corrugation/roll-types/update",
    response_model=RollTypeResponse,
)
async def update_roll_type(
    update_request: RollTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a RollType record]

    Args:
        update_request (RollTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RollTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/roll-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = RollTypeController().update_roll_type_controller(
                request=update_request
            )
            return RollTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/roll-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@roll_types_router.get(
    "/corrugation/roll-types/list_all",
)
async def list_all_roll_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all RollType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/roll-types/list_all endpoint")
        if decodeJWT(token=token):
            response = RollTypeController().get_all_roll_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/roll-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@roll_types_router.get(
    "/corrugation/roll-types/get",
    response_model=RollTypeResponse,
)
async def get_roll_type(
    roll_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific RollType record]

    Args:
        roll_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RollTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/roll-types/get endpoint")
        if decodeJWT(token=token):
            response = RollTypeController().get_roll_type_controller(
                roll_type_id=roll_type_id
            )
            return RollTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/roll-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@roll_types_router.delete("/corrugation/roll-types/delete")
async def delete_roll_type(
    roll_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a RollType record]

    Args:
        roll_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/roll-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return RollTypeController().delete_roll_type_controller(
                roll_type_id=roll_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/roll-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
