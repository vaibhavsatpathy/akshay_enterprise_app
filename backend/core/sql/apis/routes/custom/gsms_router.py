from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.gsms_request import GsmCreate, GsmUpdate
from sql.apis.schemas.responses.custom.gsms_response import GsmResponse
from sql.controllers.custom.gsms_controller import GsmController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
gsms_router = APIRouter()


@gsms_router.post(
    "/corrugation/gsms/create",
    response_model=GsmResponse,
)
async def create_gsm(
    create_request: GsmCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Gsm record]

    Args:
        create_request (GsmCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [GsmResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/gsms/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = GsmController().create_gsm_controller(
                request=create_request
            )
            return GsmResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gsms/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gsms_router.post(
    "/corrugation/gsms/update",
    response_model=GsmResponse,
)
async def update_gsm(
    update_request: GsmUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Gsm record]

    Args:
        update_request (GsmUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [GsmResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/gsms/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = GsmController().update_gsm_controller(
                request=update_request
            )
            return GsmResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gsms/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gsms_router.get(
    "/corrugation/gsms/list_all",
)
async def list_all_gsm(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Gsm records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/gsms/list_all endpoint")
        if decodeJWT(token=token):
            response = GsmController().get_all_gsm_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gsms/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gsms_router.get(
    "/corrugation/gsms/get",
    response_model=GsmResponse,
)
async def get_gsm(
    gsm_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Gsm record]

    Args:
        gsm_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [GsmResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/gsms/get endpoint")
        if decodeJWT(token=token):
            response = GsmController().get_gsm_controller(
                gsm_id=gsm_id
            )
            return GsmResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gsms/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@gsms_router.delete("/corrugation/gsms/delete")
async def delete_gsm(
    gsm_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Gsm record]

    Args:
        gsm_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/gsms/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return GsmController().delete_gsm_controller(
                gsm_id=gsm_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/gsms/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
