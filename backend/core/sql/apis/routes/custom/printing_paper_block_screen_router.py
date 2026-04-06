from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.printing_paper_block_screen_request import PrintingPaperBlockScreenCreate, PrintingPaperBlockScreenUpdate
from sql.apis.schemas.responses.custom.printing_paper_block_screen_response import PrintingPaperBlockScreenResponse
from sql.controllers.custom.printing_paper_block_screen_controller import PrintingPaperBlockScreenController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
printing_paper_block_screen_router = APIRouter()


@printing_paper_block_screen_router.post(
    "/corrugation/printing-paper-block-screen/create",
    response_model=PrintingPaperBlockScreenResponse,
)
async def create_printing_paper_block_screen(
    create_request: PrintingPaperBlockScreenCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new PrintingPaperBlockScreen record]

    Args:
        create_request (PrintingPaperBlockScreenCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintingPaperBlockScreenResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-block-screen/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PrintingPaperBlockScreenController().create_printing_paper_block_screen_controller(
                request=create_request
            )
            return PrintingPaperBlockScreenResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-block-screen/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_paper_block_screen_router.post(
    "/corrugation/printing-paper-block-screen/update",
    response_model=PrintingPaperBlockScreenResponse,
)
async def update_printing_paper_block_screen(
    update_request: PrintingPaperBlockScreenUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a PrintingPaperBlockScreen record]

    Args:
        update_request (PrintingPaperBlockScreenUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintingPaperBlockScreenResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-block-screen/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PrintingPaperBlockScreenController().update_printing_paper_block_screen_controller(
                request=update_request
            )
            return PrintingPaperBlockScreenResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-block-screen/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_paper_block_screen_router.get(
    "/corrugation/printing-paper-block-screen/list_all",
)
async def list_all_printing_paper_block_screen(
    token: str = Depends(oauth2_scheme),
):
    """[Get all PrintingPaperBlockScreen records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-block-screen/list_all endpoint")
        if decodeJWT(token=token):
            response = PrintingPaperBlockScreenController().get_all_printing_paper_block_screen_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-block-screen/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_paper_block_screen_router.get(
    "/corrugation/printing-paper-block-screen/get",
    response_model=PrintingPaperBlockScreenResponse,
)
async def get_printing_paper_block_screen(
    print_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific PrintingPaperBlockScreen record]

    Args:
        print_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintingPaperBlockScreenResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-block-screen/get endpoint")
        if decodeJWT(token=token):
            response = PrintingPaperBlockScreenController().get_printing_paper_block_screen_controller(
                print_id=print_id
            )
            return PrintingPaperBlockScreenResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-block-screen/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_paper_block_screen_router.delete("/corrugation/printing-paper-block-screen/delete")
async def delete_printing_paper_block_screen(
    print_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a PrintingPaperBlockScreen record]

    Args:
        print_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/printing-paper-block-screen/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PrintingPaperBlockScreenController().delete_printing_paper_block_screen_controller(
                print_id=print_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-paper-block-screen/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
