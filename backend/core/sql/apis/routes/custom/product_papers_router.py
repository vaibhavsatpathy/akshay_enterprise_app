from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_papers_request import ProductPaperCreate, ProductPaperUpdate
from sql.apis.schemas.responses.custom.product_papers_response import ProductPaperResponse
from sql.controllers.custom.product_papers_controller import ProductPaperController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_papers_router = APIRouter()


@product_papers_router.post(
    "/corrugation/product-papers/create",
    response_model=ProductPaperResponse,
)
async def create_product_paper(
    create_request: ProductPaperCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductPaper record]

    Args:
        create_request (ProductPaperCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductPaperResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-papers/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductPaperController().create_product_paper_controller(
                request=create_request
            )
            return ProductPaperResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-papers/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_papers_router.post(
    "/corrugation/product-papers/update",
    response_model=ProductPaperResponse,
)
async def update_product_paper(
    update_request: ProductPaperUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductPaper record]

    Args:
        update_request (ProductPaperUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductPaperResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-papers/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductPaperController().update_product_paper_controller(
                request=update_request
            )
            return ProductPaperResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-papers/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_papers_router.get(
    "/corrugation/product-papers/list_all",
)
async def list_all_product_paper(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductPaper records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-papers/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductPaperController().get_all_product_paper_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-papers/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_papers_router.get(
    "/corrugation/product-papers/get",
    response_model=ProductPaperResponse,
)
async def get_product_paper(
    gross_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductPaper record]

    Args:
        gross_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductPaperResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-papers/get endpoint")
        if decodeJWT(token=token):
            response = ProductPaperController().get_product_paper_controller(
                gross_id=gross_id
            )
            return ProductPaperResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-papers/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_papers_router.delete("/corrugation/product-papers/delete")
async def delete_product_paper(
    gross_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductPaper record]

    Args:
        gross_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-papers/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductPaperController().delete_product_paper_controller(
                gross_id=gross_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-papers/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
