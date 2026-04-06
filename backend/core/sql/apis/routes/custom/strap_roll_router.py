from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.strap_roll_request import StrapRollCreate, StrapRollUpdate
from sql.apis.schemas.responses.custom.strap_roll_response import StrapRollResponse
from sql.controllers.custom.strap_roll_controller import StrapRollController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
strap_roll_router = APIRouter()


@strap_roll_router.post(
    "/corrugation/strap-roll/create",
    response_model=StrapRollResponse,
)
async def create_strap_roll(
    create_request: StrapRollCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new StrapRoll record]

    Args:
        create_request (StrapRollCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StrapRollResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/strap-roll/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StrapRollController().create_strap_roll_controller(
                request=create_request
            )
            return StrapRollResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/strap-roll/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@strap_roll_router.post(
    "/corrugation/strap-roll/update",
    response_model=StrapRollResponse,
)
async def update_strap_roll(
    update_request: StrapRollUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a StrapRoll record]

    Args:
        update_request (StrapRollUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StrapRollResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/strap-roll/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StrapRollController().update_strap_roll_controller(
                request=update_request
            )
            return StrapRollResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/strap-roll/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@strap_roll_router.get(
    "/corrugation/strap-roll/list_all",
)
async def list_all_strap_roll(
    token: str = Depends(oauth2_scheme),
):
    """[Get all StrapRoll records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/strap-roll/list_all endpoint")
        if decodeJWT(token=token):
            response = StrapRollController().get_all_strap_roll_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/strap-roll/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@strap_roll_router.get(
    "/corrugation/strap-roll/get",
    response_model=StrapRollResponse,
)
async def get_strap_roll(
    roll_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific StrapRoll record]

    Args:
        roll_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StrapRollResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/strap-roll/get endpoint")
        if decodeJWT(token=token):
            response = StrapRollController().get_strap_roll_controller(
                roll_id=roll_id
            )
            return StrapRollResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/strap-roll/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@strap_roll_router.delete("/corrugation/strap-roll/delete")
async def delete_strap_roll(
    roll_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a StrapRoll record]

    Args:
        roll_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/strap-roll/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return StrapRollController().delete_strap_roll_controller(
                roll_id=roll_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/strap-roll/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
