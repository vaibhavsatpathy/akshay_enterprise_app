from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.pasting_job_request import PastingJobCreate, PastingJobUpdate
from sql.apis.schemas.responses.custom.pasting_job_response import PastingJobResponse
from sql.controllers.custom.pasting_job_controller import PastingJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
pasting_job_router = APIRouter()


@pasting_job_router.post(
    "/corrugation/pasting-job/create",
    response_model=PastingJobResponse,
)
async def create_pasting_job(
    create_request: PastingJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new PastingJob record]

    Args:
        create_request (PastingJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PastingJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/pasting-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PastingJobController().create_pasting_job_controller(
                request=create_request
            )
            return PastingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/pasting-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@pasting_job_router.post(
    "/corrugation/pasting-job/update",
    response_model=PastingJobResponse,
)
async def update_pasting_job(
    update_request: PastingJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a PastingJob record]

    Args:
        update_request (PastingJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PastingJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/pasting-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PastingJobController().update_pasting_job_controller(
                request=update_request
            )
            return PastingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/pasting-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@pasting_job_router.get(
    "/corrugation/pasting-job/list_all",
)
async def list_all_pasting_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all PastingJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/pasting-job/list_all endpoint")
        if decodeJWT(token=token):
            response = PastingJobController().get_all_pasting_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/pasting-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@pasting_job_router.get(
    "/corrugation/pasting-job/get",
    response_model=PastingJobResponse,
)
async def get_pasting_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific PastingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PastingJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/pasting-job/get endpoint")
        if decodeJWT(token=token):
            response = PastingJobController().get_pasting_job_controller(
                job_id=job_id
            )
            return PastingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/pasting-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@pasting_job_router.delete("/corrugation/pasting-job/delete")
async def delete_pasting_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a PastingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/pasting-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PastingJobController().delete_pasting_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/pasting-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
