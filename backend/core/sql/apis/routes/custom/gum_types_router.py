from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.gum_types_request import GumTypeCreate, GumTypeUpdate
from sql.apis.schemas.responses.custom.gum_types_response import GumTypeResponse
from sql.controllers.custom.gum_types_controller import GumTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
gum_types_router = APIRouter()


@gum_types_router.post(
    "/corrugation/gum-types/create",
    response_model=GumTypeResponse,
)
async def create_gum_type(
    create_request: GumTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new GumType record]

    Args:
        create_request (GumTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [GumTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/gum-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = GumTypeController().create_gum_type_controller(
                request=create_request
            )
            return GumTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gum-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gum_types_router.post(
    "/corrugation/gum-types/update",
    response_model=GumTypeResponse,
)
async def update_gum_type(
    update_request: GumTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a GumType record]

    Args:
        update_request (GumTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [GumTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/gum-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = GumTypeController().update_gum_type_controller(
                request=update_request
            )
            return GumTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gum-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gum_types_router.get(
    "/corrugation/gum-types/list_all",
)
async def list_all_gum_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all GumType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/gum-types/list_all endpoint")
        if decodeJWT(token=token):
            response = GumTypeController().get_all_gum_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gum-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gum_types_router.get(
    "/corrugation/gum-types/get",
    response_model=GumTypeResponse,
)
async def get_gum_type(
    gum_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific GumType record]

    Args:
        gum_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [GumTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/gum-types/get endpoint")
        if decodeJWT(token=token):
            response = GumTypeController().get_gum_type_controller(
                gum_type_id=gum_type_id
            )
            return GumTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gum-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gum_types_router.delete("/corrugation/gum-types/delete")
async def delete_gum_type(
    gum_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a GumType record]

    Args:
        gum_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/gum-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return GumTypeController().delete_gum_type_controller(
                gum_type_id=gum_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gum-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
