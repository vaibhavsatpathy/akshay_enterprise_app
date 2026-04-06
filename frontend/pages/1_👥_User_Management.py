import streamlit as st
import json
from datetime import datetime
import sys
from pathlib import Path

# Add parent directory to path to import commons
sys.path.insert(0, str(Path(__file__).parent.parent))

from commons import (
    login,
    register_user,
    change_password,
    fetch_data,
    delete_record,
    API_BASE_URL,
)
import requests

# Page configuration
st.set_page_config(
    page_title="User Management - Accuracy Packaging", page_icon="👥", layout="wide"
)


# Custom CSS
st.markdown(
    """
<style>
    .login-box {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        max-width: 500px;
        margin: 0 auto;
    }
</style>
""",
    unsafe_allow_html=True,
)


def get_all_users():
    """Get list of all users"""
    return fetch_data("/user/list_all")


def delete_user(user_name, token):
    """Delete a user (Admin only)"""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(
            f"{API_BASE_URL}/user/delete",
            headers=headers,
            params={"user_name": user_name},
        )
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.json()
    except Exception as e:
        return False, {"detail": str(e)}


# Main UI
st.title("👥 User Management")

# Check if user is authenticated
# Note: We use the explicit check here (not check_authentication()) because
# this page needs to show the login form for unauthenticated users
if not st.session_state.get("authenticated", False):
    st.markdown("## 🔐 Login")

    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.markdown('<div class="login-box">', unsafe_allow_html=True)

            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            col_btn1, col_btn2 = st.columns(2)

            with col_btn1:
                if st.button("🔓 Login", use_container_width=True):
                    if username and password:
                        success, data = login(username, password)
                        if success:
                            st.session_state.authenticated = True
                            st.session_state.token = data["access_token"]
                            st.session_state.user_name = data["user_name"]
                            st.session_state.user_role = data.get("name", "User")
                            st.success("✅ Login successful!")
                            st.rerun()
                        else:
                            st.error(
                                f"❌ Login failed: {data.get('detail', 'Unknown error')}"
                            )
                    else:
                        st.warning("⚠️ Please enter both username and password")

            with col_btn2:
                if st.button("🔄 Clear", use_container_width=True):
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info(
        "💡 **Note:** Please login to access user management features. Default admin credentials should be configured during system setup."
    )

else:
    # User is authenticated
    st.success(f"✅ Logged in as: **{st.session_state.user_name}**")

    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.session_state.token = None
        st.session_state.user_name = None
        st.session_state.user_role = None
        st.rerun()

    st.markdown("---")

    # Tabs for different user management functions
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 All Users",
            "➕ Register User",
            "🔑 Change Password",
            "⚙️ Settings",
        ]
    )

    with tab1:
        st.subheader("📋 All Registered Users")

        if st.button("🔄 Refresh User List"):
            success, data = get_all_users()
            if success:
                st.session_state.users_list = data

        if "users_list" in st.session_state and st.session_state.users_list:
            # Display users in a table
            st.dataframe(
                st.session_state.users_list, use_container_width=True, hide_index=True
            )

            # Delete user section (Admin only)
            with st.expander("🗑️ Delete User (Admin Only)"):
                user_to_delete = st.selectbox(
                    "Select user to delete",
                    options=[
                        user.get("user_name", "")
                        for user in st.session_state.users_list
                    ],
                )

                if st.button("🗑️ Delete Selected User", type="primary"):
                    if user_to_delete:
                        success, data = delete_user(
                            user_to_delete, st.session_state.token
                        )
                        if success:
                            st.success(
                                f"✅ User '{user_to_delete}' deleted successfully!"
                            )
                            st.rerun()
                        else:
                            st.error(
                                f"❌ Failed to delete user: {data.get('detail', 'Unknown error')}"
                            )
        else:
            st.info("Click 'Refresh User List' to load users")

    with tab2:
        st.subheader("➕ Register New User (Admin Only)")

        with st.form("register_form"):
            col1, col2 = st.columns(2)

            with col1:
                new_username = st.text_input("Username*")
                new_full_name = st.text_input("Full Name*")
                new_email = st.text_input("Email*")

            with col2:
                new_password = st.text_input("Password*", type="password")
                new_role = st.selectbox("Role*", options=["admin", "editor", "viewer"])
                role_id_map = {"admin": 1, "editor": 2, "viewer": 3}
                new_role_id = role_id_map[new_role]

            submitted = st.form_submit_button(
                "➕ Register User", use_container_width=True
            )

            if submitted:
                if all([new_username, new_password, new_full_name, new_email]):
                    user_data = {
                        "user_name": new_username,
                        "password": new_password,
                        "full_name": new_full_name,
                        "email_id": new_email,
                        "role_name": new_role,
                        "role_id": new_role_id,
                    }
                    success, data = register_user(user_data)
                    if success:
                        st.success("✅ User registered successfully!")
                    else:
                        st.error(
                            f"❌ Registration failed: {data.get('detail', 'Unknown error')}"
                        )
                else:
                    st.warning("⚠️ Please fill in all required fields")

    with tab3:
        st.subheader("🔑 Change Password")

        with st.form("change_password_form"):
            current_password = st.text_input("Current Password*", type="password")
            new_pass = st.text_input("New Password*", type="password")
            confirm_pass = st.text_input("Confirm New Password*", type="password")

            submitted = st.form_submit_button(
                "🔑 Update Password", use_container_width=True
            )

            if submitted:
                if new_pass != confirm_pass:
                    st.error("❌ New passwords do not match!")
                elif all([current_password, new_pass]):
                    success, data = change_password(
                        st.session_state.user_name, current_password, new_pass
                    )
                    if success:
                        st.success("✅ Password updated successfully!")
                    else:
                        st.error(
                            f"❌ Password update failed: {data.get('detail', 'Unknown error')}"
                        )
                else:
                    st.warning("⚠️ Please fill in all fields")

    with tab4:
        st.subheader("⚙️ User Settings")

        st.info(
            f"""
        **Current User Information:**
        - Username: {st.session_state.user_name}
        - Role: {st.session_state.user_role}
        """
        )

        st.markdown("---")

        st.write("### 🔒 Security")
        st.write("- Your password is encrypted and secure")
        st.write("- Session token expires after inactivity")
        st.write("- All API calls are authenticated")
