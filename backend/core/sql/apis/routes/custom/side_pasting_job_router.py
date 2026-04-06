from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.side_pasting_job_request import SidePastingJobCreate, SidePastingJobUpdate
from sql.apis.schemas.responses.custom.side_pasting_job_response import SidePastingJobResponse
from sql.controllers.custom.side_pasting_job_controller import SidePastingJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
side_pasting_job_router = APIRouter()


@side_pasting_job_router.post(
    "/corrugation/side-pasting-job/create",
    response_model=SidePastingJobResponse,
)
async def create_side_pasting_job(
    create_request: SidePastingJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new SidePastingJob record]

    Args:
        create_request (SidePastingJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [SidePastingJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/side-pasting-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = SidePastingJobController().create_side_pasting_job_controller(
                request=create_request
            )
            return SidePastingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/side-pasting-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@side_pasting_job_router.post(
    "/corrugation/side-pasting-job/update",
    response_model=SidePastingJobResponse,
)
async def update_side_pasting_job(
    update_request: SidePastingJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a SidePastingJob record]

    Args:
        update_request (SidePastingJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [SidePastingJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/side-pasting-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = SidePastingJobController().update_side_pasting_job_controller(
                request=update_request
            )
            return SidePastingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/side-pasting-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@side_pasting_job_router.get(
    "/corrugation/side-pasting-job/list_all",
)
async def list_all_side_pasting_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all SidePastingJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/side-pasting-job/list_all endpoint")
        if decodeJWT(token=token):
            response = SidePastingJobController().get_all_side_pasting_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/side-pasting-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@side_pasting_job_router.get(
    "/corrugation/side-pasting-job/get",
    response_model=SidePastingJobResponse,
)
async def get_side_pasting_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific SidePastingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [SidePastingJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/side-pasting-job/get endpoint")
        if decodeJWT(token=token):
            response = SidePastingJobController().get_side_pasting_job_controller(
                job_id=job_id
            )
            return SidePastingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/side-pasting-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@side_pasting_job_router.delete("/corrugation/side-pasting-job/delete")
async def delete_side_pasting_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a SidePastingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/side-pasting-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return SidePastingJobController().delete_side_pasting_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/side-pasting-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
