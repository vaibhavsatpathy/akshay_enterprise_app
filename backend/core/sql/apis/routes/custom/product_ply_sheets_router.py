from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.product_ply_sheets_request import ProductPlySheetCreate, ProductPlySheetUpdate
from sql.apis.schemas.responses.custom.product_ply_sheets_response import ProductPlySheetResponse
from sql.controllers.custom.product_ply_sheets_controller import ProductPlySheetController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
product_ply_sheets_router = APIRouter()


@product_ply_sheets_router.post(
    "/corrugation/product-ply-sheets/create",
    response_model=ProductPlySheetResponse,
)
async def create_product_ply_sheet(
    create_request: ProductPlySheetCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ProductPlySheet record]

    Args:
        create_request (ProductPlySheetCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductPlySheetResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/product-ply-sheets/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductPlySheetController().create_product_ply_sheet_controller(
                request=create_request
            )
            return ProductPlySheetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-ply-sheets/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_ply_sheets_router.post(
    "/corrugation/product-ply-sheets/update",
    response_model=ProductPlySheetResponse,
)
async def update_product_ply_sheet(
    update_request: ProductPlySheetUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ProductPlySheet record]

    Args:
        update_request (ProductPlySheetUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductPlySheetResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/product-ply-sheets/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ProductPlySheetController().update_product_ply_sheet_controller(
                request=update_request
            )
            return ProductPlySheetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-ply-sheets/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_ply_sheets_router.get(
    "/corrugation/product-ply-sheets/list_all",
)
async def list_all_product_ply_sheet(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ProductPlySheet records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/product-ply-sheets/list_all endpoint")
        if decodeJWT(token=token):
            response = ProductPlySheetController().get_all_product_ply_sheet_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-ply-sheets/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_ply_sheets_router.get(
    "/corrugation/product-ply-sheets/get",
    response_model=ProductPlySheetResponse,
)
async def get_product_ply_sheet(
    sheet_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ProductPlySheet record]

    Args:
        sheet_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ProductPlySheetResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/product-ply-sheets/get endpoint")
        if decodeJWT(token=token):
            response = ProductPlySheetController().get_product_ply_sheet_controller(
                sheet_id=sheet_id
            )
            return ProductPlySheetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-ply-sheets/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@product_ply_sheets_router.delete("/corrugation/product-ply-sheets/delete")
async def delete_product_ply_sheet(
    sheet_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ProductPlySheet record]

    Args:
        sheet_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/product-ply-sheets/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ProductPlySheetController().delete_product_ply_sheet_controller(
                sheet_id=sheet_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/product-ply-sheets/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
