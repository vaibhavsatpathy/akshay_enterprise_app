from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.layer_types_request import LayerTypeCreate, LayerTypeUpdate
from sql.apis.schemas.responses.custom.layer_types_response import LayerTypeResponse
from sql.controllers.custom.layer_types_controller import LayerTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
layer_types_router = APIRouter()


@layer_types_router.post(
    "/corrugation/layer-types/create",
    response_model=LayerTypeResponse,
)
async def create_layer_type(
    create_request: LayerTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new LayerType record]

    Args:
        create_request (LayerTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [LayerTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/layer-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = LayerTypeController().create_layer_type_controller(
                request=create_request
            )
            return LayerTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/layer-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@layer_types_router.post(
    "/corrugation/layer-types/update",
    response_model=LayerTypeResponse,
)
async def update_layer_type(
    update_request: LayerTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a LayerType record]

    Args:
        update_request (LayerTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [LayerTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/layer-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = LayerTypeController().update_layer_type_controller(
                request=update_request
            )
            return LayerTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/layer-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@layer_types_router.get(
    "/corrugation/layer-types/list_all",
)
async def list_all_layer_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all LayerType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/layer-types/list_all endpoint")
        if decodeJWT(token=token):
            response = LayerTypeController().get_all_layer_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/layer-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@layer_types_router.get(
    "/corrugation/layer-types/get",
    response_model=LayerTypeResponse,
)
async def get_layer_type(
    layer_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific LayerType record]

    Args:
        layer_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [LayerTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/layer-types/get endpoint")
        if decodeJWT(token=token):
            response = LayerTypeController().get_layer_type_controller(
                layer_type_id=layer_type_id
            )
            return LayerTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/layer-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@layer_types_router.delete("/corrugation/layer-types/delete")
async def delete_layer_type(
    layer_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a LayerType record]

    Args:
        layer_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/layer-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return LayerTypeController().delete_layer_type_controller(
                layer_type_id=layer_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/layer-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
