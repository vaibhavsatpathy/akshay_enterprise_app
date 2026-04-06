import streamlit as st
import pandas as pd
from datetime import datetime
import sys
from pathlib import Path

# Add parent directory to path to import commons
sys.path.insert(0, str(Path(__file__).parent.parent))

from commons import (
    fetch_data,
    create_record,
    delete_record,
    check_authentication,
    display_user_info,
)

# Page configuration
st.set_page_config(
    page_title="Printing Operations - Accuracy Packaging", page_icon="🖨️", layout="wide"
)

# Main UI
st.title("🖨️ Printing Operations")

check_authentication()
display_user_info()
st.markdown("---")

# Printing operation types
printing_types = {
    "Block Print Colors": {
        "endpoint": "/corrugation/block-print-colors",
        "description": "Manage color configurations for block printing",
        "fields": ["color_name", "description"],
    },
    "Block Printing Products": {
        "endpoint": "/corrugation/product-block-printing",
        "description": "Track block printing jobs and products",
    },
    "Screen Printing": {
        "endpoint": "/corrugation/screen-printing",
        "description": "Manage screen printing operations",
    },
    "Offset Plates": {
        "endpoint": "/corrugation/offset-plate",
        "description": "Track offset printing plates",
    },
    "Offset Printing Paper": {
        "endpoint": "/corrugation/printing-paper-offset",
        "description": "Manage offset printing paper inventory",
    },
    "Block/Screen Printing Paper": {
        "endpoint": "/corrugation/printing-paper-block-screen",
        "description": "Manage block and screen printing paper",
    },
}

# Select printing type
selected_type = st.selectbox(
    "🖨️ Select Printing Operation", options=list(printing_types.keys())
)

if selected_type:
    config = printing_types[selected_type]

    st.info(f"ℹ️ {config['description']}")

    tab1, tab2, tab3 = st.tabs(["📋 View Records", "➕ Add New", "🗑️ Delete"])

    with tab1:
        st.subheader(f"{selected_type} - All Records")

        if st.button("🔄 Refresh Data", use_container_width=True):
            success, data = fetch_data(f"{config['endpoint']}/list_all")
            if success:
                st.session_state[f"{selected_type}_data"] = data
                st.success(f"✅ Loaded {len(data)} records")
            else:
                st.error(
                    f"❌ Failed to load data: {data.get('detail', 'Unknown error')}"
                )

        if f"{selected_type}_data" in st.session_state:
            data = st.session_state[f"{selected_type}_data"]
            if data:
                df = pd.DataFrame(data)

                # Display metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Records", len(df))
                with col2:
                    if "quantity" in df.columns:
                        st.metric("Total Quantity", int(df["quantity"].sum()))
                with col3:
                    if "total_sheets" in df.columns:
                        st.metric("Total Sheets", int(df["total_sheets"].sum()))

                st.markdown("---")

                # Display dataframe
                st.dataframe(df, use_container_width=True, hide_index=True)

                # Export option
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download CSV",
                    data=csv,
                    file_name=f"{selected_type}_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv",
                )
            else:
                st.info("No records found")
        else:
            st.info("Click 'Refresh Data' to load records")

    with tab2:
        st.subheader(f"Add New {selected_type}")

        # Simple form for Block Print Colors
        if selected_type == "Block Print Colors":
            with st.form("color_form"):
                color_name = st.text_input(
                    "Color Name*", help="Enter the name of the color"
                )
                description = st.text_area(
                    "Description", help="Additional details about the color"
                )

                submitted = st.form_submit_button(
                    "➕ Add Color", use_container_width=True
                )

                if submitted:
                    if not color_name:
                        st.error("❌ Color name is required")
                    else:
                        data = {
                            "color_name": color_name,
                            "description": description if description else None,
                        }

                        success, result = create_record(
                            f"{config['endpoint']}/create", data
                        )
                        if success:
                            st.success("✅ Color created successfully!")
                            if f"{selected_type}_data" in st.session_state:
                                del st.session_state[f"{selected_type}_data"]
                        else:
                            st.error(
                                f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                            )

        # Block Printing Products
        elif selected_type == "Block Printing Products":
            with st.form("block_printing_form"):
                col1, col2 = st.columns(2)

                with col1:
                    job_number = st.number_input("Job Number", min_value=0, step=1)
                    party_id = st.number_input("Party ID", min_value=1, step=1)
                    product_name_id = st.number_input(
                        "Product Name ID", min_value=1, step=1
                    )
                    size_length = st.number_input(
                        "Size Length (mm)", min_value=0.0, step=0.1
                    )
                    size_width = st.number_input(
                        "Size Width (mm)", min_value=0.0, step=0.1
                    )
                    gsm_id = st.number_input("GSM ID", min_value=1, step=1)

                with col2:
                    bf_id = st.number_input("BF ID", min_value=1, step=1)
                    dimension_id = st.number_input("Dimension ID", min_value=1, step=1)
                    total_sheets = st.number_input("Total Sheets", min_value=0, step=1)
                    colors = st.text_input("Colors (comma-separated IDs)")
                    remarks = st.text_area("Remarks")

                submitted = st.form_submit_button(
                    "➕ Add Block Printing Product", use_container_width=True
                )

                if submitted:
                    # Parse color IDs
                    color_list = (
                        [int(c.strip()) for c in colors.split(",")] if colors else []
                    )

                    data = {
                        "job_number": job_number,
                        "party_id": party_id,
                        "product_name_id": product_name_id,
                        "size_length": size_length,
                        "size_width": size_width,
                        "gsm_id": gsm_id,
                        "bf_id": bf_id,
                        "dimension_id": dimension_id,
                        "total_sheets": total_sheets,
                        "color_1": color_list[0] if len(color_list) > 0 else None,
                        "color_2": color_list[1] if len(color_list) > 1 else None,
                        "color_3": color_list[2] if len(color_list) > 2 else None,
                        "color_4": color_list[3] if len(color_list) > 3 else None,
                        "remarks": remarks if remarks else None,
                    }

                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Block printing product created successfully!")
                        if f"{selected_type}_data" in st.session_state:
                            del st.session_state[f"{selected_type}_data"]
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        # Screen Printing
        elif selected_type == "Screen Printing":
            with st.form("screen_printing_form"):
                col1, col2 = st.columns(2)

                with col1:
                    job_number = st.number_input("Job Number", min_value=0, step=1)
                    party_id = st.number_input("Party ID", min_value=1, step=1)
                    product_name_id = st.number_input(
                        "Product Name ID", min_value=1, step=1
                    )
                    size_length = st.number_input(
                        "Size Length (mm)", min_value=0.0, step=0.1
                    )
                    size_width = st.number_input(
                        "Size Width (mm)", min_value=0.0, step=0.1
                    )

                with col2:
                    gsm_id = st.number_input("GSM ID", min_value=1, step=1)
                    bf_id = st.number_input("BF ID", min_value=1, step=1)
                    dimension_id = st.number_input("Dimension ID", min_value=1, step=1)
                    total_sheets = st.number_input("Total Sheets", min_value=0, step=1)
                    remarks = st.text_area("Remarks")

                submitted = st.form_submit_button(
                    "➕ Add Screen Printing", use_container_width=True
                )

                if submitted:
                    data = {
                        "job_number": job_number,
                        "party_id": party_id,
                        "product_name_id": product_name_id,
                        "size_length": size_length,
                        "size_width": size_width,
                        "gsm_id": gsm_id,
                        "bf_id": bf_id,
                        "dimension_id": dimension_id,
                        "total_sheets": total_sheets,
                        "remarks": remarks if remarks else None,
                    }

                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Screen printing created successfully!")
                        if f"{selected_type}_data" in st.session_state:
                            del st.session_state[f"{selected_type}_data"]
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        else:
            st.info(
                "📝 Use the API directly for complex printing entries or configure the form above."
            )
            st.code(
                f"""
# API Endpoint: {config['endpoint']}/create
# Method: POST
# Requires: JWT Token in Authorization header
            """
            )

    with tab3:
        st.subheader(f"Delete {selected_type}")

        with st.expander("🗑️ Delete Record"):
            record_id = st.number_input(
                "Record ID to Delete",
                min_value=1,
                step=1,
                key=f"delete_{selected_type}",
            )

            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("🗑️ Delete", use_container_width=True):
                    success = delete_record(f"{config['endpoint']}/delete", record_id)
                    if success:
                        st.success(f"✅ Record {record_id} deleted successfully!")
                        if f"{selected_type}_data" in st.session_state:
                            del st.session_state[f"{selected_type}_data"]
                    else:
                        st.error(f"❌ Failed to delete record {record_id}")

            with col2:
                st.warning("⚠️ This action cannot be undone!")

st.markdown("---")
st.info(
    "💡 **Tip:** Configure colors in Block Print Colors before creating block printing products. Ensure products and parties are set up in Lookup Tables."
)
