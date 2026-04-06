from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.block_types_request import BlockTypeCreate, BlockTypeUpdate
from sql.apis.schemas.responses.custom.block_types_response import BlockTypeResponse
from sql.controllers.custom.block_types_controller import BlockTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
block_types_router = APIRouter()


@block_types_router.post(
    "/corrugation/block-types/create",
    response_model=BlockTypeResponse,
)
async def create_block_type(
    create_request: BlockTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new BlockType record]

    Args:
        create_request (BlockTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BlockTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/block-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BlockTypeController().create_block_type_controller(
                request=create_request
            )
            return BlockTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@block_types_router.post(
    "/corrugation/block-types/update",
    response_model=BlockTypeResponse,
)
async def update_block_type(
    update_request: BlockTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a BlockType record]

    Args:
        update_request (BlockTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BlockTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/block-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BlockTypeController().update_block_type_controller(
                request=update_request
            )
            return BlockTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@block_types_router.get(
    "/corrugation/block-types/list_all",
)
async def list_all_block_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all BlockType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/block-types/list_all endpoint")
        if decodeJWT(token=token):
            response = BlockTypeController().get_all_block_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@block_types_router.get(
    "/corrugation/block-types/get",
    response_model=BlockTypeResponse,
)
async def get_block_type(
    block_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific BlockType record]

    Args:
        block_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BlockTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/block-types/get endpoint")
        if decodeJWT(token=token):
            response = BlockTypeController().get_block_type_controller(
                block_type_id=block_type_id
            )
            return BlockTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@block_types_router.delete("/corrugation/block-types/delete")
async def delete_block_type(
    block_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a BlockType record]

    Args:
        block_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/block-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return BlockTypeController().delete_block_type_controller(
                block_type_id=block_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
