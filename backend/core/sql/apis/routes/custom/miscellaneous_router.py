from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.miscellaneous_request import MiscellaneousCreate, MiscellaneousUpdate
from sql.apis.schemas.responses.custom.miscellaneous_response import MiscellaneousResponse
from sql.controllers.custom.miscellaneous_controller import MiscellaneousController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
miscellaneous_router = APIRouter()


@miscellaneous_router.post(
    "/corrugation/miscellaneous/create",
    response_model=MiscellaneousResponse,
)
async def create_miscellaneous(
    create_request: MiscellaneousCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Miscellaneous record]

    Args:
        create_request (MiscellaneousCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [MiscellaneousResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/miscellaneous/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = MiscellaneousController().create_miscellaneous_controller(
                request=create_request
            )
            return MiscellaneousResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/miscellaneous/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@miscellaneous_router.post(
    "/corrugation/miscellaneous/update",
    response_model=MiscellaneousResponse,
)
async def update_miscellaneous(
    update_request: MiscellaneousUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Miscellaneous record]

    Args:
        update_request (MiscellaneousUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [MiscellaneousResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/miscellaneous/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = MiscellaneousController().update_miscellaneous_controller(
                request=update_request
            )
            return MiscellaneousResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/miscellaneous/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@miscellaneous_router.get(
    "/corrugation/miscellaneous/list_all",
)
async def list_all_miscellaneous(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Miscellaneous records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/miscellaneous/list_all endpoint")
        if decodeJWT(token=token):
            response = MiscellaneousController().get_all_miscellaneous_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/miscellaneous/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@miscellaneous_router.get(
    "/corrugation/miscellaneous/get",
    response_model=MiscellaneousResponse,
)
async def get_miscellaneous(
    misc_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Miscellaneous record]

    Args:
        misc_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [MiscellaneousResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/miscellaneous/get endpoint")
        if decodeJWT(token=token):
            response = MiscellaneousController().get_miscellaneous_controller(
                misc_id=misc_id
            )
            return MiscellaneousResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/miscellaneous/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@miscellaneous_router.delete("/corrugation/miscellaneous/delete")
async def delete_miscellaneous(
    misc_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Miscellaneous record]

    Args:
        misc_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/miscellaneous/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return MiscellaneousController().delete_miscellaneous_controller(
                misc_id=misc_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/miscellaneous/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
