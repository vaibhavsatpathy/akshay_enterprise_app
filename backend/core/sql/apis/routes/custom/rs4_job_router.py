from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.rs4_job_request import Rs4JobCreate, Rs4JobUpdate
from sql.apis.schemas.responses.custom.rs4_job_response import Rs4JobResponse
from sql.controllers.custom.rs4_job_controller import Rs4JobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
rs4_job_router = APIRouter()


@rs4_job_router.post(
    "/corrugation/rs4-job/create",
    response_model=Rs4JobResponse,
)
async def create_rs4_job(
    create_request: Rs4JobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Rs4Job record]

    Args:
        create_request (Rs4JobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [Rs4JobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/rs4-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = Rs4JobController().create_rs4_job_controller(
                request=create_request
            )
            return Rs4JobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rs4-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rs4_job_router.post(
    "/corrugation/rs4-job/update",
    response_model=Rs4JobResponse,
)
async def update_rs4_job(
    update_request: Rs4JobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Rs4Job record]

    Args:
        update_request (Rs4JobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [Rs4JobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/rs4-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = Rs4JobController().update_rs4_job_controller(
                request=update_request
            )
            return Rs4JobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rs4-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rs4_job_router.get(
    "/corrugation/rs4-job/list_all",
)
async def list_all_rs4_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Rs4Job records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/rs4-job/list_all endpoint")
        if decodeJWT(token=token):
            response = Rs4JobController().get_all_rs4_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rs4-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rs4_job_router.get(
    "/corrugation/rs4-job/get",
    response_model=Rs4JobResponse,
)
async def get_rs4_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Rs4Job record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [Rs4JobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/rs4-job/get endpoint")
        if decodeJWT(token=token):
            response = Rs4JobController().get_rs4_job_controller(
                job_id=job_id
            )
            return Rs4JobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rs4-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rs4_job_router.delete("/corrugation/rs4-job/delete")
async def delete_rs4_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Rs4Job record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/rs4-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return Rs4JobController().delete_rs4_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rs4-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
