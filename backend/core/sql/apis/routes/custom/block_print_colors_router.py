from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.block_print_colors_request import BlockPrintColorCreate, BlockPrintColorUpdate
from sql.apis.schemas.responses.custom.block_print_colors_response import BlockPrintColorResponse
from sql.controllers.custom.block_print_colors_controller import BlockPrintColorController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
block_print_colors_router = APIRouter()


@block_print_colors_router.post(
    "/corrugation/block-print-colors/create",
    response_model=BlockPrintColorResponse,
)
async def create_block_print_color(
    create_request: BlockPrintColorCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new BlockPrintColor record]

    Args:
        create_request (BlockPrintColorCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BlockPrintColorResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/block-print-colors/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BlockPrintColorController().create_block_print_color_controller(
                request=create_request
            )
            return BlockPrintColorResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-print-colors/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@block_print_colors_router.post(
    "/corrugation/block-print-colors/update",
    response_model=BlockPrintColorResponse,
)
async def update_block_print_color(
    update_request: BlockPrintColorUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a BlockPrintColor record]

    Args:
        update_request (BlockPrintColorUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BlockPrintColorResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/block-print-colors/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BlockPrintColorController().update_block_print_color_controller(
                request=update_request
            )
            return BlockPrintColorResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-print-colors/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@block_print_colors_router.get(
    "/corrugation/block-print-colors/list_all",
)
async def list_all_block_print_color(
    token: str = Depends(oauth2_scheme),
):
    """[Get all BlockPrintColor records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/block-print-colors/list_all endpoint")
        if decodeJWT(token=token):
            response = BlockPrintColorController().get_all_block_print_color_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-print-colors/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@block_print_colors_router.get(
    "/corrugation/block-print-colors/get",
    response_model=BlockPrintColorResponse,
)
async def get_block_print_color(
    color_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific BlockPrintColor record]

    Args:
        color_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BlockPrintColorResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/block-print-colors/get endpoint")
        if decodeJWT(token=token):
            response = BlockPrintColorController().get_block_print_color_controller(
                color_id=color_id
            )
            return BlockPrintColorResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-print-colors/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@block_print_colors_router.delete("/corrugation/block-print-colors/delete")
async def delete_block_print_color(
    color_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a BlockPrintColor record]

    Args:
        color_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/block-print-colors/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return BlockPrintColorController().delete_block_print_color_controller(
                color_id=color_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/block-print-colors/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
