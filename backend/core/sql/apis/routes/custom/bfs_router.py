from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.bfs_request import BfCreate, BfUpdate
from sql.apis.schemas.responses.custom.bfs_response import BfResponse
from sql.controllers.custom.bfs_controller import BfController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
bfs_router = APIRouter()


@bfs_router.post(
    "/corrugation/bfs/create",
    response_model=BfResponse,
)
async def create_bf(
    create_request: BfCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Bf record]

    Args:
        create_request (BfCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BfResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/bfs/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BfController().create_bf_controller(
                request=create_request
            )
            return BfResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bfs/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bfs_router.post(
    "/corrugation/bfs/update",
    response_model=BfResponse,
)
async def update_bf(
    update_request: BfUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Bf record]

    Args:
        update_request (BfUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BfResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/bfs/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BfController().update_bf_controller(
                request=update_request
            )
            return BfResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bfs/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bfs_router.get(
    "/corrugation/bfs/list_all",
)
async def list_all_bf(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Bf records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/bfs/list_all endpoint")
        if decodeJWT(token=token):
            response = BfController().get_all_bf_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bfs/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bfs_router.get(
    "/corrugation/bfs/get",
    response_model=BfResponse,
)
async def get_bf(
    bf_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Bf record]

    Args:
        bf_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BfResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/bfs/get endpoint")
        if decodeJWT(token=token):
            response = BfController().get_bf_controller(
                bf_id=bf_id
            )
            return BfResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bfs/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bfs_router.delete("/corrugation/bfs/delete")
async def delete_bf(
    bf_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Bf record]

    Args:
        bf_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/bfs/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return BfController().delete_bf_controller(
                bf_id=bf_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bfs/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
