from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.orders_table_request import (
    OrdersTableCreate,
    OrdersTableUpdate,
)
from sql.apis.schemas.responses.custom.orders_table_response import OrdersTableResponse
from sql.controllers.custom.orders_table_controller import OrdersTableController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
orders_table_router = APIRouter()


@orders_table_router.post(
    "/corrugation/orders-table/create",
    response_model=OrdersTableResponse,
)
async def create_orders_table(
    create_request: OrdersTableCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new OrdersTable record]

    Args:
        create_request (OrdersTableCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [OrdersTableResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/orders-table/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = OrdersTableController().create_order_controller(
                request=create_request
            )
            return OrdersTableResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/orders-table/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@orders_table_router.post(
    "/corrugation/orders-table/update",
    response_model=OrdersTableResponse,
)
async def update_orders_table(
    update_request: OrdersTableUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a OrdersTable record]

    Args:
        update_request (OrdersTableUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [OrdersTableResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/orders-table/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = OrdersTableController().update_order_controller(
                request=update_request
            )
            return OrdersTableResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/orders-table/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@orders_table_router.get(
    "/corrugation/orders-table/list_all",
)
async def list_all_orders_table(
    token: str = Depends(oauth2_scheme),
):
    """[Get all OrdersTable records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/orders-table/list_all endpoint")
        if decodeJWT(token=token):
            response = OrdersTableController().get_all_order_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/orders-table/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@orders_table_router.get(
    "/corrugation/orders-table/get",
    response_model=OrdersTableResponse,
)
async def get_orders_table(
    order_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific OrdersTable record]

    Args:
        order_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [OrdersTableResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/orders-table/get endpoint")
        if decodeJWT(token=token):
            response = OrdersTableController().get_order_controller(order_id=order_id)
            return OrdersTableResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/orders-table/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@orders_table_router.delete("/corrugation/orders-table/delete")
async def delete_orders_table(
    order_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a OrdersTable record]

    Args:
        order_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/orders-table/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return OrdersTableController().delete_order_controller(order_id=order_id)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/orders-table/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
