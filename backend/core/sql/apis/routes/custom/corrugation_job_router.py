from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.corrugation_job_request import CorrugationJobCreate, CorrugationJobUpdate
from sql.apis.schemas.responses.custom.corrugation_job_response import CorrugationJobResponse
from sql.controllers.custom.corrugation_job_controller import CorrugationJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
corrugation_job_router = APIRouter()


@corrugation_job_router.post(
    "/corrugation/corrugation-job/create",
    response_model=CorrugationJobResponse,
)
async def create_corrugation_job(
    create_request: CorrugationJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new CorrugationJob record]

    Args:
        create_request (CorrugationJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [CorrugationJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/corrugation-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = CorrugationJobController().create_corrugation_job_controller(
                request=create_request
            )
            return CorrugationJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/corrugation-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@corrugation_job_router.post(
    "/corrugation/corrugation-job/update",
    response_model=CorrugationJobResponse,
)
async def update_corrugation_job(
    update_request: CorrugationJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a CorrugationJob record]

    Args:
        update_request (CorrugationJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [CorrugationJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/corrugation-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = CorrugationJobController().update_corrugation_job_controller(
                request=update_request
            )
            return CorrugationJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/corrugation-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@corrugation_job_router.get(
    "/corrugation/corrugation-job/list_all",
)
async def list_all_corrugation_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all CorrugationJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/corrugation-job/list_all endpoint")
        if decodeJWT(token=token):
            response = CorrugationJobController().get_all_corrugation_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/corrugation-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@corrugation_job_router.get(
    "/corrugation/corrugation-job/get",
    response_model=CorrugationJobResponse,
)
async def get_corrugation_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific CorrugationJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [CorrugationJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/corrugation-job/get endpoint")
        if decodeJWT(token=token):
            response = CorrugationJobController().get_corrugation_job_controller(
                job_id=job_id
            )
            return CorrugationJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/corrugation-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@corrugation_job_router.delete("/corrugation/corrugation-job/delete")
async def delete_corrugation_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a CorrugationJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/corrugation-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return CorrugationJobController().delete_corrugation_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/corrugation-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
