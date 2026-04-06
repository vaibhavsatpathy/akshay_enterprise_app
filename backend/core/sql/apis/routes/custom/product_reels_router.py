from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_reels_request import ProductReelCreate, ProductReelUpdate
from sql.apis.schemas.responses.custom.product_reels_response import ProductReelResponse
from sql.controllers.custom.product_reels_controller import ProductReelController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_reels_router = APIRouter()


@product_reels_router.post(
    "/corrugation/product-reels/create",
    response_model=ProductReelResponse,
)
async def create_product_reel(
    create_request: ProductReelCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductReel record]

    Args:
        create_request (ProductReelCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductReelResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-reels/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductReelController().create_product_reel_controller(
                request=create_request
            )
            return ProductReelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-reels/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_reels_router.post(
    "/corrugation/product-reels/update",
    response_model=ProductReelResponse,
)
async def update_product_reel(
    update_request: ProductReelUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductReel record]

    Args:
        update_request (ProductReelUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductReelResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-reels/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductReelController().update_product_reel_controller(
                request=update_request
            )
            return ProductReelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-reels/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_reels_router.get(
    "/corrugation/product-reels/list_all",
)
async def list_all_product_reel(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductReel records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-reels/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductReelController().get_all_product_reel_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-reels/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_reels_router.get(
    "/corrugation/product-reels/get",
    response_model=ProductReelResponse,
)
async def get_product_reel(
    reel_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductReel record]

    Args:
        reel_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductReelResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-reels/get endpoint")
        if decodeJWT(token=token):
            response = ProductReelController().get_product_reel_controller(
                reel_id=reel_id
            )
            return ProductReelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-reels/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_reels_router.delete("/corrugation/product-reels/delete")
async def delete_product_reel(
    reel_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductReel record]

    Args:
        reel_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-reels/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductReelController().delete_product_reel_controller(
                reel_id=reel_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-reels/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
