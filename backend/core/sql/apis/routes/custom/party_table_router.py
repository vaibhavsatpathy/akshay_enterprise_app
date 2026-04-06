from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.party_table_request import PartyCreate, PartyUpdate
from sql.apis.schemas.responses.custom.party_table_response import PartyResponse
from sql.controllers.custom.party_table_controller import PartyController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
party_table_router = APIRouter()


@party_table_router.post(
    "/corrugation/party-table/create",
    response_model=PartyResponse,
)
async def create_party(
    create_request: PartyCreate,
    token: str = Depends(oauth2_scheme),
):
    """[Create a new Party record]

    Args:
        create_request (PartyCreate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PartyResponse]: [Created record]
    """
    try:
        logging.info("Calling /corrugation/party-table/create endpoint")
        logging.debug(f"Request: {create_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PartyController().create_party_controller(
                request=create_request
            )
            return PartyResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/party-table/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@party_table_router.post(
    "/corrugation/party-table/update",
    response_model=PartyResponse,
)
async def update_party(
    update_request: PartyUpdate,
    token: str = Depends(oauth2_scheme),
):
    """[Update a Party record]

    Args:
        update_request (PartyUpdate): [Request body]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PartyResponse]: [Updated record]
    """
    try:
        logging.info("Calling /corrugation/party-table/update endpoint")
        logging.debug(f"Request: {update_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = PartyController().update_party_controller(
                request=update_request
            )
            return PartyResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/party-table/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@party_table_router.get(
    "/corrugation/party-table/list_all",
)
async def list_all_party(
    token: str = Depends(oauth2_scheme),
):
    """[Get all Party records]

    Args:
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [list]: [List of all records]
    """
    try:
        logging.info("Calling /corrugation/party-table/list_all endpoint")
        if decodeJWT(token=token):
            response = PartyController().get_all_party_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/party-table/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@party_table_router.get(
    "/corrugation/party-table/get",
    response_model=PartyResponse,
)
async def get_party(
    party_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Get a specific Party record]

    Args:
        party_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [PartyResponse]: [Record details]
    """
    try:
        logging.info("Calling /corrugation/party-table/get endpoint")
        if decodeJWT(token=token):
            response = PartyController().get_party_controller(
                party_id=party_id
            )
            return PartyResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/party-table/get endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@party_table_router.delete("/corrugation/party-table/delete")
async def delete_party(
    party_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[Delete a Party record]

    Args:
        party_id (int): [Primary key]
        token (str, optional): [Auth token]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized or Internal Server Error]

    Returns:
        [dict]: [Deleted record details]
    """
    try:
        logging.info("Calling /corrugation/party-table/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return PartyController().delete_party_controller(
                party_id=party_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /corrugation/party-table/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
