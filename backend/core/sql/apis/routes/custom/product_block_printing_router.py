from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_block_printing_request import ProductBlockPrintingCreate, ProductBlockPrintingUpdate
from sql.apis.schemas.responses.custom.product_block_printing_response import ProductBlockPrintingResponse
from sql.controllers.custom.product_block_printing_controller import ProductBlockPrintingController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_block_printing_router = APIRouter()


@product_block_printing_router.post(
    "/corrugation/product-block-printing/create",
    response_model=ProductBlockPrintingResponse,
)
async def create_product_block_printing(
    create_request: ProductBlockPrintingCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductBlockPrinting record]

    Args:
        create_request (ProductBlockPrintingCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductBlockPrintingResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-block-printing/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductBlockPrintingController().create_product_block_printing_controller(
                request=create_request
            )
            return ProductBlockPrintingResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-block-printing/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_block_printing_router.post(
    "/corrugation/product-block-printing/update",
    response_model=ProductBlockPrintingResponse,
)
async def update_product_block_printing(
    update_request: ProductBlockPrintingUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductBlockPrinting record]

    Args:
        update_request (ProductBlockPrintingUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductBlockPrintingResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-block-printing/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductBlockPrintingController().update_product_block_printing_controller(
                request=update_request
            )
            return ProductBlockPrintingResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-block-printing/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_block_printing_router.get(
    "/corrugation/product-block-printing/list_all",
)
async def list_all_product_block_printing(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductBlockPrinting records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-block-printing/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductBlockPrintingController().get_all_product_block_printing_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-block-printing/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_block_printing_router.get(
    "/corrugation/product-block-printing/get",
    response_model=ProductBlockPrintingResponse,
)
async def get_product_block_printing(
    print_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductBlockPrinting record]

    Args:
        print_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductBlockPrintingResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-block-printing/get endpoint")
        if decodeJWT(token=token):
            response = ProductBlockPrintingController().get_product_block_printing_controller(
                print_id=print_id
            )
            return ProductBlockPrintingResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-block-printing/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_block_printing_router.delete("/corrugation/product-block-printing/delete")
async def delete_product_block_printing(
    print_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductBlockPrinting record]

    Args:
        print_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-block-printing/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductBlockPrintingController().delete_product_block_printing_controller(
                print_id=print_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-block-printing/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
