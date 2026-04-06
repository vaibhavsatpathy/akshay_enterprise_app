from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.dispatch_table_request import (
    DispatchTableCreate,
    DispatchTableUpdate,
)
from sql.apis.schemas.responses.custom.dispatch_table_response import (
    DispatchTableResponse,
)
from sql.controllers.custom.dispatch_table_controller import DispatchTableController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
dispatch_table_router = APIRouter()


@dispatch_table_router.post(
    "/corrugation/dispatch-table/create",
    response_model=DispatchTableResponse,
)
async def create_dispatch_table(
    create_request: DispatchTableCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new DispatchTable record]

    Args:
        create_request (DispatchTableCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DispatchTableResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/dispatch-table/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = DispatchTableController().create_dispatch_controller(
                request=create_request
            )
            return DispatchTableResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/dispatch-table/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@dispatch_table_router.post(
    "/corrugation/dispatch-table/update",
    response_model=DispatchTableResponse,
)
async def update_dispatch_table(
    update_request: DispatchTableUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a DispatchTable record]

    Args:
        update_request (DispatchTableUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DispatchTableResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/dispatch-table/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = DispatchTableController().update_dispatch_controller(
                request=update_request
            )
            return DispatchTableResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/dispatch-table/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@dispatch_table_router.get(
    "/corrugation/dispatch-table/list_all",
)
async def list_all_dispatch_table(
    token: str = Depends(oauth2_scheme),
):
    """[Get all DispatchTable records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/dispatch-table/list_all endpoint")
        if decodeJWT(token=token):
            response = DispatchTableController().get_all_dispatch_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /corrugation/dispatch-table/list_all endpoint: {error}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@dispatch_table_router.get(
    "/corrugation/dispatch-table/get",
    response_model=DispatchTableResponse,
)
async def get_dispatch_table(
    id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific DispatchTable record]

    Args:
        id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DispatchTableResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/dispatch-table/get endpoint")
        if decodeJWT(token=token):
            response = DispatchTableController().get_dispatch_controller(id=id)
            return DispatchTableResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/dispatch-table/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@dispatch_table_router.delete("/corrugation/dispatch-table/delete")
async def delete_dispatch_table(
    id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a DispatchTable record]

    Args:
        id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/dispatch-table/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return DispatchTableController().delete_dispatch_controller(id=id)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/dispatch-table/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
