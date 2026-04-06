from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.plate_types_request import PlateTypeCreate, PlateTypeUpdate
from sql.apis.schemas.responses.custom.plate_types_response import PlateTypeResponse
from sql.controllers.custom.plate_types_controller import PlateTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
plate_types_router = APIRouter()


@plate_types_router.post(
    "/corrugation/plate-types/create",
    response_model=PlateTypeResponse,
)
async def create_plate_type(
    create_request: PlateTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new PlateType record]

    Args:
        create_request (PlateTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PlateTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/plate-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PlateTypeController().create_plate_type_controller(
                request=create_request
            )
            return PlateTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@plate_types_router.post(
    "/corrugation/plate-types/update",
    response_model=PlateTypeResponse,
)
async def update_plate_type(
    update_request: PlateTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a PlateType record]

    Args:
        update_request (PlateTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PlateTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/plate-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PlateTypeController().update_plate_type_controller(
                request=update_request
            )
            return PlateTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@plate_types_router.get(
    "/corrugation/plate-types/list_all",
)
async def list_all_plate_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all PlateType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/plate-types/list_all endpoint")
        if decodeJWT(token=token):
            response = PlateTypeController().get_all_plate_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@plate_types_router.get(
    "/corrugation/plate-types/get",
    response_model=PlateTypeResponse,
)
async def get_plate_type(
    plate_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific PlateType record]

    Args:
        plate_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PlateTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/plate-types/get endpoint")
        if decodeJWT(token=token):
            response = PlateTypeController().get_plate_type_controller(
                plate_type_id=plate_type_id
            )
            return PlateTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@plate_types_router.delete("/corrugation/plate-types/delete")
async def delete_plate_type(
    plate_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a PlateType record]

    Args:
        plate_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/plate-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PlateTypeController().delete_plate_type_controller(
                plate_type_id=plate_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/plate-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
