from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.transporters_request import TransporterCreate, TransporterUpdate
from sql.apis.schemas.responses.custom.transporters_response import TransporterResponse
from sql.controllers.custom.transporters_controller import TransporterController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
transporters_router = APIRouter()


@transporters_router.post(
    "/corrugation/transporters/create",
    response_model=TransporterResponse,
)
async def create_transporter(
    create_request: TransporterCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Transporter record]

    Args:
        create_request (TransporterCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [TransporterResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/transporters/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = TransporterController().create_transporter_controller(
                request=create_request
            )
            return TransporterResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/transporters/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@transporters_router.post(
    "/corrugation/transporters/update",
    response_model=TransporterResponse,
)
async def update_transporter(
    update_request: TransporterUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Transporter record]

    Args:
        update_request (TransporterUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [TransporterResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/transporters/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = TransporterController().update_transporter_controller(
                request=update_request
            )
            return TransporterResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/transporters/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@transporters_router.get(
    "/corrugation/transporters/list_all",
)
async def list_all_transporter(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Transporter records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/transporters/list_all endpoint")
        if decodeJWT(token=token):
            response = TransporterController().get_all_transporter_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/transporters/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@transporters_router.get(
    "/corrugation/transporters/get",
    response_model=TransporterResponse,
)
async def get_transporter(
    transporter_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Transporter record]

    Args:
        transporter_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [TransporterResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/transporters/get endpoint")
        if decodeJWT(token=token):
            response = TransporterController().get_transporter_controller(
                transporter_id=transporter_id
            )
            return TransporterResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/transporters/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@transporters_router.delete("/corrugation/transporters/delete")
async def delete_transporter(
    transporter_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Transporter record]

    Args:
        transporter_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/transporters/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return TransporterController().delete_transporter_controller(
                transporter_id=transporter_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/transporters/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
