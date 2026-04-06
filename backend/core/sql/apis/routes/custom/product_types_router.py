from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_types_request import ProductTypeCreate, ProductTypeUpdate
from sql.apis.schemas.responses.custom.product_types_response import ProductTypeResponse
from sql.controllers.custom.product_types_controller import ProductTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_types_router = APIRouter()


@product_types_router.post(
    "/corrugation/product-types/create",
    response_model=ProductTypeResponse,
)
async def create_product_type(
    create_request: ProductTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductType record]

    Args:
        create_request (ProductTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductTypeController().create_product_type_controller(
                request=create_request
            )
            return ProductTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_types_router.post(
    "/corrugation/product-types/update",
    response_model=ProductTypeResponse,
)
async def update_product_type(
    update_request: ProductTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductType record]

    Args:
        update_request (ProductTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductTypeController().update_product_type_controller(
                request=update_request
            )
            return ProductTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_types_router.get(
    "/corrugation/product-types/list_all",
)
async def list_all_product_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-types/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductTypeController().get_all_product_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_types_router.get(
    "/corrugation/product-types/get",
    response_model=ProductTypeResponse,
)
async def get_product_type(
    product_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductType record]

    Args:
        product_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-types/get endpoint")
        if decodeJWT(token=token):
            response = ProductTypeController().get_product_type_controller(
                product_type_id=product_type_id
            )
            return ProductTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_types_router.delete("/corrugation/product-types/delete")
async def delete_product_type(
    product_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductType record]

    Args:
        product_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductTypeController().delete_product_type_controller(
                product_type_id=product_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
