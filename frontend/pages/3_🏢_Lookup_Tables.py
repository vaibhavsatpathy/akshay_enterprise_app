import streamlit as st
import pandas as pd
import sys
from pathlib import Path
import requests

from commons import LOOKUP_CONFIG

# Add parent directory to path to import commons
sys.path.insert(0, str(Path(__file__).parent.parent))

from commons import (
    fetch_data,
    create_record,
    check_authentication,
    display_user_info,
    API_BASE_URL,
    get_auth_headers,
)

# Page configuration
st.set_page_config(
    page_title="Lookup Tables - Accuracy Packaging", page_icon="🏢", layout="wide"
)


# Custom delete function for Lookup Tables (uses param_name/param_value pattern)
def delete_record_by_param(endpoint, param_name, param_value):
    """Delete a record using parameter-based deletion"""
    try:
        response = requests.delete(
            f"{API_BASE_URL}{endpoint}",
            headers=get_auth_headers(),
            params={param_name: param_value},
        )
        return (
            (True, response.json())
            if response.status_code == 200
            else (False, response.json())
        )
    except Exception as e:
        return False, {"detail": str(e)}


# Main UI
st.title("🏢 Lookup Tables Management")

check_authentication()
display_user_info()
st.markdown("---")

# Select lookup table
selected_lookup = st.selectbox(
    "📂 Select Lookup Table", options=list(LOOKUP_CONFIG.keys())
)

if selected_lookup:
    config = LOOKUP_CONFIG[selected_lookup]
    st.markdown(f"### {selected_lookup}")

    tab1, tab2 = st.tabs(
        [
            "📋 View All",
            "➕ Add New",
        ]
    )

    with tab1:
        st.subheader(f"All {selected_lookup}")

        if st.button("🔄 Refresh Data"):
            success, data = fetch_data(f"{config['endpoint']}/list_all")
            if success:
                st.session_state[f"{selected_lookup}_data"] = data
            else:
                st.error(
                    f"❌ Failed to load data: {data.get('detail', 'Unknown error')}"
                )

        if f"{selected_lookup}_data" in st.session_state:
            data = st.session_state[f"{selected_lookup}_data"]
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)

                # Delete section
                with st.expander("🗑️ Delete Record"):
                    record_options = [
                        f"{item.get(config['id_field'])} - {item.get(config['fields'][0]['name'])}"
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
        st.subheader(f"Add New {selected_lookup}")

        with st.form(f"add_{selected_lookup}_form"):
            form_data = {}

            for field in config["fields"]:
                if field["type"] == "text":
                    form_data[field["name"]] = st.text_input(
                        field["label"] + (" *" if field["required"] else "")
                    )
                elif field["type"] == "textarea":
                    form_data[field["name"]] = st.text_area(
                        field["label"] + (" *" if field["required"] else "")
                    )
                elif field["type"] == "dropdown":
                    # Fetch options for dropdown from Products table
                    if field["name"] == "product_type_id":
                        success, products = fetch_data(
                            "/corrugation/product-types/list_all"
                        )
                        if success:
                            options = {}
                            for product in products:
                                options[product["product_type_value"]] = product[
                                    "product_type_id"
                                ]
                        else:
                            options = {}
                            st.error(
                                f"❌ Failed to load products: {products.get('detail', 'Unknown error')}"
                            )
                    else:
                        options = {}

                    form_data[field["name"]] = st.selectbox(
                        field["label"] + (" *" if field["required"] else ""),
                        options=list(options.keys()),
                    )
                    form_data[field["name"]] = options[form_data[field["name"]]]

            submitted = st.form_submit_button("➕ Add Record", use_container_width=True)

            if submitted:
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
                        if f"{selected_lookup}_data" in st.session_state:
                            del st.session_state[f"{selected_lookup}_data"]
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )
                else:
                    st.warning("⚠️ Please fill in all required fields")

st.markdown("---")
st.info(
    "💡 **Note:** Configure vendors, transporters, and parties before creating inventory entries or orders."
)
