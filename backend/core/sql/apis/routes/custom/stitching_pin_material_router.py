from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.stitching_pin_material_request import StitchingPinMaterialCreate, StitchingPinMaterialUpdate
from sql.apis.schemas.responses.custom.stitching_pin_material_response import StitchingPinMaterialResponse
from sql.controllers.custom.stitching_pin_material_controller import StitchingPinMaterialController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
stitching_pin_material_router = APIRouter()


@stitching_pin_material_router.post(
    "/corrugation/stitching-pin-material/create",
    response_model=StitchingPinMaterialResponse,
)
async def create_stitching_pin_material(
    create_request: StitchingPinMaterialCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new StitchingPinMaterial record]

    Args:
        create_request (StitchingPinMaterialCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingPinMaterialResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-material/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StitchingPinMaterialController().create_stitching_pin_material_controller(
                request=create_request
            )
            return StitchingPinMaterialResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-material/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_material_router.post(
    "/corrugation/stitching-pin-material/update",
    response_model=StitchingPinMaterialResponse,
)
async def update_stitching_pin_material(
    update_request: StitchingPinMaterialUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a StitchingPinMaterial record]

    Args:
        update_request (StitchingPinMaterialUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingPinMaterialResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-material/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = StitchingPinMaterialController().update_stitching_pin_material_controller(
                request=update_request
            )
            return StitchingPinMaterialResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-material/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_material_router.get(
    "/corrugation/stitching-pin-material/list_all",
)
async def list_all_stitching_pin_material(
    token: str = Depends(oauth2_scheme),
):
    """[Get all StitchingPinMaterial records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-material/list_all endpoint")
        if decodeJWT(token=token):
            response = StitchingPinMaterialController().get_all_stitching_pin_material_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-material/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_material_router.get(
    "/corrugation/stitching-pin-material/get",
    response_model=StitchingPinMaterialResponse,
)
async def get_stitching_pin_material(
    material_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific StitchingPinMaterial record]

    Args:
        material_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [StitchingPinMaterialResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-material/get endpoint")
        if decodeJWT(token=token):
            response = StitchingPinMaterialController().get_stitching_pin_material_controller(
                material_id=material_id
            )
            return StitchingPinMaterialResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-material/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@stitching_pin_material_router.delete("/corrugation/stitching-pin-material/delete")
async def delete_stitching_pin_material(
    material_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a StitchingPinMaterial record]

    Args:
        material_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/stitching-pin-material/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return StitchingPinMaterialController().delete_stitching_pin_material_controller(
                material_id=material_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/stitching-pin-material/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
