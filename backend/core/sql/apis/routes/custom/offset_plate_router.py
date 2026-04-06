from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.offset_plate_request import OffsetPlateCreate, OffsetPlateUpdate
from sql.apis.schemas.responses.custom.offset_plate_response import OffsetPlateResponse
from sql.controllers.custom.offset_plate_controller import OffsetPlateController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
offset_plate_router = APIRouter()


@offset_plate_router.post(
    "/corrugation/offset-plate/create",
    response_model=OffsetPlateResponse,
)
async def create_offset_plate(
    create_request: OffsetPlateCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new OffsetPlate record]

    Args:
        create_request (OffsetPlateCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [OffsetPlateResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/offset-plate/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = OffsetPlateController().create_offset_plate_controller(
                request=create_request
            )
            return OffsetPlateResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/offset-plate/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@offset_plate_router.post(
    "/corrugation/offset-plate/update",
    response_model=OffsetPlateResponse,
)
async def update_offset_plate(
    update_request: OffsetPlateUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a OffsetPlate record]

    Args:
        update_request (OffsetPlateUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [OffsetPlateResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/offset-plate/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = OffsetPlateController().update_offset_plate_controller(
                request=update_request
            )
            return OffsetPlateResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/offset-plate/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@offset_plate_router.get(
    "/corrugation/offset-plate/list_all",
)
async def list_all_offset_plate(
    token: str = Depends(oauth2_scheme),
):
    """[Get all OffsetPlate records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/offset-plate/list_all endpoint")
        if decodeJWT(token=token):
            response = OffsetPlateController().get_all_offset_plate_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/offset-plate/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@offset_plate_router.get(
    "/corrugation/offset-plate/get",
    response_model=OffsetPlateResponse,
)
async def get_offset_plate(
    plate_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific OffsetPlate record]

    Args:
        plate_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [OffsetPlateResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/offset-plate/get endpoint")
        if decodeJWT(token=token):
            response = OffsetPlateController().get_offset_plate_controller(
                plate_id=plate_id
            )
            return OffsetPlateResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/offset-plate/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@offset_plate_router.delete("/corrugation/offset-plate/delete")
async def delete_offset_plate(
    plate_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a OffsetPlate record]

    Args:
        plate_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/offset-plate/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return OffsetPlateController().delete_offset_plate_controller(
                plate_id=plate_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/offset-plate/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
