from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.inventory_request import InventoryCreate, InventoryUpdate
from sql.apis.schemas.responses.custom.inventory_response import InventoryResponse
from sql.controllers.custom.inventory_controller import InventoryController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
inventory_router = APIRouter()


@inventory_router.post(
    "/corrugation/inventory/create",
    response_model=InventoryResponse,
)
async def create_inventory(
    create_request: InventoryCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Inventory record]

    Args:
        create_request (InventoryCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [InventoryResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/inventory/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = InventoryController().create_inventory_controller(
                request=create_request
            )
            return InventoryResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/inventory/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@inventory_router.post(
    "/corrugation/inventory/update",
    response_model=InventoryResponse,
)
async def update_inventory(
    update_request: InventoryUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Inventory record]

    Args:
        update_request (InventoryUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [InventoryResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/inventory/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = InventoryController().update_inventory_controller(
                request=update_request
            )
            return InventoryResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/inventory/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@inventory_router.get(
    "/corrugation/inventory/list_all",
)
async def list_all_inventory(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Inventory records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/inventory/list_all endpoint")
        if decodeJWT(token=token):
            response = InventoryController().get_all_inventory_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/inventory/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@inventory_router.get(
    "/corrugation/inventory/get",
    response_model=InventoryResponse,
)
async def get_inventory(
    inventory_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Inventory record]

    Args:
        inventory_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [InventoryResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/inventory/get endpoint")
        if decodeJWT(token=token):
            response = InventoryController().get_inventory_controller(
                inventory_id=inventory_id
            )
            return InventoryResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/inventory/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@inventory_router.delete("/corrugation/inventory/delete")
async def delete_inventory(
    inventory_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Inventory record]

    Args:
        inventory_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/inventory/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return InventoryController().delete_inventory_controller(
                inventory_id=inventory_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/inventory/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
