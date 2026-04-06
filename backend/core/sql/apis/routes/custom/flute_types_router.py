from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.flute_types_request import FluteTypeCreate, FluteTypeUpdate
from sql.apis.schemas.responses.custom.flute_types_response import FluteTypeResponse
from sql.controllers.custom.flute_types_controller import FluteTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
flute_types_router = APIRouter()


@flute_types_router.post(
    "/corrugation/flute-types/create",
    response_model=FluteTypeResponse,
)
async def create_flute_type(
    create_request: FluteTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new FluteType record]

    Args:
        create_request (FluteTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [FluteTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/flute-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = FluteTypeController().create_flute_type_controller(
                request=create_request
            )
            return FluteTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/flute-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@flute_types_router.post(
    "/corrugation/flute-types/update",
    response_model=FluteTypeResponse,
)
async def update_flute_type(
    update_request: FluteTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a FluteType record]

    Args:
        update_request (FluteTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [FluteTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/flute-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = FluteTypeController().update_flute_type_controller(
                request=update_request
            )
            return FluteTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/flute-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@flute_types_router.get(
    "/corrugation/flute-types/list_all",
)
async def list_all_flute_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all FluteType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/flute-types/list_all endpoint")
        if decodeJWT(token=token):
            response = FluteTypeController().get_all_flute_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/flute-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@flute_types_router.get(
    "/corrugation/flute-types/get",
    response_model=FluteTypeResponse,
)
async def get_flute_type(
    flute_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific FluteType record]

    Args:
        flute_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [FluteTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/flute-types/get endpoint")
        if decodeJWT(token=token):
            response = FluteTypeController().get_flute_type_controller(
                flute_type_id=flute_type_id
            )
            return FluteTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/flute-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@flute_types_router.delete("/corrugation/flute-types/delete")
async def delete_flute_type(
    flute_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a FluteType record]

    Args:
        flute_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/flute-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return FluteTypeController().delete_flute_type_controller(
                flute_type_id=flute_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/flute-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
