from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.locations_request import LocationCreate, LocationUpdate
from sql.apis.schemas.responses.custom.locations_response import LocationResponse
from sql.controllers.custom.locations_controller import LocationController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
locations_router = APIRouter()


@locations_router.post(
    "/corrugation/locations/create",
    response_model=LocationResponse,
)
async def create_location(
    create_request: LocationCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Location record]

    Args:
        create_request (LocationCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [LocationResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/locations/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = LocationController().create_location_controller(
                request=create_request
            )
            return LocationResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/locations/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@locations_router.post(
    "/corrugation/locations/update",
    response_model=LocationResponse,
)
async def update_location(
    update_request: LocationUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Location record]

    Args:
        update_request (LocationUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [LocationResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/locations/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = LocationController().update_location_controller(
                request=update_request
            )
            return LocationResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/locations/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@locations_router.get(
    "/corrugation/locations/list_all",
)
async def list_all_location(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Location records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/locations/list_all endpoint")
        if decodeJWT(token=token):
            response = LocationController().get_all_location_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/locations/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@locations_router.get(
    "/corrugation/locations/get",
    response_model=LocationResponse,
)
async def get_location(
    location_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Location record]

    Args:
        location_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [LocationResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/locations/get endpoint")
        if decodeJWT(token=token):
            response = LocationController().get_location_controller(
                location_id=location_id
            )
            return LocationResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/locations/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@locations_router.delete("/corrugation/locations/delete")
async def delete_location(
    location_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Location record]

    Args:
        location_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/locations/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return LocationController().delete_location_controller(
                location_id=location_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/locations/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
