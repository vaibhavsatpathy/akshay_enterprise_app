from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.color_table_request import ColorTableCreate, ColorTableUpdate
from sql.apis.schemas.responses.custom.color_table_response import ColorTableResponse
from sql.controllers.custom.color_table_controller import ColorTableController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
color_table_router = APIRouter()


@color_table_router.post(
    "/corrugation/color-table/create",
    response_model=ColorTableResponse,
)
async def create_color_table(
    create_request: ColorTableCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ColorTable record]

    Args:
        create_request (ColorTableCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ColorTableResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/color-table/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ColorTableController().create_color_table_controller(
                request=create_request
            )
            return ColorTableResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-table/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@color_table_router.post(
    "/corrugation/color-table/update",
    response_model=ColorTableResponse,
)
async def update_color_table(
    update_request: ColorTableUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ColorTable record]

    Args:
        update_request (ColorTableUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ColorTableResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/color-table/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ColorTableController().update_color_table_controller(
                request=update_request
            )
            return ColorTableResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-table/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@color_table_router.get(
    "/corrugation/color-table/list_all",
)
async def list_all_color_table(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ColorTable records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/color-table/list_all endpoint")
        if decodeJWT(token=token):
            response = ColorTableController().get_all_color_table_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-table/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@color_table_router.get(
    "/corrugation/color-table/get",
    response_model=ColorTableResponse,
)
async def get_color_table(
    color_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ColorTable record]

    Args:
        color_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ColorTableResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/color-table/get endpoint")
        if decodeJWT(token=token):
            response = ColorTableController().get_color_table_controller(
                color_id=color_id
            )
            return ColorTableResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-table/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@color_table_router.delete("/corrugation/color-table/delete")
async def delete_color_table(
    color_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ColorTable record]

    Args:
        color_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/color-table/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ColorTableController().delete_color_table_controller(
                color_id=color_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-table/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
