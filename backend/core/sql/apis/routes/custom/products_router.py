from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.products_request import ProductCreate, ProductUpdate
from sql.apis.schemas.responses.custom.products_response import ProductResponse
from sql.controllers.custom.products_controller import ProductController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
products_router = APIRouter()


@products_router.post(
    "/corrugation/products/create",
    response_model=ProductResponse,
)
async def create_product(
    create_request: ProductCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Product record]

    Args:
        create_request (ProductCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/products/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductController().create_product_controller(
                request=create_request
            )
            return ProductResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/products/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@products_router.post(
    "/corrugation/products/update",
    response_model=ProductResponse,
)
async def update_product(
    update_request: ProductUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Product record]

    Args:
        update_request (ProductUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/products/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductController().update_product_controller(
                request=update_request
            )
            return ProductResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/products/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@products_router.get(
    "/corrugation/products/list_all",
)
async def list_all_product(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Product records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/products/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductController().get_all_product_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/products/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@products_router.get(
    "/corrugation/products/get",
    response_model=ProductResponse,
)
async def get_product(
    product_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Product record]

    Args:
        product_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/products/get endpoint")
        if decodeJWT(token=token):
            response = ProductController().get_product_controller(
                product_id=product_id
            )
            return ProductResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/products/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@products_router.delete("/corrugation/products/delete")
async def delete_product(
    product_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Product record]

    Args:
        product_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/products/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductController().delete_product_controller(
                product_id=product_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/products/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
