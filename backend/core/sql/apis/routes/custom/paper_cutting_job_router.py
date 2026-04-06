from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.paper_cutting_job_request import PaperCuttingJobCreate, PaperCuttingJobUpdate
from sql.apis.schemas.responses.custom.paper_cutting_job_response import PaperCuttingJobResponse
from sql.controllers.custom.paper_cutting_job_controller import PaperCuttingJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
paper_cutting_job_router = APIRouter()


@paper_cutting_job_router.post(
    "/corrugation/paper-cutting-job/create",
    response_model=PaperCuttingJobResponse,
)
async def create_paper_cutting_job(
    create_request: PaperCuttingJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new PaperCuttingJob record]

    Args:
        create_request (PaperCuttingJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PaperCuttingJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/paper-cutting-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PaperCuttingJobController().create_paper_cutting_job_controller(
                request=create_request
            )
            return PaperCuttingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-cutting-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@paper_cutting_job_router.post(
    "/corrugation/paper-cutting-job/update",
    response_model=PaperCuttingJobResponse,
)
async def update_paper_cutting_job(
    update_request: PaperCuttingJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a PaperCuttingJob record]

    Args:
        update_request (PaperCuttingJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PaperCuttingJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/paper-cutting-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PaperCuttingJobController().update_paper_cutting_job_controller(
                request=update_request
            )
            return PaperCuttingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-cutting-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@paper_cutting_job_router.get(
    "/corrugation/paper-cutting-job/list_all",
)
async def list_all_paper_cutting_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all PaperCuttingJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/paper-cutting-job/list_all endpoint")
        if decodeJWT(token=token):
            response = PaperCuttingJobController().get_all_paper_cutting_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-cutting-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@paper_cutting_job_router.get(
    "/corrugation/paper-cutting-job/get",
    response_model=PaperCuttingJobResponse,
)
async def get_paper_cutting_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific PaperCuttingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PaperCuttingJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/paper-cutting-job/get endpoint")
        if decodeJWT(token=token):
            response = PaperCuttingJobController().get_paper_cutting_job_controller(
                job_id=job_id
            )
            return PaperCuttingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-cutting-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@paper_cutting_job_router.delete("/corrugation/paper-cutting-job/delete")
async def delete_paper_cutting_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a PaperCuttingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/paper-cutting-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PaperCuttingJobController().delete_paper_cutting_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/paper-cutting-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
