from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.die_punching_job_request import DiePunchingJobCreate, DiePunchingJobUpdate
from sql.apis.schemas.responses.custom.die_punching_job_response import DiePunchingJobResponse
from sql.controllers.custom.die_punching_job_controller import DiePunchingJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
die_punching_job_router = APIRouter()


@die_punching_job_router.post(
    "/corrugation/die-punching-job/create",
    response_model=DiePunchingJobResponse,
)
async def create_die_punching_job(
    create_request: DiePunchingJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new DiePunchingJob record]

    Args:
        create_request (DiePunchingJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DiePunchingJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/die-punching-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = DiePunchingJobController().create_die_punching_job_controller(
                request=create_request
            )
            return DiePunchingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die-punching-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@die_punching_job_router.post(
    "/corrugation/die-punching-job/update",
    response_model=DiePunchingJobResponse,
)
async def update_die_punching_job(
    update_request: DiePunchingJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a DiePunchingJob record]

    Args:
        update_request (DiePunchingJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DiePunchingJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/die-punching-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = DiePunchingJobController().update_die_punching_job_controller(
                request=update_request
            )
            return DiePunchingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die-punching-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@die_punching_job_router.get(
    "/corrugation/die-punching-job/list_all",
)
async def list_all_die_punching_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all DiePunchingJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/die-punching-job/list_all endpoint")
        if decodeJWT(token=token):
            response = DiePunchingJobController().get_all_die_punching_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die-punching-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@die_punching_job_router.get(
    "/corrugation/die-punching-job/get",
    response_model=DiePunchingJobResponse,
)
async def get_die_punching_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific DiePunchingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [DiePunchingJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/die-punching-job/get endpoint")
        if decodeJWT(token=token):
            response = DiePunchingJobController().get_die_punching_job_controller(
                job_id=job_id
            )
            return DiePunchingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die-punching-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@die_punching_job_router.delete("/corrugation/die-punching-job/delete")
async def delete_die_punching_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a DiePunchingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/die-punching-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return DiePunchingJobController().delete_die_punching_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/die-punching-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
