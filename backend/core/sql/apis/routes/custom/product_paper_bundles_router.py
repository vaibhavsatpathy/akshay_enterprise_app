from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_paper_bundles_request import ProductPaperBundleCreate, ProductPaperBundleUpdate
from sql.apis.schemas.responses.custom.product_paper_bundles_response import ProductPaperBundleResponse
from sql.controllers.custom.product_paper_bundles_controller import ProductPaperBundleController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_paper_bundles_router = APIRouter()


@product_paper_bundles_router.post(
    "/corrugation/product-paper-bundles/create",
    response_model=ProductPaperBundleResponse,
)
async def create_product_paper_bundle(
    create_request: ProductPaperBundleCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductPaperBundle record]

    Args:
        create_request (ProductPaperBundleCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductPaperBundleResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-paper-bundles/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductPaperBundleController().create_product_paper_bundle_controller(
                request=create_request
            )
            return ProductPaperBundleResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-paper-bundles/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_paper_bundles_router.post(
    "/corrugation/product-paper-bundles/update",
    response_model=ProductPaperBundleResponse,
)
async def update_product_paper_bundle(
    update_request: ProductPaperBundleUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductPaperBundle record]

    Args:
        update_request (ProductPaperBundleUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductPaperBundleResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-paper-bundles/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductPaperBundleController().update_product_paper_bundle_controller(
                request=update_request
            )
            return ProductPaperBundleResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-paper-bundles/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_paper_bundles_router.get(
    "/corrugation/product-paper-bundles/list_all",
)
async def list_all_product_paper_bundle(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductPaperBundle records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-paper-bundles/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductPaperBundleController().get_all_product_paper_bundle_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-paper-bundles/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_paper_bundles_router.get(
    "/corrugation/product-paper-bundles/get",
    response_model=ProductPaperBundleResponse,
)
async def get_product_paper_bundle(
    bundle_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductPaperBundle record]

    Args:
        bundle_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductPaperBundleResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-paper-bundles/get endpoint")
        if decodeJWT(token=token):
            response = ProductPaperBundleController().get_product_paper_bundle_controller(
                bundle_id=bundle_id
            )
            return ProductPaperBundleResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-paper-bundles/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_paper_bundles_router.delete("/corrugation/product-paper-bundles/delete")
async def delete_product_paper_bundle(
    bundle_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductPaperBundle record]

    Args:
        bundle_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-paper-bundles/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductPaperBundleController().delete_product_paper_bundle_controller(
                bundle_id=bundle_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-paper-bundles/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
