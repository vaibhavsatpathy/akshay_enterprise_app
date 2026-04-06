from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.gst_config_request import GstConfigCreate, GstConfigUpdate
from sql.apis.schemas.responses.custom.gst_config_response import GstConfigResponse
from sql.controllers.custom.gst_config_controller import GstConfigController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
gst_config_router = APIRouter()


@gst_config_router.post(
    "/corrugation/gst-config/create",
    response_model=GstConfigResponse,
)
async def create_gst_config(
    create_request: GstConfigCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new GstConfig record]

    Args:
        create_request (GstConfigCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [GstConfigResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/gst-config/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = GstConfigController().create_gst_config_controller(
                request=create_request
            )
            return GstConfigResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gst-config/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gst_config_router.post(
    "/corrugation/gst-config/update",
    response_model=GstConfigResponse,
)
async def update_gst_config(
    update_request: GstConfigUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a GstConfig record]

    Args:
        update_request (GstConfigUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [GstConfigResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/gst-config/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = GstConfigController().update_gst_config_controller(
                request=update_request
            )
            return GstConfigResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gst-config/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gst_config_router.get(
    "/corrugation/gst-config/list_all",
)
async def list_all_gst_config(
    token: str = Depends(oauth2_scheme),
):
    """[Get all GstConfig records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/gst-config/list_all endpoint")
        if decodeJWT(token=token):
            response = GstConfigController().get_all_gst_config_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gst-config/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gst_config_router.get(
    "/corrugation/gst-config/get",
    response_model=GstConfigResponse,
)
async def get_gst_config(
    gst_config_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific GstConfig record]

    Args:
        gst_config_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [GstConfigResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/gst-config/get endpoint")
        if decodeJWT(token=token):
            response = GstConfigController().get_gst_config_controller(
                gst_config_id=gst_config_id
            )
            return GstConfigResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gst-config/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gst_config_router.delete("/corrugation/gst-config/delete")
async def delete_gst_config(
    gst_config_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a GstConfig record]

    Args:
        gst_config_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/gst-config/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return GstConfigController().delete_gst_config_controller(
                gst_config_id=gst_config_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gst-config/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
