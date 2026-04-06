from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.rejected_item_types_request import RejectedItemTypeCreate, RejectedItemTypeUpdate
from sql.apis.schemas.responses.custom.rejected_item_types_response import RejectedItemTypeResponse
from sql.controllers.custom.rejected_item_types_controller import RejectedItemTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
rejected_item_types_router = APIRouter()


@rejected_item_types_router.post(
    "/corrugation/rejected-item-types/create",
    response_model=RejectedItemTypeResponse,
)
async def create_rejected_item_type(
    create_request: RejectedItemTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new RejectedItemType record]

    Args:
        create_request (RejectedItemTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RejectedItemTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/rejected-item-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = RejectedItemTypeController().create_rejected_item_type_controller(
                request=create_request
            )
            return RejectedItemTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-item-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rejected_item_types_router.post(
    "/corrugation/rejected-item-types/update",
    response_model=RejectedItemTypeResponse,
)
async def update_rejected_item_type(
    update_request: RejectedItemTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a RejectedItemType record]

    Args:
        update_request (RejectedItemTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RejectedItemTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/rejected-item-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = RejectedItemTypeController().update_rejected_item_type_controller(
                request=update_request
            )
            return RejectedItemTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-item-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rejected_item_types_router.get(
    "/corrugation/rejected-item-types/list_all",
)
async def list_all_rejected_item_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all RejectedItemType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/rejected-item-types/list_all endpoint")
        if decodeJWT(token=token):
            response = RejectedItemTypeController().get_all_rejected_item_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-item-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rejected_item_types_router.get(
    "/corrugation/rejected-item-types/get",
    response_model=RejectedItemTypeResponse,
)
async def get_rejected_item_type(
    rejected_item_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific RejectedItemType record]

    Args:
        rejected_item_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RejectedItemTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/rejected-item-types/get endpoint")
        if decodeJWT(token=token):
            response = RejectedItemTypeController().get_rejected_item_type_controller(
                rejected_item_type_id=rejected_item_type_id
            )
            return RejectedItemTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-item-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rejected_item_types_router.delete("/corrugation/rejected-item-types/delete")
async def delete_rejected_item_type(
    rejected_item_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a RejectedItemType record]

    Args:
        rejected_item_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/rejected-item-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return RejectedItemTypeController().delete_rejected_item_type_controller(
                rejected_item_type_id=rejected_item_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-item-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
