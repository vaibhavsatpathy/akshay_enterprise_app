from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.paper_types_request import PaperTypeCreate, PaperTypeUpdate
from sql.apis.schemas.responses.custom.paper_types_response import PaperTypeResponse
from sql.controllers.custom.paper_types_controller import PaperTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
paper_types_router = APIRouter()


@paper_types_router.post(
    "/corrugation/paper-types/create",
    response_model=PaperTypeResponse,
)
async def create_paper_type(
    create_request: PaperTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new PaperType record]

    Args:
        create_request (PaperTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PaperTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/paper-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PaperTypeController().create_paper_type_controller(
                request=create_request
            )
            return PaperTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@paper_types_router.post(
    "/corrugation/paper-types/update",
    response_model=PaperTypeResponse,
)
async def update_paper_type(
    update_request: PaperTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a PaperType record]

    Args:
        update_request (PaperTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PaperTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/paper-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PaperTypeController().update_paper_type_controller(
                request=update_request
            )
            return PaperTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@paper_types_router.get(
    "/corrugation/paper-types/list_all",
)
async def list_all_paper_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all PaperType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/paper-types/list_all endpoint")
        if decodeJWT(token=token):
            response = PaperTypeController().get_all_paper_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@paper_types_router.get(
    "/corrugation/paper-types/get",
    response_model=PaperTypeResponse,
)
async def get_paper_type(
    paper_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific PaperType record]

    Args:
        paper_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PaperTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/paper-types/get endpoint")
        if decodeJWT(token=token):
            response = PaperTypeController().get_paper_type_controller(
                paper_type_id=paper_type_id
            )
            return PaperTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@paper_types_router.delete("/corrugation/paper-types/delete")
async def delete_paper_type(
    paper_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a PaperType record]

    Args:
        paper_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/paper-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PaperTypeController().delete_paper_type_controller(
                paper_type_id=paper_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
