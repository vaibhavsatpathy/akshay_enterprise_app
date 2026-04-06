"""
UI Helper Functions for Streamlit Frontend
Contains common UI components and utilities
"""

import streamlit as st
from typing import Optional


def check_authentication() -> bool:
    """
    Check if user is authenticated and display warning if not

    Returns:
        bool: True if authenticated, False otherwise
    """
    if not st.session_state.get("authenticated", False):
        st.warning(
            "⚠️ Please login from the User Management page to access this feature"
        )
        st.stop()
        return False
    return True


def display_user_info():
    """
    Display logged-in user information
    """
    if st.session_state.get("authenticated", False):
        st.success(f"✅ Logged in as: **{st.session_state.user_name}**")


def display_metrics(data_frame, metric_configs: list):
    """
    Display metrics in columns

    Args:
        data_frame: Pandas DataFrame containing the data
        metric_configs: List of dicts with 'label', 'column', 'aggregation' keys

    Example:
        metric_configs = [
            {'label': 'Total Records', 'value': len(df)},
            {'label': 'Total Weight', 'column': 'weight', 'aggregation': 'sum', 'format': '{:.2f}'},
        ]
    """
    cols = st.columns(len(metric_configs))

    for idx, config in enumerate(metric_configs):
        with cols[idx]:
            if "value" in config:
                value = config["value"]
            elif "column" in config and config["column"] in data_frame.columns:
                if config.get("aggregation") == "sum":
                    value = data_frame[config["column"]].sum()
                elif config.get("aggregation") == "mean":
                    value = data_frame[config["column"]].mean()
                elif config.get("aggregation") == "nunique":
                    value = data_frame[config["column"]].nunique()
                else:
                    value = len(data_frame)

                if config.get("format"):
                    value = config["format"].format(value)
            else:
                value = 0

            st.metric(config["label"], value)


def create_delete_section(
    record_type: str, delete_callback, endpoint: str, session_key: Optional[str] = None
):
    """
    Create a standardized delete section with expander

    Args:
        record_type (str): Type of record being deleted (e.g., "Order", "User")
        delete_callback: Function to call for deletion
        endpoint (str): API endpoint for deletion
        session_key (str, optional): Session state key to clear after deletion
    """
    with st.expander(f"🗑️ Delete {record_type}"):
        st.warning(
            f"⚠️ **Warning:** Deleting a {record_type.lower()} is permanent and cannot be undone!"
        )

        record_id = st.number_input(
            f"{record_type} ID to Delete",
            min_value=1,
            step=1,
            key=f"delete_{record_type.lower().replace(' ', '_')}",
        )

        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button(f"🗑️ Delete {record_type}", use_container_width=True):
                success = delete_callback(endpoint, record_id)
                if success:
                    st.success(f"✅ {record_type} {record_id} deleted successfully!")
                    if session_key and session_key in st.session_state:
                        del st.session_state[session_key]
                else:
                    st.error(f"❌ Failed to delete {record_type.lower()} {record_id}")

        with col2:
            st.info(
                f"ℹ️ Make sure you have the correct {record_type.lower()} ID before deleting."
            )


def show_dataframe_with_export(
    data_frame,
    filename_prefix: str,
    show_all_columns: bool = True,
    key_columns: Optional[list] = None,
):
    """
    Display dataframe with export functionality

    Args:
        data_frame: Pandas DataFrame to display
        filename_prefix (str): Prefix for downloaded file
        show_all_columns (bool): Whether to show all columns by default
        key_columns (list, optional): List of key columns to show if not showing all
    """
    from datetime import datetime

    # Column selection for large dataframes
    if len(data_frame.columns) > 10 and not show_all_columns:
        show_all = st.checkbox("Show all columns", value=False)
        if not show_all and key_columns:
            display_cols = [col for col in key_columns if col in data_frame.columns]
            df_display = data_frame[display_cols]
        else:
            df_display = data_frame
    else:
        df_display = data_frame

    st.dataframe(df_display, use_container_width=True, hide_index=True)

    # Export button
    csv = data_frame.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f"{filename_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        use_container_width=True,
    )


def refresh_button(
    label: str,
    fetch_callback,
    endpoint: str,
    session_key: str,
    use_container_width: bool = True,
) -> bool:
    """
    Create a refresh button that fetches data and stores in session

    Args:
        label (str): Button label
        fetch_callback: Function to fetch data
        endpoint (str): API endpoint to fetch from
        session_key (str): Session state key to store data
        use_container_width (bool): Whether button should use full width

    Returns:
        bool: True if refresh was clicked and successful
    """
    if st.button(label, use_container_width=use_container_width):
        success, data = fetch_callback(endpoint)
        if success:
            st.session_state[session_key] = data
            st.success(f"✅ Loaded {len(data)} records")
            return True
        else:
            st.error(f"❌ Failed to load data: {data.get('detail', 'Unknown error')}")
            return False
    return False
