from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.shades_request import ShadeCreate, ShadeUpdate
from sql.apis.schemas.responses.custom.shades_response import ShadeResponse
from sql.controllers.custom.shades_controller import ShadeController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
shades_router = APIRouter()


@shades_router.post(
    "/corrugation/shades/create",
    response_model=ShadeResponse,
)
async def create_shade(
    create_request: ShadeCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Shade record]

    Args:
        create_request (ShadeCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ShadeResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/shades/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ShadeController().create_shade_controller(
                request=create_request
            )
            return ShadeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/shades/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@shades_router.post(
    "/corrugation/shades/update",
    response_model=ShadeResponse,
)
async def update_shade(
    update_request: ShadeUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Shade record]

    Args:
        update_request (ShadeUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ShadeResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/shades/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ShadeController().update_shade_controller(
                request=update_request
            )
            return ShadeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/shades/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@shades_router.get(
    "/corrugation/shades/list_all",
)
async def list_all_shade(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Shade records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/shades/list_all endpoint")
        if decodeJWT(token=token):
            response = ShadeController().get_all_shade_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/shades/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@shades_router.get(
    "/corrugation/shades/get",
    response_model=ShadeResponse,
)
async def get_shade(
    shade_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Shade record]

    Args:
        shade_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [ShadeResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/shades/get endpoint")
        if decodeJWT(token=token):
            response = ShadeController().get_shade_controller(
                shade_id=shade_id
            )
            return ShadeResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/shades/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@shades_router.delete("/corrugation/shades/delete")
async def delete_shade(
    shade_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Shade record]

    Args:
        shade_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/shades/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return ShadeController().delete_shade_controller(
                shade_id=shade_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/shades/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
