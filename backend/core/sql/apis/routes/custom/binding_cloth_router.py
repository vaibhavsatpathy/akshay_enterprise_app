from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.binding_cloth_request import BindingClothCreate, BindingClothUpdate
from sql.apis.schemas.responses.custom.binding_cloth_response import BindingClothResponse
from sql.controllers.custom.binding_cloth_controller import BindingClothController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
binding_cloth_router = APIRouter()


@binding_cloth_router.post(
    "/corrugation/binding-cloth/create",
    response_model=BindingClothResponse,
)
async def create_binding_cloth(
    create_request: BindingClothCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new BindingCloth record]

    Args:
        create_request (BindingClothCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BindingClothResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/binding-cloth/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BindingClothController().create_binding_cloth_controller(
                request=create_request
            )
            return BindingClothResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/binding-cloth/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@binding_cloth_router.post(
    "/corrugation/binding-cloth/update",
    response_model=BindingClothResponse,
)
async def update_binding_cloth(
    update_request: BindingClothUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a BindingCloth record]

    Args:
        update_request (BindingClothUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BindingClothResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/binding-cloth/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = BindingClothController().update_binding_cloth_controller(
                request=update_request
            )
            return BindingClothResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/binding-cloth/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@binding_cloth_router.get(
    "/corrugation/binding-cloth/list_all",
)
async def list_all_binding_cloth(
    token: str = Depends(oauth2_scheme),
):
    """[Get all BindingCloth records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/binding-cloth/list_all endpoint")
        if decodeJWT(token=token):
            response = BindingClothController().get_all_binding_cloth_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/binding-cloth/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@binding_cloth_router.get(
    "/corrugation/binding-cloth/get",
    response_model=BindingClothResponse,
)
async def get_binding_cloth(
    cloth_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific BindingCloth record]

    Args:
        cloth_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [BindingClothResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/binding-cloth/get endpoint")
        if decodeJWT(token=token):
            response = BindingClothController().get_binding_cloth_controller(
                cloth_id=cloth_id
            )
            return BindingClothResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/binding-cloth/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@binding_cloth_router.delete("/corrugation/binding-cloth/delete")
async def delete_binding_cloth(
    cloth_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a BindingCloth record]

    Args:
        cloth_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/binding-cloth/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return BindingClothController().delete_binding_cloth_controller(
                cloth_id=cloth_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/binding-cloth/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
