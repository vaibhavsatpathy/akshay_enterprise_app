from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.die_request import DieCreate, DieUpdate
from sql.apis.schemas.responses.custom.die_response import DieResponse
from sql.controllers.custom.die_controller import DieController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
die_router = APIRouter()


@die_router.post(
    "/corrugation/die/create",
    response_model=DieResponse,
)
async def create_die(
    create_request: DieCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Die record]

    Args:
        create_request (DieCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DieResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/die/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = DieController().create_die_controller(
                request=create_request
            )
            return DieResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@die_router.post(
    "/corrugation/die/update",
    response_model=DieResponse,
)
async def update_die(
    update_request: DieUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Die record]

    Args:
        update_request (DieUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DieResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/die/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = DieController().update_die_controller(
                request=update_request
            )
            return DieResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@die_router.get(
    "/corrugation/die/list_all",
)
async def list_all_die(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Die records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/die/list_all endpoint")
        if decodeJWT(token=token):
            response = DieController().get_all_die_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@die_router.get(
    "/corrugation/die/get",
    response_model=DieResponse,
)
async def get_die(
    die_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Die record]

    Args:
        die_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DieResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/die/get endpoint")
        if decodeJWT(token=token):
            response = DieController().get_die_controller(
                die_id=die_id
            )
            return DieResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@die_router.delete("/corrugation/die/delete")
async def delete_die(
    die_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Die record]

    Args:
        die_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/die/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return DieController().delete_die_controller(
                die_id=die_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
