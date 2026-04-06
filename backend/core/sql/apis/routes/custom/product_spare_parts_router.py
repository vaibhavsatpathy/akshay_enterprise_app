from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_spare_parts_request import ProductSparePartCreate, ProductSparePartUpdate
from sql.apis.schemas.responses.custom.product_spare_parts_response import ProductSparePartResponse
from sql.controllers.custom.product_spare_parts_controller import ProductSparePartController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_spare_parts_router = APIRouter()


@product_spare_parts_router.post(
    "/corrugation/product-spare-parts/create",
    response_model=ProductSparePartResponse,
)
async def create_product_spare_part(
    create_request: ProductSparePartCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductSparePart record]

    Args:
        create_request (ProductSparePartCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductSparePartResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-spare-parts/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductSparePartController().create_product_spare_part_controller(
                request=create_request
            )
            return ProductSparePartResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-spare-parts/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_spare_parts_router.post(
    "/corrugation/product-spare-parts/update",
    response_model=ProductSparePartResponse,
)
async def update_product_spare_part(
    update_request: ProductSparePartUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductSparePart record]

    Args:
        update_request (ProductSparePartUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductSparePartResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-spare-parts/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductSparePartController().update_product_spare_part_controller(
                request=update_request
            )
            return ProductSparePartResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-spare-parts/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_spare_parts_router.get(
    "/corrugation/product-spare-parts/list_all",
)
async def list_all_product_spare_part(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductSparePart records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-spare-parts/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductSparePartController().get_all_product_spare_part_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-spare-parts/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_spare_parts_router.get(
    "/corrugation/product-spare-parts/get",
    response_model=ProductSparePartResponse,
)
async def get_product_spare_part(
    part_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductSparePart record]

    Args:
        part_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductSparePartResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-spare-parts/get endpoint")
        if decodeJWT(token=token):
            response = ProductSparePartController().get_product_spare_part_controller(
                part_id=part_id
            )
            return ProductSparePartResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-spare-parts/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_spare_parts_router.delete("/corrugation/product-spare-parts/delete")
async def delete_product_spare_part(
    part_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductSparePart record]

    Args:
        part_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-spare-parts/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductSparePartController().delete_product_spare_part_controller(
                part_id=part_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-spare-parts/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
