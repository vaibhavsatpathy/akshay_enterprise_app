from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.rejected_items_request import RejectedItemCreate, RejectedItemUpdate
from sql.apis.schemas.responses.custom.rejected_items_response import RejectedItemResponse
from sql.controllers.custom.rejected_items_controller import RejectedItemController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
rejected_items_router = APIRouter()


@rejected_items_router.post(
    "/corrugation/rejected-items/create",
    response_model=RejectedItemResponse,
)
async def create_rejected_item(
    create_request: RejectedItemCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new RejectedItem record]

    Args:
        create_request (RejectedItemCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RejectedItemResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/rejected-items/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = RejectedItemController().create_rejected_item_controller(
                request=create_request
            )
            return RejectedItemResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-items/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rejected_items_router.post(
    "/corrugation/rejected-items/update",
    response_model=RejectedItemResponse,
)
async def update_rejected_item(
    update_request: RejectedItemUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a RejectedItem record]

    Args:
        update_request (RejectedItemUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RejectedItemResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/rejected-items/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = RejectedItemController().update_rejected_item_controller(
                request=update_request
            )
            return RejectedItemResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-items/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rejected_items_router.get(
    "/corrugation/rejected-items/list_all",
)
async def list_all_rejected_item(
    token: str = Depends(oauth2_scheme),
):
    """[Get all RejectedItem records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/rejected-items/list_all endpoint")
        if decodeJWT(token=token):
            response = RejectedItemController().get_all_rejected_item_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-items/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rejected_items_router.get(
    "/corrugation/rejected-items/get",
    response_model=RejectedItemResponse,
)
async def get_rejected_item(
    rejected_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific RejectedItem record]

    Args:
        rejected_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RejectedItemResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/rejected-items/get endpoint")
        if decodeJWT(token=token):
            response = RejectedItemController().get_rejected_item_controller(
                rejected_id=rejected_id
            )
            return RejectedItemResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-items/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rejected_items_router.delete("/corrugation/rejected-items/delete")
async def delete_rejected_item(
    rejected_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a RejectedItem record]

    Args:
        rejected_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/rejected-items/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return RejectedItemController().delete_rejected_item_controller(
                rejected_id=rejected_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rejected-items/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
