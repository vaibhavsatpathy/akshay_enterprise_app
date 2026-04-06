from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.color_job_types_request import ColorJobTypeCreate, ColorJobTypeUpdate
from sql.apis.schemas.responses.custom.color_job_types_response import ColorJobTypeResponse
from sql.controllers.custom.color_job_types_controller import ColorJobTypeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
color_job_types_router = APIRouter()


@color_job_types_router.post(
    "/corrugation/color-job-types/create",
    response_model=ColorJobTypeResponse,
)
async def create_color_job_type(
    create_request: ColorJobTypeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new ColorJobType record]

    Args:
        create_request (ColorJobTypeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ColorJobTypeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/color-job-types/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ColorJobTypeController().create_color_job_type_controller(
                request=create_request
            )
            return ColorJobTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-job-types/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@color_job_types_router.post(
    "/corrugation/color-job-types/update",
    response_model=ColorJobTypeResponse,
)
async def update_color_job_type(
    update_request: ColorJobTypeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a ColorJobType record]

    Args:
        update_request (ColorJobTypeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ColorJobTypeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/color-job-types/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ColorJobTypeController().update_color_job_type_controller(
                request=update_request
            )
            return ColorJobTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-job-types/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@color_job_types_router.get(
    "/corrugation/color-job-types/list_all",
)
async def list_all_color_job_type(
    token: str = Depends(oauth2_scheme),
):
    """[Get all ColorJobType records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/color-job-types/list_all endpoint")
        if decodeJWT(token=token):
            response = ColorJobTypeController().get_all_color_job_type_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-job-types/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@color_job_types_router.get(
    "/corrugation/color-job-types/get",
    response_model=ColorJobTypeResponse,
)
async def get_color_job_type(
    color_job_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific ColorJobType record]

    Args:
        color_job_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ColorJobTypeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/color-job-types/get endpoint")
        if decodeJWT(token=token):
            response = ColorJobTypeController().get_color_job_type_controller(
                color_job_type_id=color_job_type_id
            )
            return ColorJobTypeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-job-types/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@color_job_types_router.delete("/corrugation/color-job-types/delete")
async def delete_color_job_type(
    color_job_type_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a ColorJobType record]

    Args:
        color_job_type_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/color-job-types/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ColorJobTypeController().delete_color_job_type_controller(
                color_job_type_id=color_job_type_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/color-job-types/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
