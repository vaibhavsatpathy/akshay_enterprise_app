from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.vendors_request import VendorCreate, VendorUpdate
from sql.apis.schemas.responses.custom.vendors_response import VendorResponse
from sql.controllers.custom.vendors_controller import VendorController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
vendors_router = APIRouter()


@vendors_router.post(
    "/corrugation/vendors/create",
    response_model=VendorResponse,
)
async def create_vendor(
    create_request: VendorCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Vendor record]

    Args:
        create_request (VendorCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [VendorResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/vendors/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = VendorController().create_vendor_controller(
                request=create_request
            )
            return VendorResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/vendors/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@vendors_router.post(
    "/corrugation/vendors/update",
    response_model=VendorResponse,
)
async def update_vendor(
    update_request: VendorUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Vendor record]

    Args:
        update_request (VendorUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [VendorResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/vendors/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = VendorController().update_vendor_controller(
                request=update_request
            )
            return VendorResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/vendors/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@vendors_router.get(
    "/corrugation/vendors/list_all",
)
async def list_all_vendor(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Vendor records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/vendors/list_all endpoint")
        if decodeJWT(token=token):
            response = VendorController().get_all_vendor_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/vendors/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@vendors_router.get(
    "/corrugation/vendors/get",
    response_model=VendorResponse,
)
async def get_vendor(
    vendor_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Vendor record]

    Args:
        vendor_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [VendorResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/vendors/get endpoint")
        if decodeJWT(token=token):
            response = VendorController().get_vendor_controller(
                vendor_id=vendor_id
            )
            return VendorResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/vendors/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@vendors_router.delete("/corrugation/vendors/delete")
async def delete_vendor(
    vendor_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Vendor record]

    Args:
        vendor_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/vendors/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return VendorController().delete_vendor_controller(
                vendor_id=vendor_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/vendors/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
