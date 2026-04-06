from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.bundling_rope_request import BundlingRopeCreate, BundlingRopeUpdate
from sql.apis.schemas.responses.custom.bundling_rope_response import BundlingRopeResponse
from sql.controllers.custom.bundling_rope_controller import BundlingRopeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
bundling_rope_router = APIRouter()


@bundling_rope_router.post(
    "/corrugation/bundling-rope/create",
    response_model=BundlingRopeResponse,
)
async def create_bundling_rope(
    create_request: BundlingRopeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new BundlingRope record]

    Args:
        create_request (BundlingRopeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BundlingRopeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/bundling-rope/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BundlingRopeController().create_bundling_rope_controller(
                request=create_request
            )
            return BundlingRopeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundling-rope/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bundling_rope_router.post(
    "/corrugation/bundling-rope/update",
    response_model=BundlingRopeResponse,
)
async def update_bundling_rope(
    update_request: BundlingRopeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a BundlingRope record]

    Args:
        update_request (BundlingRopeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BundlingRopeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/bundling-rope/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BundlingRopeController().update_bundling_rope_controller(
                request=update_request
            )
            return BundlingRopeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundling-rope/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bundling_rope_router.get(
    "/corrugation/bundling-rope/list_all",
)
async def list_all_bundling_rope(
    token: str = Depends(oauth2_scheme),
):
    """[Get all BundlingRope records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/bundling-rope/list_all endpoint")
        if decodeJWT(token=token):
            response = BundlingRopeController().get_all_bundling_rope_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundling-rope/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bundling_rope_router.get(
    "/corrugation/bundling-rope/get",
    response_model=BundlingRopeResponse,
)
async def get_bundling_rope(
    bundle_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific BundlingRope record]

    Args:
        bundle_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BundlingRopeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/bundling-rope/get endpoint")
        if decodeJWT(token=token):
            response = BundlingRopeController().get_bundling_rope_controller(
                bundle_id=bundle_id
            )
            return BundlingRopeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundling-rope/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bundling_rope_router.delete("/corrugation/bundling-rope/delete")
async def delete_bundling_rope(
    bundle_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a BundlingRope record]

    Args:
        bundle_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/bundling-rope/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return BundlingRopeController().delete_bundling_rope_controller(
                bundle_id=bundle_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundling-rope/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
