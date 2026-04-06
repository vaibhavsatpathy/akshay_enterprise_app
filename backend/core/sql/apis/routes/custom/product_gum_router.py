from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_gum_request import ProductGumCreate, ProductGumUpdate
from sql.apis.schemas.responses.custom.product_gum_response import ProductGumResponse
from sql.controllers.custom.product_gum_controller import ProductGumController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_gum_router = APIRouter()


@product_gum_router.post(
    "/corrugation/product-gum/create",
    response_model=ProductGumResponse,
)
async def create_product_gum(
    create_request: ProductGumCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductGum record]

    Args:
        create_request (ProductGumCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductGumResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-gum/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductGumController().create_product_gum_controller(
                request=create_request
            )
            return ProductGumResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-gum/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_gum_router.post(
    "/corrugation/product-gum/update",
    response_model=ProductGumResponse,
)
async def update_product_gum(
    update_request: ProductGumUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductGum record]

    Args:
        update_request (ProductGumUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductGumResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-gum/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductGumController().update_product_gum_controller(
                request=update_request
            )
            return ProductGumResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-gum/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_gum_router.get(
    "/corrugation/product-gum/list_all",
)
async def list_all_product_gum(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductGum records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-gum/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductGumController().get_all_product_gum_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-gum/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_gum_router.get(
    "/corrugation/product-gum/get",
    response_model=ProductGumResponse,
)
async def get_product_gum(
    gum_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductGum record]

    Args:
        gum_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductGumResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-gum/get endpoint")
        if decodeJWT(token=token):
            response = ProductGumController().get_product_gum_controller(
                gum_id=gum_id
            )
            return ProductGumResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-gum/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_gum_router.delete("/corrugation/product-gum/delete")
async def delete_product_gum(
    gum_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductGum record]

    Args:
        gum_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-gum/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductGumController().delete_product_gum_controller(
                gum_id=gum_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-gum/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
