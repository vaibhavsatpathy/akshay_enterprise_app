from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.single_two_pieces_type_request import SingleTwoPiecesTypeCreate, SingleTwoPiecesTypeUpdate
from sql.apis.schemas.responses.custom.single_two_pieces_type_response import SingleTwoPiecesTypeResponse
from sql.controllers.custom.single_two_pieces_type_controller import SingleTwoPiecesTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
single_two_pieces_type_router = APIRouter()


@single_two_pieces_type_router.post(
    "/corrugation/single-two-pieces-type/create",
    response_model=SingleTwoPiecesTypeResponse,
)
async def create_single_two_pieces_type(
    create_request: SingleTwoPiecesTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new SingleTwoPiecesType record]

    Args:
        create_request (SingleTwoPiecesTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [SingleTwoPiecesTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/single-two-pieces-type/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = SingleTwoPiecesTypeController().create_single_two_pieces_type_controller(
                request=create_request
            )
            return SingleTwoPiecesTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/single-two-pieces-type/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@single_two_pieces_type_router.post(
    "/corrugation/single-two-pieces-type/update",
    response_model=SingleTwoPiecesTypeResponse,
)
async def update_single_two_pieces_type(
    update_request: SingleTwoPiecesTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a SingleTwoPiecesType record]

    Args:
        update_request (SingleTwoPiecesTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [SingleTwoPiecesTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/single-two-pieces-type/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = SingleTwoPiecesTypeController().update_single_two_pieces_type_controller(
                request=update_request
            )
            return SingleTwoPiecesTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/single-two-pieces-type/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@single_two_pieces_type_router.get(
    "/corrugation/single-two-pieces-type/list_all",
)
async def list_all_single_two_pieces_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all SingleTwoPiecesType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/single-two-pieces-type/list_all endpoint")
        if decodeJWT(token=token):
            response = SingleTwoPiecesTypeController().get_all_single_two_pieces_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/single-two-pieces-type/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@single_two_pieces_type_router.get(
    "/corrugation/single-two-pieces-type/get",
    response_model=SingleTwoPiecesTypeResponse,
)
async def get_single_two_pieces_type(
    single_two_pieces_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific SingleTwoPiecesType record]

    Args:
        single_two_pieces_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [SingleTwoPiecesTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/single-two-pieces-type/get endpoint")
        if decodeJWT(token=token):
            response = SingleTwoPiecesTypeController().get_single_two_pieces_type_controller(
                single_two_pieces_type_id=single_two_pieces_type_id
            )
            return SingleTwoPiecesTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/single-two-pieces-type/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@single_two_pieces_type_router.delete("/corrugation/single-two-pieces-type/delete")
async def delete_single_two_pieces_type(
    single_two_pieces_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a SingleTwoPiecesType record]

    Args:
        single_two_pieces_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/single-two-pieces-type/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return SingleTwoPiecesTypeController().delete_single_two_pieces_type_controller(
                single_two_pieces_type_id=single_two_pieces_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/single-two-pieces-type/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
