from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_stitching_pin_request import ProductStitchingPinCreate, ProductStitchingPinUpdate
from sql.apis.schemas.responses.custom.product_stitching_pin_response import ProductStitchingPinResponse
from sql.controllers.custom.product_stitching_pin_controller import ProductStitchingPinController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_stitching_pin_router = APIRouter()


@product_stitching_pin_router.post(
    "/corrugation/product-stitching-pin/create",
    response_model=ProductStitchingPinResponse,
)
async def create_product_stitching_pin(
    create_request: ProductStitchingPinCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductStitchingPin record]

    Args:
        create_request (ProductStitchingPinCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductStitchingPinResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-stitching-pin/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductStitchingPinController().create_product_stitching_pin_controller(
                request=create_request
            )
            return ProductStitchingPinResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-stitching-pin/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_stitching_pin_router.post(
    "/corrugation/product-stitching-pin/update",
    response_model=ProductStitchingPinResponse,
)
async def update_product_stitching_pin(
    update_request: ProductStitchingPinUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductStitchingPin record]

    Args:
        update_request (ProductStitchingPinUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductStitchingPinResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-stitching-pin/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductStitchingPinController().update_product_stitching_pin_controller(
                request=update_request
            )
            return ProductStitchingPinResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-stitching-pin/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_stitching_pin_router.get(
    "/corrugation/product-stitching-pin/list_all",
)
async def list_all_product_stitching_pin(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductStitchingPin records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-stitching-pin/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductStitchingPinController().get_all_product_stitching_pin_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-stitching-pin/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_stitching_pin_router.get(
    "/corrugation/product-stitching-pin/get",
    response_model=ProductStitchingPinResponse,
)
async def get_product_stitching_pin(
    pin_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductStitchingPin record]

    Args:
        pin_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductStitchingPinResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-stitching-pin/get endpoint")
        if decodeJWT(token=token):
            response = ProductStitchingPinController().get_product_stitching_pin_controller(
                pin_id=pin_id
            )
            return ProductStitchingPinResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-stitching-pin/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_stitching_pin_router.delete("/corrugation/product-stitching-pin/delete")
async def delete_product_stitching_pin(
    pin_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductStitchingPin record]

    Args:
        pin_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-stitching-pin/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductStitchingPinController().delete_product_stitching_pin_controller(
                pin_id=pin_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-stitching-pin/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
