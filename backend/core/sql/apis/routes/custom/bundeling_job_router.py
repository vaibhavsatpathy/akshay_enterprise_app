from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.bundeling_job_request import BundelingJobCreate, BundelingJobUpdate
from sql.apis.schemas.responses.custom.bundeling_job_response import BundelingJobResponse
from sql.controllers.custom.bundeling_job_controller import BundelingJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
bundeling_job_router = APIRouter()


@bundeling_job_router.post(
    "/corrugation/bundeling-job/create",
    response_model=BundelingJobResponse,
)
async def create_bundeling_job(
    create_request: BundelingJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new BundelingJob record]

    Args:
        create_request (BundelingJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BundelingJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/bundeling-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BundelingJobController().create_bundeling_job_controller(
                request=create_request
            )
            return BundelingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundeling-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bundeling_job_router.post(
    "/corrugation/bundeling-job/update",
    response_model=BundelingJobResponse,
)
async def update_bundeling_job(
    update_request: BundelingJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a BundelingJob record]

    Args:
        update_request (BundelingJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BundelingJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/bundeling-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BundelingJobController().update_bundeling_job_controller(
                request=update_request
            )
            return BundelingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundeling-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bundeling_job_router.get(
    "/corrugation/bundeling-job/list_all",
)
async def list_all_bundeling_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all BundelingJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/bundeling-job/list_all endpoint")
        if decodeJWT(token=token):
            response = BundelingJobController().get_all_bundeling_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundeling-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bundeling_job_router.get(
    "/corrugation/bundeling-job/get",
    response_model=BundelingJobResponse,
)
async def get_bundeling_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific BundelingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BundelingJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/bundeling-job/get endpoint")
        if decodeJWT(token=token):
            response = BundelingJobController().get_bundeling_job_controller(
                job_id=job_id
            )
            return BundelingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundeling-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@bundeling_job_router.delete("/corrugation/bundeling-job/delete")
async def delete_bundeling_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a BundelingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/bundeling-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return BundelingJobController().delete_bundeling_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/bundeling-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
