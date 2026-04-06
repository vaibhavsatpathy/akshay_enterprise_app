from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.stitching_pin_types_request import StitchingPinTypeCreate, StitchingPinTypeUpdate
from sql.apis.schemas.responses.custom.stitching_pin_types_response import StitchingPinTypeResponse
from sql.controllers.custom.stitching_pin_types_controller import StitchingPinTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
stitching_pin_types_router = APIRouter()


@stitching_pin_types_router.post(
    "/corrugation/stitching-pin-types/create",
    response_model=StitchingPinTypeResponse,
)
async def create_stitching_pin_type(
    create_request: StitchingPinTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new StitchingPinType record]

    Args:
        create_request (StitchingPinTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingPinTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StitchingPinTypeController().create_stitching_pin_type_controller(
                request=create_request
            )
            return StitchingPinTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_types_router.post(
    "/corrugation/stitching-pin-types/update",
    response_model=StitchingPinTypeResponse,
)
async def update_stitching_pin_type(
    update_request: StitchingPinTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a StitchingPinType record]

    Args:
        update_request (StitchingPinTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingPinTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StitchingPinTypeController().update_stitching_pin_type_controller(
                request=update_request
            )
            return StitchingPinTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_types_router.get(
    "/corrugation/stitching-pin-types/list_all",
)
async def list_all_stitching_pin_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all StitchingPinType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-types/list_all endpoint")
        if decodeJWT(token=token):
            response = StitchingPinTypeController().get_all_stitching_pin_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_types_router.get(
    "/corrugation/stitching-pin-types/get",
    response_model=StitchingPinTypeResponse,
)
async def get_stitching_pin_type(
    pin_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific StitchingPinType record]

    Args:
        pin_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingPinTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-types/get endpoint")
        if decodeJWT(token=token):
            response = StitchingPinTypeController().get_stitching_pin_type_controller(
                pin_type_id=pin_type_id
            )
            return StitchingPinTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_types_router.delete("/corrugation/stitching-pin-types/delete")
async def delete_stitching_pin_type(
    pin_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a StitchingPinType record]

    Args:
        pin_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return StitchingPinTypeController().delete_stitching_pin_type_controller(
                pin_type_id=pin_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
