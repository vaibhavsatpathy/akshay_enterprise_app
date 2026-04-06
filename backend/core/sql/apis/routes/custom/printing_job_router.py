from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.printing_job_request import PrintingJobCreate, PrintingJobUpdate
from sql.apis.schemas.responses.custom.printing_job_response import PrintingJobResponse
from sql.controllers.custom.printing_job_controller import PrintingJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
printing_job_router = APIRouter()


@printing_job_router.post(
    "/corrugation/printing-job/create",
    response_model=PrintingJobResponse,
)
async def create_printing_job(
    create_request: PrintingJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new PrintingJob record]

    Args:
        create_request (PrintingJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintingJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/printing-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PrintingJobController().create_printing_job_controller(
                request=create_request
            )
            return PrintingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_job_router.post(
    "/corrugation/printing-job/update",
    response_model=PrintingJobResponse,
)
async def update_printing_job(
    update_request: PrintingJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a PrintingJob record]

    Args:
        update_request (PrintingJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintingJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/printing-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PrintingJobController().update_printing_job_controller(
                request=update_request
            )
            return PrintingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_job_router.get(
    "/corrugation/printing-job/list_all",
)
async def list_all_printing_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all PrintingJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/printing-job/list_all endpoint")
        if decodeJWT(token=token):
            response = PrintingJobController().get_all_printing_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_job_router.get(
    "/corrugation/printing-job/get",
    response_model=PrintingJobResponse,
)
async def get_printing_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific PrintingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PrintingJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/printing-job/get endpoint")
        if decodeJWT(token=token):
            response = PrintingJobController().get_printing_job_controller(
                job_id=job_id
            )
            return PrintingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@printing_job_router.delete("/corrugation/printing-job/delete")
async def delete_printing_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a PrintingJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/printing-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PrintingJobController().delete_printing_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/printing-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
