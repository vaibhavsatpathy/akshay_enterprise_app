from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.plate_sizes_request import PlateSizeCreate, PlateSizeUpdate
from sql.apis.schemas.responses.custom.plate_sizes_response import PlateSizeResponse
from sql.controllers.custom.plate_sizes_controller import PlateSizeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
plate_sizes_router = APIRouter()


@plate_sizes_router.post(
    "/corrugation/plate-sizes/create",
    response_model=PlateSizeResponse,
)
async def create_plate_size(
    create_request: PlateSizeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new PlateSize record]

    Args:
        create_request (PlateSizeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PlateSizeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/plate-sizes/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PlateSizeController().create_plate_size_controller(
                request=create_request
            )
            return PlateSizeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-sizes/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@plate_sizes_router.post(
    "/corrugation/plate-sizes/update",
    response_model=PlateSizeResponse,
)
async def update_plate_size(
    update_request: PlateSizeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a PlateSize record]

    Args:
        update_request (PlateSizeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PlateSizeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/plate-sizes/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PlateSizeController().update_plate_size_controller(
                request=update_request
            )
            return PlateSizeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-sizes/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@plate_sizes_router.get(
    "/corrugation/plate-sizes/list_all",
)
async def list_all_plate_size(
    token: str = Depends(oauth2_scheme),
):
    """[Get all PlateSize records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/plate-sizes/list_all endpoint")
        if decodeJWT(token=token):
            response = PlateSizeController().get_all_plate_size_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-sizes/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@plate_sizes_router.get(
    "/corrugation/plate-sizes/get",
    response_model=PlateSizeResponse,
)
async def get_plate_size(
    plate_size_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific PlateSize record]

    Args:
        plate_size_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PlateSizeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/plate-sizes/get endpoint")
        if decodeJWT(token=token):
            response = PlateSizeController().get_plate_size_controller(
                plate_size_id=plate_size_id
            )
            return PlateSizeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-sizes/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@plate_sizes_router.delete("/corrugation/plate-sizes/delete")
async def delete_plate_size(
    plate_size_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a PlateSize record]

    Args:
        plate_size_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/plate-sizes/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PlateSizeController().delete_plate_size_controller(
                plate_size_id=plate_size_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-sizes/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
