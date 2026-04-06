from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.dimensions_request import (
    DimensionCreate,
    DimensionUpdate,
)
from sql.apis.schemas.responses.custom.dimensions_response import DimensionResponse
from sql.controllers.custom.dimensions_controller import DimensionController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
dimensions_router = APIRouter()


@dimensions_router.post(
    "/corrugation/dimensions/create",
    response_model=DimensionResponse,
)
async def create_dimension(
    create_request: DimensionCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Dimension record]

    Args:
        create_request (DimensionCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DimensionResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/dimensions/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details,
                allowed_user_role_id=1,
            )
            response = DimensionController().create_dimension_controller(
                request=create_request
            )
            return DimensionResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/dimensions/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@dimensions_router.post(
    "/corrugation/dimensions/update",
    response_model=DimensionResponse,
)
async def update_dimension(
    update_request: DimensionUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Dimension record]

    Args:
        update_request (DimensionUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DimensionResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/dimensions/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = DimensionController().update_dimension_controller(
                request=update_request
            )
            return DimensionResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/dimensions/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@dimensions_router.get(
    "/corrugation/dimensions/list_all",
)
async def list_all_dimension(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Dimension records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/dimensions/list_all endpoint")
        if decodeJWT(token=token):
            response = DimensionController().get_all_dimension_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/dimensions/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@dimensions_router.get(
    "/corrugation/dimensions/get",
    response_model=DimensionResponse,
)
async def get_dimension(
    dimension_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Dimension record]

    Args:
        dimension_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DimensionResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/dimensions/get endpoint")
        if decodeJWT(token=token):
            response = DimensionController().get_dimension_controller(
                dimension_id=dimension_id
            )
            return DimensionResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/dimensions/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@dimensions_router.delete("/corrugation/dimensions/delete")
async def delete_dimension(
    dimension_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Dimension record]

    Args:
        dimension_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/dimensions/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return DimensionController().delete_dimension_controller(
                dimension_id=dimension_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/dimensions/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
