import streamlit as st
import pandas as pd
from datetime import datetime
import sys
from pathlib import Path
import requests

from commons import MASTER_DATA_CONFIG

# Add parent directory to path to import commons
sys.path.insert(0, str(Path(__file__).parent.parent))

from commons import (
    fetch_data,
    create_record,
    update_record,
    check_authentication,
    display_user_info,
    API_BASE_URL,
    get_auth_headers,
)

# Page configuration
st.set_page_config(
    page_title="Master Data - Accuracy Packaging", page_icon="📏", layout="wide"
)


# Custom delete function for Master Data (uses param_name/param_value pattern)
def delete_record_by_param(endpoint, param_name, param_value):
    """Delete a record using parameter-based deletion"""
    try:
        response = requests.delete(
            f"{API_BASE_URL}{endpoint}",
            headers=get_auth_headers(),
            params={param_name: param_value},
        )
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.json()
    except Exception as e:
        return False, {"detail": str(e)}


# Main UI
st.title("📏 Master Data Management")

# Check authentication
check_authentication()
display_user_info()

st.markdown("---")

# Select master data type
selected_master = st.selectbox(
    "📂 Select Master Data Type", options=list(MASTER_DATA_CONFIG.keys())
)

if selected_master:
    config = MASTER_DATA_CONFIG[selected_master]

    st.markdown(f"### {selected_master}")

    # Tabs for view and manage
    tab1, tab2 = st.tabs(
        [
            "📋 View All",
            "➕ Add/Edit",
        ]
    )

    with tab1:
        st.subheader(f"All {selected_master}")

        if st.button("🔄 Refresh Data"):
            success, data = fetch_data(f"{config['endpoint']}/list_all")
            if success:
                st.session_state[f"{selected_master}_data"] = data
            else:
                st.error(
                    f"❌ Failed to load data: {data.get('detail', 'Unknown error')}"
                )

        if f"{selected_master}_data" in st.session_state:
            data = st.session_state[f"{selected_master}_data"]
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)

                # Delete section
                with st.expander("🗑️ Delete Record"):
                    if data:
                        record_options = [
                            f"{item.get(config['id_field'])} - {item.get(config['name_field'])}"
                            for item in data
                        ]
                        selected_record = st.selectbox(
                            "Select record to delete", options=record_options
                        )

                        if st.button("🗑️ Delete Selected", type="primary"):
                            record_id = int(selected_record.split(" - ")[0])
                            success, result = delete_record_by_param(
                                f"{config['endpoint']}/delete",
                                config["id_field"],
                                record_id,
                            )
                            if success:
                                st.success("✅ Record deleted successfully!")
                                st.rerun()
                            else:
                                st.error(
                                    f"❌ Delete failed: {result.get('detail', 'Unknown error')}"
                                )
            else:
                st.info("No records found")
        else:
            st.info("Click 'Refresh Data' to load records")

    with tab2:
        st.subheader(f"Add New {selected_master}")

        with st.form(f"add_{selected_master}_form"):
            form_data = {}

            for field in config["fields"]:
                if field["type"] == "text":
                    form_data[field["name"]] = st.text_input(
                        field["label"] + (" *" if field["required"] else "")
                    )
                elif field["type"] == "number":
                    form_data[field["name"]] = st.number_input(
                        field["label"] + (" *" if field["required"] else ""),
                        min_value=0.0,
                    )

            submitted = st.form_submit_button("➕ Add Record", use_container_width=True)

            if submitted:
                # Validate required fields
                valid = all(
                    form_data[field["name"]]
                    for field in config["fields"]
                    if field["required"]
                )

                if valid:
                    success, result = create_record(
                        f"{config['endpoint']}/create", form_data
                    )
                    if success:
                        st.success("✅ Record created successfully!")
                        # Clear cache
                        if f"{selected_master}_data" in st.session_state:
                            del st.session_state[f"{selected_master}_data"]
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )
                else:
                    st.warning("⚠️ Please fill in all required fields")

st.markdown("---")
st.info(
    "💡 **Tip:** Master data values are used throughout the system. Make sure to configure all necessary values before creating orders or jobs."
)
