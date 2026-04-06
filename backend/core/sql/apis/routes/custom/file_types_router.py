from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.file_types_request import FileTypeCreate, FileTypeUpdate
from sql.apis.schemas.responses.custom.file_types_response import FileTypeResponse
from sql.controllers.custom.file_types_controller import FileTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
file_types_router = APIRouter()


@file_types_router.post(
    "/corrugation/file-types/create",
    response_model=FileTypeResponse,
)
async def create_file_type(
    create_request: FileTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new FileType record]

    Args:
        create_request (FileTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [FileTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/file-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = FileTypeController().create_file_type_controller(
                request=create_request
            )
            return FileTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@file_types_router.post(
    "/corrugation/file-types/update",
    response_model=FileTypeResponse,
)
async def update_file_type(
    update_request: FileTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a FileType record]

    Args:
        update_request (FileTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [FileTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/file-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = FileTypeController().update_file_type_controller(
                request=update_request
            )
            return FileTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@file_types_router.get(
    "/corrugation/file-types/list_all",
)
async def list_all_file_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all FileType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/file-types/list_all endpoint")
        if decodeJWT(token=token):
            response = FileTypeController().get_all_file_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@file_types_router.get(
    "/corrugation/file-types/get",
    response_model=FileTypeResponse,
)
async def get_file_type(
    file_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific FileType record]

    Args:
        file_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [FileTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/file-types/get endpoint")
        if decodeJWT(token=token):
            response = FileTypeController().get_file_type_controller(
                file_type_id=file_type_id
            )
            return FileTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@file_types_router.delete("/corrugation/file-types/delete")
async def delete_file_type(
    file_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a FileType record]

    Args:
        file_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/file-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return FileTypeController().delete_file_type_controller(
                file_type_id=file_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/file-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
