from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.rotory_job_request import RotoryJobCreate, RotoryJobUpdate
from sql.apis.schemas.responses.custom.rotory_job_response import RotoryJobResponse
from sql.controllers.custom.rotory_job_controller import RotoryJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
rotory_job_router = APIRouter()


@rotory_job_router.post(
    "/corrugation/rotory-job/create",
    response_model=RotoryJobResponse,
)
async def create_rotory_job(
    create_request: RotoryJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new RotoryJob record]

    Args:
        create_request (RotoryJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RotoryJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/rotory-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = RotoryJobController().create_rotory_job_controller(
                request=create_request
            )
            return RotoryJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rotory-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rotory_job_router.post(
    "/corrugation/rotory-job/update",
    response_model=RotoryJobResponse,
)
async def update_rotory_job(
    update_request: RotoryJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a RotoryJob record]

    Args:
        update_request (RotoryJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RotoryJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/rotory-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = RotoryJobController().update_rotory_job_controller(
                request=update_request
            )
            return RotoryJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rotory-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rotory_job_router.get(
    "/corrugation/rotory-job/list_all",
)
async def list_all_rotory_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all RotoryJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/rotory-job/list_all endpoint")
        if decodeJWT(token=token):
            response = RotoryJobController().get_all_rotory_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rotory-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rotory_job_router.get(
    "/corrugation/rotory-job/get",
    response_model=RotoryJobResponse,
)
async def get_rotory_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific RotoryJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [RotoryJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/rotory-job/get endpoint")
        if decodeJWT(token=token):
            response = RotoryJobController().get_rotory_job_controller(
                job_id=job_id
            )
            return RotoryJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rotory-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@rotory_job_router.delete("/corrugation/rotory-job/delete")
async def delete_rotory_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a RotoryJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/rotory-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return RotoryJobController().delete_rotory_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/rotory-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
