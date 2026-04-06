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
    page_title="Dispatch Management - Accuracy Packaging", page_icon="🚚", layout="wide"
)

# Main UI
st.title("🚚 Dispatch Management")

check_authentication()
display_user_info()
st.markdown("---")

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 View Dispatches", "➕ Create Dispatch", "🗑️ Delete Dispatch", "📈 Analytics"]
)

# VIEW DISPATCHES TAB
with tab1:
    st.subheader("All Dispatch Records")

    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("🔄 Refresh Dispatches", use_container_width=True):
            success, data = fetch_data("/corrugation/dispatch-table/list_all")
            if success:
                st.session_state["dispatch_data"] = data
                st.success(f"✅ Loaded {len(data)} dispatch records")
            else:
                st.error(
                    f"❌ Failed to load dispatches: {data.get('detail', 'Unknown error')}"
                )

    if "dispatch_data" in st.session_state:
        data = st.session_state["dispatch_data"]
        if data:
            df = pd.DataFrame(data)

            # Key Metrics
            st.markdown("### 📊 Key Metrics")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Dispatches", len(df))

            with col2:
                if "dispatch_quantity" in df.columns:
                    st.metric("Total Quantity", int(df["dispatch_quantity"].sum()))

            with col3:
                if "party_id" in df.columns:
                    st.metric("Unique Parties", df["party_id"].nunique())

            with col4:
                if "transporter_id" in df.columns:
                    st.metric("Transporters Used", df["transporter_id"].nunique())

            st.markdown("---")

            # Filters
            st.markdown("### 🔍 Filters")
            filter_col1, filter_col2, filter_col3 = st.columns(3)

            with filter_col1:
                if "dispatch_date" in df.columns:
                    df["dispatch_date"] = pd.to_datetime(df["dispatch_date"])
                    min_date = df["dispatch_date"].min().date()
                    max_date = df["dispatch_date"].max().date()

                    date_range = st.date_input(
                        "Dispatch Date Range",
                        value=(min_date, max_date),
                        min_value=min_date,
                        max_value=max_date,
                    )

                    if len(date_range) == 2:
                        df = df[
                            (df["dispatch_date"].dt.date >= date_range[0])
                            & (df["dispatch_date"].dt.date <= date_range[1])
                        ]

            with filter_col2:
                if "party_id" in df.columns:
                    party_filter = st.multiselect(
                        "Filter by Party ID",
                        options=sorted(df["party_id"].unique()),
                        default=None,
                    )
                    if party_filter:
                        df = df[df["party_id"].isin(party_filter)]

            with filter_col3:
                if "transporter_id" in df.columns:
                    transporter_filter = st.multiselect(
                        "Filter by Transporter ID",
                        options=sorted(df["transporter_id"].unique()),
                        default=None,
                    )
                    if transporter_filter:
                        df = df[df["transporter_id"].isin(transporter_filter)]

            st.markdown("---")

            # Display data
            st.markdown("### 📋 Dispatch Records")

            # Column selection
            if len(df.columns) > 10:
                show_all = st.checkbox("Show all columns", value=False)
                if not show_all:
                    key_columns = [
                        "id",
                        "dispatch_number",
                        "dispatch_date",
                        "party_id",
                        "order_id",
                        "dispatch_quantity",
                        "vehicle_number",
                        "transporter_id",
                        "freight_charges",
                    ]
                    display_cols = [col for col in key_columns if col in df.columns]
                    df_display = df[display_cols]
                else:
                    df_display = df
            else:
                df_display = df

            st.dataframe(df_display, use_container_width=True, hide_index=True)

            # Export options
            col1, col2 = st.columns(2)
            with col1:
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Filtered Data (CSV)",
                    data=csv,
                    file_name=f"dispatches_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    use_container_width=True,
                )

            with col2:
                excel_buffer = df.to_excel(index=False, engine="openpyxl")
                # Note: This requires openpyxl to be installed
                # st.download_button would need BytesIO buffer for Excel
        else:
            st.info("No dispatch records found")
    else:
        st.info("Click 'Refresh Dispatches' to load data")

# CREATE DISPATCH TAB
with tab2:
    st.subheader("Create New Dispatch")

    with st.form("create_dispatch_form"):
        st.markdown("### Basic Information")
        col1, col2, col3 = st.columns(3)

        with col1:
            dispatch_number = st.number_input("Dispatch Number*", min_value=0, step=1)
            party_id = st.number_input("Party ID*", min_value=1, step=1)
            order_id = st.number_input("Order ID*", min_value=1, step=1)

        with col2:
            dispatch_date = st.date_input("Dispatch Date*", value=datetime.now())
            dispatch_quantity = st.number_input(
                "Dispatch Quantity*", min_value=1, step=1
            )
            product_name_id = st.number_input("Product Name ID", min_value=0, step=1)

        with col3:
            transporter_id = st.number_input("Transporter ID*", min_value=1, step=1)
            freight_charges = st.number_input(
                "Freight Charges", min_value=0.0, step=0.01
            )
            lr_number = st.text_input("LR Number")

        st.markdown("### Vehicle Details")
        col1, col2, col3 = st.columns(3)

        with col1:
            vehicle_number = st.text_input("Vehicle Number*")
            vehicle_type = st.selectbox(
                "Vehicle Type", ["Truck", "Tempo", "Mini Truck", "Container", "Other"]
            )

        with col2:
            driver_name = st.text_input("Driver Name")
            driver_phone = st.text_input("Driver Phone")

        with col3:
            lr_date = st.date_input("LR Date", value=None)
            eway_bill_number = st.text_input("E-Way Bill Number")

        st.markdown("### Additional Details")
        col1, col2 = st.columns(2)

        with col1:
            invoice_number = st.text_input("Invoice Number")
            invoice_date = st.date_input("Invoice Date", value=None)

        with col2:
            destination = st.text_input("Destination")
            expected_delivery = st.date_input("Expected Delivery Date", value=None)

        remarks = st.text_area("Remarks", help="Any special instructions or notes")

        submitted = st.form_submit_button(
            "➕ Create Dispatch", use_container_width=True
        )

        if submitted:
            if (
                not dispatch_number
                or not party_id
                or not order_id
                or not vehicle_number
                or not transporter_id
            ):
                st.error("❌ Please fill in all required fields (marked with *)")
            else:
                data = {
                    "dispatch_number": dispatch_number,
                    "dispatch_date": dispatch_date.isoformat(),
                    "party_id": party_id,
                    "order_id": order_id,
                    "dispatch_quantity": dispatch_quantity,
                    "transporter_id": transporter_id,
                    "vehicle_number": vehicle_number,
                    "vehicle_type": vehicle_type if vehicle_type else None,
                    "driver_name": driver_name if driver_name else None,
                    "driver_phone": driver_phone if driver_phone else None,
                    "freight_charges": freight_charges if freight_charges > 0 else None,
                    "lr_number": lr_number if lr_number else None,
                    "lr_date": lr_date.isoformat() if lr_date else None,
                    "eway_bill_number": eway_bill_number if eway_bill_number else None,
                    "invoice_number": invoice_number if invoice_number else None,
                    "invoice_date": invoice_date.isoformat() if invoice_date else None,
                    "destination": destination if destination else None,
                    "expected_delivery_date": (
                        expected_delivery.isoformat() if expected_delivery else None
                    ),
                    "remarks": remarks if remarks else None,
                }

                if product_name_id > 0:
                    data["product_name_id"] = product_name_id

                success, result = create_record(
                    "/corrugation/dispatch-table/create", data
                )
                if success:
                    st.success("✅ Dispatch created successfully!")
                    st.balloons()
                    if "dispatch_data" in st.session_state:
                        del st.session_state["dispatch_data"]
                else:
                    st.error(
                        f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                    )

# DELETE DISPATCH TAB
with tab3:
    st.subheader("Delete Dispatch Record")

    with st.expander("🗑️ Delete Dispatch"):
        st.warning(
            "⚠️ **Warning:** Deleting a dispatch record is permanent and cannot be undone!"
        )

        dispatch_id = st.number_input(
            "Dispatch ID to Delete", min_value=1, step=1, key="delete_dispatch"
        )

        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("🗑️ Delete Dispatch", use_container_width=True):
                success = delete_record(
                    "/corrugation/dispatch-table/delete", dispatch_id
                )
                if success:
                    st.success(f"✅ Dispatch {dispatch_id} deleted successfully!")
                    if "dispatch_data" in st.session_state:
                        del st.session_state["dispatch_data"]
                else:
                    st.error(f"❌ Failed to delete dispatch {dispatch_id}")

        with col2:
            st.info("ℹ️ Make sure you have the correct dispatch ID before deleting.")

# ANALYTICS TAB
with tab4:
    st.subheader("📈 Dispatch Analytics")

    if "dispatch_data" in st.session_state and st.session_state["dispatch_data"]:
        df = pd.DataFrame(st.session_state["dispatch_data"])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Top Parties by Dispatch Count")
            if "party_id" in df.columns:
                party_counts = df["party_id"].value_counts().head(10)
                st.bar_chart(party_counts)

        with col2:
            st.markdown("#### Top Transporters by Usage")
            if "transporter_id" in df.columns:
                transporter_counts = df["transporter_id"].value_counts().head(10)
                st.bar_chart(transporter_counts)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Dispatches Over Time")
            if "dispatch_date" in df.columns:
                df["dispatch_date"] = pd.to_datetime(df["dispatch_date"])
                daily_dispatches = df.groupby(df["dispatch_date"].dt.date).size()
                st.line_chart(daily_dispatches)

        with col2:
            st.markdown("#### Quantity Distribution")
            if "dispatch_quantity" in df.columns:
                st.bar_chart(df["dispatch_quantity"].value_counts().head(20))

        st.markdown("---")

        # Freight analysis
        if "freight_charges" in df.columns:
            st.markdown("#### Freight Charges Analysis")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total Freight", f"₹{df['freight_charges'].sum():,.2f}")
            with col2:
                st.metric("Average Freight", f"₹{df['freight_charges'].mean():,.2f}")
            with col3:
                st.metric("Max Freight", f"₹{df['freight_charges'].max():,.2f}")
    else:
        st.info("Load dispatch data from the 'View Dispatches' tab to see analytics")

st.markdown("---")

# Footer with tips
st.info(
    """
💡 **Tips for Dispatch Management:**
- Ensure orders are created before creating dispatch entries
- Configure transporters and parties in Lookup Tables
- Always get LR number and E-Way bill before dispatching
- Track vehicle numbers for future reference
- Use remarks for special delivery instructions
- Monitor freight charges for cost control
"""
)
