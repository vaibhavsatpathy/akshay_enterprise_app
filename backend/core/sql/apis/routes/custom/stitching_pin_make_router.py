from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.stitching_pin_make_request import StitchingPinMakeCreate, StitchingPinMakeUpdate
from sql.apis.schemas.responses.custom.stitching_pin_make_response import StitchingPinMakeResponse
from sql.controllers.custom.stitching_pin_make_controller import StitchingPinMakeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
stitching_pin_make_router = APIRouter()


@stitching_pin_make_router.post(
    "/corrugation/stitching-pin-make/create",
    response_model=StitchingPinMakeResponse,
)
async def create_stitching_pin_make(
    create_request: StitchingPinMakeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new StitchingPinMake record]

    Args:
        create_request (StitchingPinMakeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingPinMakeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-make/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StitchingPinMakeController().create_stitching_pin_make_controller(
                request=create_request
            )
            return StitchingPinMakeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-make/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_make_router.post(
    "/corrugation/stitching-pin-make/update",
    response_model=StitchingPinMakeResponse,
)
async def update_stitching_pin_make(
    update_request: StitchingPinMakeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a StitchingPinMake record]

    Args:
        update_request (StitchingPinMakeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingPinMakeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-make/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StitchingPinMakeController().update_stitching_pin_make_controller(
                request=update_request
            )
            return StitchingPinMakeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-make/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_make_router.get(
    "/corrugation/stitching-pin-make/list_all",
)
async def list_all_stitching_pin_make(
    token: str = Depends(oauth2_scheme),
):
    """[Get all StitchingPinMake records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-make/list_all endpoint")
        if decodeJWT(token=token):
            response = StitchingPinMakeController().get_all_stitching_pin_make_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-make/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_make_router.get(
    "/corrugation/stitching-pin-make/get",
    response_model=StitchingPinMakeResponse,
)
async def get_stitching_pin_make(
    make_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific StitchingPinMake record]

    Args:
        make_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingPinMakeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-make/get endpoint")
        if decodeJWT(token=token):
            response = StitchingPinMakeController().get_stitching_pin_make_controller(
                make_id=make_id
            )
            return StitchingPinMakeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-make/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_make_router.delete("/corrugation/stitching-pin-make/delete")
async def delete_stitching_pin_make(
    make_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a StitchingPinMake record]

    Args:
        make_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-make/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return StitchingPinMakeController().delete_stitching_pin_make_controller(
                make_id=make_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-make/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
