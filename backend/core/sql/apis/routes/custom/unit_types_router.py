from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.unit_types_request import UnitTypeCreate, UnitTypeUpdate
from sql.apis.schemas.responses.custom.unit_types_response import UnitTypeResponse
from sql.controllers.custom.unit_types_controller import UnitTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
unit_types_router = APIRouter()


@unit_types_router.post(
    "/corrugation/unit-types/create",
    response_model=UnitTypeResponse,
)
async def create_unit_type(
    create_request: UnitTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new UnitType record]

    Args:
        create_request (UnitTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [UnitTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/unit-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = UnitTypeController().create_unit_type_controller(
                request=create_request
            )
            return UnitTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/unit-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@unit_types_router.post(
    "/corrugation/unit-types/update",
    response_model=UnitTypeResponse,
)
async def update_unit_type(
    update_request: UnitTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a UnitType record]

    Args:
        update_request (UnitTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [UnitTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/unit-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = UnitTypeController().update_unit_type_controller(
                request=update_request
            )
            return UnitTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/unit-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@unit_types_router.get(
    "/corrugation/unit-types/list_all",
)
async def list_all_unit_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all UnitType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/unit-types/list_all endpoint")
        if decodeJWT(token=token):
            response = UnitTypeController().get_all_unit_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/unit-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@unit_types_router.get(
    "/corrugation/unit-types/get",
    response_model=UnitTypeResponse,
)
async def get_unit_type(
    unit_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific UnitType record]

    Args:
        unit_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [UnitTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/unit-types/get endpoint")
        if decodeJWT(token=token):
            response = UnitTypeController().get_unit_type_controller(
                unit_type_id=unit_type_id
            )
            return UnitTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/unit-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@unit_types_router.delete("/corrugation/unit-types/delete")
async def delete_unit_type(
    unit_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a UnitType record]

    Args:
        unit_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/unit-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return UnitTypeController().delete_unit_type_controller(
                unit_type_id=unit_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/unit-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
