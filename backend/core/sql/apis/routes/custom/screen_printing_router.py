from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.screen_printing_request import ScreenPrintingCreate, ScreenPrintingUpdate
from sql.apis.schemas.responses.custom.screen_printing_response import ScreenPrintingResponse
from sql.controllers.custom.screen_printing_controller import ScreenPrintingController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
screen_printing_router = APIRouter()


@screen_printing_router.post(
    "/corrugation/screen-printing/create",
    response_model=ScreenPrintingResponse,
)
async def create_screen_printing(
    create_request: ScreenPrintingCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ScreenPrinting record]

    Args:
        create_request (ScreenPrintingCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ScreenPrintingResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/screen-printing/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ScreenPrintingController().create_screen_printing_controller(
                request=create_request
            )
            return ScreenPrintingResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/screen-printing/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@screen_printing_router.post(
    "/corrugation/screen-printing/update",
    response_model=ScreenPrintingResponse,
)
async def update_screen_printing(
    update_request: ScreenPrintingUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ScreenPrinting record]

    Args:
        update_request (ScreenPrintingUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ScreenPrintingResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/screen-printing/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ScreenPrintingController().update_screen_printing_controller(
                request=update_request
            )
            return ScreenPrintingResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/screen-printing/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@screen_printing_router.get(
    "/corrugation/screen-printing/list_all",
)
async def list_all_screen_printing(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ScreenPrinting records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/screen-printing/list_all endpoint")
        if decodeJWT(token=token):
            response = ScreenPrintingController().get_all_screen_printing_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/screen-printing/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@screen_printing_router.get(
    "/corrugation/screen-printing/get",
    response_model=ScreenPrintingResponse,
)
async def get_screen_printing(
    print_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ScreenPrinting record]

    Args:
        print_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ScreenPrintingResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/screen-printing/get endpoint")
        if decodeJWT(token=token):
            response = ScreenPrintingController().get_screen_printing_controller(
                print_id=print_id
            )
            return ScreenPrintingResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/screen-printing/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@screen_printing_router.delete("/corrugation/screen-printing/delete")
async def delete_screen_printing(
    print_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ScreenPrinting record]

    Args:
        print_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/screen-printing/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ScreenPrintingController().delete_screen_printing_controller(
                print_id=print_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/screen-printing/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
