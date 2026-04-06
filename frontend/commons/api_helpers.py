"""
API Helper Functions for Streamlit Frontend
Contains common functions for interacting with the FastAPI backend
"""

import requests
import streamlit as st
from typing import Tuple, Dict, Any, Optional

# API Base URL
API_BASE_URL = "http://localhost:8080"


def get_auth_headers() -> Dict[str, str]:
    """
    Get authentication headers with JWT token from session state

    Returns:
        Dict[str, str]: Headers dictionary with Authorization token
    """
    if st.session_state.get("token"):
        return {"Authorization": f"Bearer {st.session_state.token}"}
    return {}


def fetch_data(endpoint: str) -> Tuple[bool, Any]:
    """
    Fetch data from API endpoint

    Args:
        endpoint (str): API endpoint path (e.g., '/corrugation/inventory/list_all')

    Returns:
        Tuple[bool, Any]: (success, data) - success is True if request succeeded,
                          data is the JSON response or error details
    """
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", headers=get_auth_headers())
        return (
            (True, response.json())
            if response.status_code == 200
            else (False, response.json())
        )
    except Exception as e:
        return False, {"detail": str(e)}


def create_record(endpoint: str, data: Dict[str, Any]) -> Tuple[bool, Any]:
    """
    Create a new record via API

    Args:
        endpoint (str): API endpoint path (e.g., '/corrugation/inventory/create')
        data (Dict[str, Any]): Data dictionary to send in request body

    Returns:
        Tuple[bool, Any]: (success, response) - success is True if create succeeded,
                          response is the created object or error details
    """
    try:
        response = requests.post(
            f"{API_BASE_URL}{endpoint}",
            headers=get_auth_headers(),
            json=data,
        )
        return (
            (True, response.json())
            if response.status_code == 200
            else (False, response.json())
        )
    except Exception as e:
        return False, {"detail": str(e)}


def update_record(
    endpoint: str, record_id: int, data: Dict[str, Any]
) -> Tuple[bool, Any]:
    """
    Update an existing record via API

    Args:
        endpoint (str): API endpoint path (e.g., '/corrugation/inventory')
        record_id (int): ID of the record to update
        data (Dict[str, Any]): Data dictionary with fields to update

    Returns:
        Tuple[bool, Any]: (success, response) - success is True if update succeeded,
                          response is the updated object or error details
    """
    try:
        response = requests.put(
            f"{API_BASE_URL}{endpoint}/{record_id}",
            headers=get_auth_headers(),
            json=data,
        )
        return (
            (True, response.json())
            if response.status_code == 200
            else (False, response.json())
        )
    except Exception as e:
        return False, {"detail": str(e)}


def delete_record(endpoint: str, record_id: int) -> bool:
    """
    Delete a record via API

    Args:
        endpoint (str): API endpoint path (e.g., '/corrugation/inventory/delete')
        record_id (int): ID of the record to delete

    Returns:
        bool: True if delete succeeded, False otherwise
    """
    try:
        response = requests.delete(
            f"{API_BASE_URL}{endpoint}/{record_id}", headers=get_auth_headers()
        )
        return response.status_code == 200
    except Exception as e:
        return False


def login(username: str, password: str) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """
    Authenticate user and get JWT token

    Args:
        username (str): User's username
        password (str): User's password

    Returns:
        Tuple[bool, Optional[Dict]]: (success, token_data) - success is True if login succeeded,
                                      token_data contains access_token and token_type
    """
    try:
        response = requests.post(
            f"{API_BASE_URL}/user/login",
            data={"username": username, "password": password},
        )

        if response.status_code == 200:
            return True, response.json()
        else:
            return False, None
    except Exception as e:
        st.error(f"Login error: {str(e)}")
        return False, None


def register_user(user_data: Dict[str, Any]) -> Tuple[bool, Any]:
    """
    Register a new user (admin only)

    Args:
        user_data (Dict[str, Any]): User data including username, password, full_name, role_id

    Returns:
        Tuple[bool, Any]: (success, response) - success is True if registration succeeded
    """
    return create_record("/user/register", user_data)


def change_password(
    username: str, old_password: str, new_password: str
) -> Tuple[bool, Any]:
    """
    Change user password

    Args:
        username (str): Username
        old_password (str): Current password
        new_password (str): New password

    Returns:
        Tuple[bool, Any]: (success, response) - success is True if password changed
    """
    try:
        response = requests.post(
            f"{API_BASE_URL}/user/update_password",
            headers=get_auth_headers(),
            json={
                "user_name": username,
                "old_password": old_password,
                "new_password": new_password,
            },
        )
        return (
            (True, response.json())
            if response.status_code == 200
            else (False, response.json())
        )
    except Exception as e:
        return False, {"detail": str(e)}
