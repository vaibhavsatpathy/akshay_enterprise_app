from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.print_plain_style_request import PrintPlainStyleCreate, PrintPlainStyleUpdate
from sql.apis.schemas.responses.custom.print_plain_style_response import PrintPlainStyleResponse
from sql.controllers.custom.print_plain_style_controller import PrintPlainStyleController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
print_plain_style_router = APIRouter()


@print_plain_style_router.post(
    "/corrugation/print-plain-style/create",
    response_model=PrintPlainStyleResponse,
)
async def create_print_plain_style(
    create_request: PrintPlainStyleCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new PrintPlainStyle record]

    Args:
        create_request (PrintPlainStyleCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintPlainStyleResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/print-plain-style/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PrintPlainStyleController().create_print_plain_style_controller(
                request=create_request
            )
            return PrintPlainStyleResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/print-plain-style/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@print_plain_style_router.post(
    "/corrugation/print-plain-style/update",
    response_model=PrintPlainStyleResponse,
)
async def update_print_plain_style(
    update_request: PrintPlainStyleUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a PrintPlainStyle record]

    Args:
        update_request (PrintPlainStyleUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintPlainStyleResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/print-plain-style/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PrintPlainStyleController().update_print_plain_style_controller(
                request=update_request
            )
            return PrintPlainStyleResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/print-plain-style/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@print_plain_style_router.get(
    "/corrugation/print-plain-style/list_all",
)
async def list_all_print_plain_style(
    token: str = Depends(oauth2_scheme),
):
    """[Get all PrintPlainStyle records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/print-plain-style/list_all endpoint")
        if decodeJWT(token=token):
            response = PrintPlainStyleController().get_all_print_plain_style_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/print-plain-style/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@print_plain_style_router.get(
    "/corrugation/print-plain-style/get",
    response_model=PrintPlainStyleResponse,
)
async def get_print_plain_style(
    print_plain_style_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific PrintPlainStyle record]

    Args:
        print_plain_style_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintPlainStyleResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/print-plain-style/get endpoint")
        if decodeJWT(token=token):
            response = PrintPlainStyleController().get_print_plain_style_controller(
                print_plain_style_id=print_plain_style_id
            )
            return PrintPlainStyleResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/print-plain-style/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@print_plain_style_router.delete("/corrugation/print-plain-style/delete")
async def delete_print_plain_style(
    print_plain_style_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a PrintPlainStyle record]

    Args:
        print_plain_style_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/print-plain-style/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PrintPlainStyleController().delete_print_plain_style_controller(
                print_plain_style_id=print_plain_style_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/print-plain-style/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
