from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.file_placing_request import FilePlacingCreate, FilePlacingUpdate
from sql.apis.schemas.responses.custom.file_placing_response import FilePlacingResponse
from sql.controllers.custom.file_placing_controller import FilePlacingController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
file_placing_router = APIRouter()


@file_placing_router.post(
    "/corrugation/file-placing/create",
    response_model=FilePlacingResponse,
)
async def create_file_placing(
    create_request: FilePlacingCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new FilePlacing record]

    Args:
        create_request (FilePlacingCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [FilePlacingResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/file-placing/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = FilePlacingController().create_file_placing_controller(
                request=create_request
            )
            return FilePlacingResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-placing/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@file_placing_router.post(
    "/corrugation/file-placing/update",
    response_model=FilePlacingResponse,
)
async def update_file_placing(
    update_request: FilePlacingUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a FilePlacing record]

    Args:
        update_request (FilePlacingUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [FilePlacingResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/file-placing/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = FilePlacingController().update_file_placing_controller(
                request=update_request
            )
            return FilePlacingResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-placing/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@file_placing_router.get(
    "/corrugation/file-placing/list_all",
)
async def list_all_file_placing(
    token: str = Depends(oauth2_scheme),
):
    """[Get all FilePlacing records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/file-placing/list_all endpoint")
        if decodeJWT(token=token):
            response = FilePlacingController().get_all_file_placing_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-placing/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@file_placing_router.get(
    "/corrugation/file-placing/get",
    response_model=FilePlacingResponse,
)
async def get_file_placing(
    file_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific FilePlacing record]

    Args:
        file_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [FilePlacingResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/file-placing/get endpoint")
        if decodeJWT(token=token):
            response = FilePlacingController().get_file_placing_controller(
                file_id=file_id
            )
            return FilePlacingResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-placing/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@file_placing_router.delete("/corrugation/file-placing/delete")
async def delete_file_placing(
    file_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a FilePlacing record]

    Args:
        file_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/file-placing/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return FilePlacingController().delete_file_placing_controller(
                file_id=file_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-placing/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
