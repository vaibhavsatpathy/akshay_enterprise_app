from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.box_types_request import BoxTypeCreate, BoxTypeUpdate
from sql.apis.schemas.responses.custom.box_types_response import BoxTypeResponse
from sql.controllers.custom.box_types_controller import BoxTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
box_types_router = APIRouter()


@box_types_router.post(
    "/corrugation/box-types/create",
    response_model=BoxTypeResponse,
)
async def create_box_type(
    create_request: BoxTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new BoxType record]

    Args:
        create_request (BoxTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BoxTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/box-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BoxTypeController().create_box_type_controller(
                request=create_request
            )
            return BoxTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/box-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@box_types_router.post(
    "/corrugation/box-types/update",
    response_model=BoxTypeResponse,
)
async def update_box_type(
    update_request: BoxTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a BoxType record]

    Args:
        update_request (BoxTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BoxTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/box-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BoxTypeController().update_box_type_controller(
                request=update_request
            )
            return BoxTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/box-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@box_types_router.get(
    "/corrugation/box-types/list_all",
)
async def list_all_box_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all BoxType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/box-types/list_all endpoint")
        if decodeJWT(token=token):
            response = BoxTypeController().get_all_box_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/box-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@box_types_router.get(
    "/corrugation/box-types/get",
    response_model=BoxTypeResponse,
)
async def get_box_type(
    box_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific BoxType record]

    Args:
        box_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BoxTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/box-types/get endpoint")
        if decodeJWT(token=token):
            response = BoxTypeController().get_box_type_controller(
                box_type_id=box_type_id
            )
            return BoxTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/box-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@box_types_router.delete("/corrugation/box-types/delete")
async def delete_box_type(
    box_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a BoxType record]

    Args:
        box_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/box-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return BoxTypeController().delete_box_type_controller(
                box_type_id=box_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/box-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
