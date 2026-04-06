from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.chilai_job_request import ChilaiJobCreate, ChilaiJobUpdate
from sql.apis.schemas.responses.custom.chilai_job_response import ChilaiJobResponse
from sql.controllers.custom.chilai_job_controller import ChilaiJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
chilai_job_router = APIRouter()


@chilai_job_router.post(
    "/corrugation/chilai-job/create",
    response_model=ChilaiJobResponse,
)
async def create_chilai_job(
    create_request: ChilaiJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ChilaiJob record]

    Args:
        create_request (ChilaiJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ChilaiJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/chilai-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ChilaiJobController().create_chilai_job_controller(
                request=create_request
            )
            return ChilaiJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/chilai-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@chilai_job_router.post(
    "/corrugation/chilai-job/update",
    response_model=ChilaiJobResponse,
)
async def update_chilai_job(
    update_request: ChilaiJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ChilaiJob record]

    Args:
        update_request (ChilaiJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ChilaiJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/chilai-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ChilaiJobController().update_chilai_job_controller(
                request=update_request
            )
            return ChilaiJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/chilai-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@chilai_job_router.get(
    "/corrugation/chilai-job/list_all",
)
async def list_all_chilai_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ChilaiJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/chilai-job/list_all endpoint")
        if decodeJWT(token=token):
            response = ChilaiJobController().get_all_chilai_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/chilai-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@chilai_job_router.get(
    "/corrugation/chilai-job/get",
    response_model=ChilaiJobResponse,
)
async def get_chilai_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ChilaiJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ChilaiJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/chilai-job/get endpoint")
        if decodeJWT(token=token):
            response = ChilaiJobController().get_chilai_job_controller(
                job_id=job_id
            )
            return ChilaiJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/chilai-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@chilai_job_router.delete("/corrugation/chilai-job/delete")
async def delete_chilai_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ChilaiJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/chilai-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ChilaiJobController().delete_chilai_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/chilai-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
