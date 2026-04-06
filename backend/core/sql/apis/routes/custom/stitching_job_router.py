from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.stitching_job_request import StitchingJobCreate, StitchingJobUpdate
from sql.apis.schemas.responses.custom.stitching_job_response import StitchingJobResponse
from sql.controllers.custom.stitching_job_controller import StitchingJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
stitching_job_router = APIRouter()


@stitching_job_router.post(
    "/corrugation/stitching-job/create",
    response_model=StitchingJobResponse,
)
async def create_stitching_job(
    create_request: StitchingJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new StitchingJob record]

    Args:
        create_request (StitchingJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/stitching-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StitchingJobController().create_stitching_job_controller(
                request=create_request
            )
            return StitchingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_job_router.post(
    "/corrugation/stitching-job/update",
    response_model=StitchingJobResponse,
)
async def update_stitching_job(
    update_request: StitchingJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a StitchingJob record]

    Args:
        update_request (StitchingJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/stitching-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StitchingJobController().update_stitching_job_controller(
                request=update_request
            )
            return StitchingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_job_router.get(
    "/corrugation/stitching-job/list_all",
)
async def list_all_stitching_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all StitchingJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/stitching-job/list_all endpoint")
        if decodeJWT(token=token):
            response = StitchingJobController().get_all_stitching_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_job_router.get(
    "/corrugation/stitching-job/get",
    response_model=StitchingJobResponse,
)
async def get_stitching_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific StitchingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/stitching-job/get endpoint")
        if decodeJWT(token=token):
            response = StitchingJobController().get_stitching_job_controller(
                job_id=job_id
            )
            return StitchingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_job_router.delete("/corrugation/stitching-job/delete")
async def delete_stitching_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a StitchingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/stitching-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return StitchingJobController().delete_stitching_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
