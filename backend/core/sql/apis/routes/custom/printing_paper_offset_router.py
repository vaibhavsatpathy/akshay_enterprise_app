from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.printing_paper_offset_request import PrintingPaperOffsetCreate, PrintingPaperOffsetUpdate
from sql.apis.schemas.responses.custom.printing_paper_offset_response import PrintingPaperOffsetResponse
from sql.controllers.custom.printing_paper_offset_controller import PrintingPaperOffsetController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
printing_paper_offset_router = APIRouter()


@printing_paper_offset_router.post(
    "/corrugation/printing-paper-offset/create",
    response_model=PrintingPaperOffsetResponse,
)
async def create_printing_paper_offset(
    create_request: PrintingPaperOffsetCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new PrintingPaperOffset record]

    Args:
        create_request (PrintingPaperOffsetCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintingPaperOffsetResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-offset/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PrintingPaperOffsetController().create_printing_paper_offset_controller(
                request=create_request
            )
            return PrintingPaperOffsetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-offset/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_paper_offset_router.post(
    "/corrugation/printing-paper-offset/update",
    response_model=PrintingPaperOffsetResponse,
)
async def update_printing_paper_offset(
    update_request: PrintingPaperOffsetUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a PrintingPaperOffset record]

    Args:
        update_request (PrintingPaperOffsetUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintingPaperOffsetResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-offset/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PrintingPaperOffsetController().update_printing_paper_offset_controller(
                request=update_request
            )
            return PrintingPaperOffsetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-offset/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_paper_offset_router.get(
    "/corrugation/printing-paper-offset/list_all",
)
async def list_all_printing_paper_offset(
    token: str = Depends(oauth2_scheme),
):
    """[Get all PrintingPaperOffset records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-offset/list_all endpoint")
        if decodeJWT(token=token):
            response = PrintingPaperOffsetController().get_all_printing_paper_offset_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-offset/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_paper_offset_router.get(
    "/corrugation/printing-paper-offset/get",
    response_model=PrintingPaperOffsetResponse,
)
async def get_printing_paper_offset(
    print_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific PrintingPaperOffset record]

    Args:
        print_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintingPaperOffsetResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-offset/get endpoint")
        if decodeJWT(token=token):
            response = PrintingPaperOffsetController().get_printing_paper_offset_controller(
                print_id=print_id
            )
            return PrintingPaperOffsetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-offset/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_paper_offset_router.delete("/corrugation/printing-paper-offset/delete")
async def delete_printing_paper_offset(
    print_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a PrintingPaperOffset record]

    Args:
        print_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-offset/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PrintingPaperOffsetController().delete_printing_paper_offset_controller(
                print_id=print_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-offset/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
