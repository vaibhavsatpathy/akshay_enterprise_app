from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.slot_job_request import SlotJobCreate, SlotJobUpdate
from sql.apis.schemas.responses.custom.slot_job_response import SlotJobResponse
from sql.controllers.custom.slot_job_controller import SlotJobController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
slot_job_router = APIRouter()


@slot_job_router.post(
    "/corrugation/slot-job/create",
    response_model=SlotJobResponse,
)
async def create_slot_job(
    create_request: SlotJobCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new SlotJob record]

    Args:
        create_request (SlotJobCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [SlotJobResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/slot-job/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = SlotJobController().create_slot_job_controller(
                request=create_request
            )
            return SlotJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/slot-job/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@slot_job_router.post(
    "/corrugation/slot-job/update",
    response_model=SlotJobResponse,
)
async def update_slot_job(
    update_request: SlotJobUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a SlotJob record]

    Args:
        update_request (SlotJobUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [SlotJobResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/slot-job/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = SlotJobController().update_slot_job_controller(
                request=update_request
            )
            return SlotJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/slot-job/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@slot_job_router.get(
    "/corrugation/slot-job/list_all",
)
async def list_all_slot_job(
    token: str = Depends(oauth2_scheme),
):
    """[Get all SlotJob records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/slot-job/list_all endpoint")
        if decodeJWT(token=token):
            response = SlotJobController().get_all_slot_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/slot-job/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@slot_job_router.get(
    "/corrugation/slot-job/get",
    response_model=SlotJobResponse,
)
async def get_slot_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific SlotJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [SlotJobResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/slot-job/get endpoint")
        if decodeJWT(token=token):
            response = SlotJobController().get_slot_job_controller(
                job_id=job_id
            )
            return SlotJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/slot-job/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@slot_job_router.delete("/corrugation/slot-job/delete")
async def delete_slot_job(
    job_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a SlotJob record]

    Args:
        job_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/slot-job/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return SlotJobController().delete_slot_job_controller(
                job_id=job_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/slot-job/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
