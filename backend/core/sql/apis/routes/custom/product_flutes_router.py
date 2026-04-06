from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_flutes_request import ProductFluteCreate, ProductFluteUpdate
from sql.apis.schemas.responses.custom.product_flutes_response import ProductFluteResponse
from sql.controllers.custom.product_flutes_controller import ProductFluteController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_flutes_router = APIRouter()


@product_flutes_router.post(
    "/corrugation/product-flutes/create",
    response_model=ProductFluteResponse,
)
async def create_product_flute(
    create_request: ProductFluteCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductFlute record]

    Args:
        create_request (ProductFluteCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductFluteResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-flutes/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductFluteController().create_product_flute_controller(
                request=create_request
            )
            return ProductFluteResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-flutes/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_flutes_router.post(
    "/corrugation/product-flutes/update",
    response_model=ProductFluteResponse,
)
async def update_product_flute(
    update_request: ProductFluteUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductFlute record]

    Args:
        update_request (ProductFluteUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductFluteResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-flutes/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductFluteController().update_product_flute_controller(
                request=update_request
            )
            return ProductFluteResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-flutes/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_flutes_router.get(
    "/corrugation/product-flutes/list_all",
)
async def list_all_product_flute(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductFlute records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-flutes/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductFluteController().get_all_product_flute_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-flutes/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_flutes_router.get(
    "/corrugation/product-flutes/get",
    response_model=ProductFluteResponse,
)
async def get_product_flute(
    flute_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductFlute record]

    Args:
        flute_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductFluteResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-flutes/get endpoint")
        if decodeJWT(token=token):
            response = ProductFluteController().get_product_flute_controller(
                flute_id=flute_id
            )
            return ProductFluteResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-flutes/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_flutes_router.delete("/corrugation/product-flutes/delete")
async def delete_product_flute(
    flute_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductFlute record]

    Args:
        flute_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-flutes/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductFluteController().delete_product_flute_controller(
                flute_id=flute_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-flutes/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
