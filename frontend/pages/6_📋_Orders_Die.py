import streamlit as st
import pandas as pd
from datetime import datetime
import json
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
    page_title="Orders & Die Management - Accuracy Packaging",
    page_icon="📋",
    layout="wide",
)

# Main UI
st.title("📋 Orders & Die Management")

check_authentication()
display_user_info()
st.markdown("---")

# Management tabs
management_tab1, management_tab2 = st.tabs(["📋 Orders", "🔧 Die Management"])

# ORDERS MANAGEMENT
with management_tab1:
    st.header("📋 Order Management")

    order_tab1, order_tab2, order_tab3 = st.tabs(
        ["📊 View Orders", "➕ Create Order", "🗑️ Delete Order"]
    )

    with order_tab1:
        st.subheader("All Orders")

        if st.button(
            "🔄 Refresh Orders", use_container_width=True, key="refresh_orders"
        ):
            success, data = fetch_data("/corrugation/orders-table/list_all")
            if success:
                st.session_state["orders_data"] = data
                st.success(f"✅ Loaded {len(data)} orders")
            else:
                st.error(
                    f"❌ Failed to load orders: {data.get('detail', 'Unknown error')}"
                )

        if "orders_data" in st.session_state:
            data = st.session_state["orders_data"]
            if data:
                df = pd.DataFrame(data)

                # Metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Orders", len(df))
                with col2:
                    if "order_quantity" in df.columns:
                        st.metric("Total Quantity", int(df["order_quantity"].sum()))
                with col3:
                    if "priority" in df.columns:
                        high_priority = len(df[df["priority"] == "High"])
                        st.metric("High Priority", high_priority)
                with col4:
                    if "order_date" in df.columns:
                        st.metric("Recent Orders (7d)", len(df))

                st.markdown("---")

                # Filter options
                col1, col2 = st.columns(2)
                with col1:
                    if "party_id" in df.columns:
                        party_filter = st.multiselect(
                            "Filter by Party ID", df["party_id"].unique()
                        )
                        if party_filter:
                            df = df[df["party_id"].isin(party_filter)]

                with col2:
                    if "product_type_id" in df.columns:
                        product_filter = st.multiselect(
                            "Filter by Product Type", df["product_type_id"].unique()
                        )
                        if product_filter:
                            df = df[df["product_type_id"].isin(product_filter)]

                st.dataframe(df, use_container_width=True, hide_index=True)

                # Export
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Orders CSV",
                    data=csv,
                    file_name=f"orders_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv",
                )
            else:
                st.info("No orders found")
        else:
            st.info("Click 'Refresh Orders' to load data")

    with order_tab2:
        st.subheader("Create New Order")

        with st.form("create_order_form"):
            st.markdown("### Basic Information")
            col1, col2 = st.columns(2)

            with col1:
                order_number = st.number_input("Order Number*", min_value=0, step=1)
                party_id = st.number_input("Party ID*", min_value=1, step=1)
                order_date = st.date_input("Order Date*", value=datetime.now())
                order_quantity = st.number_input("Order Quantity*", min_value=1, step=1)

            with col2:
                product_type_id = st.number_input(
                    "Product Type ID*", min_value=1, step=1
                )
                product_name_id = st.number_input(
                    "Product Name ID*", min_value=1, step=1
                )
                priority = st.selectbox("Priority", ["Low", "Medium", "High"])
                urgency = st.selectbox("Urgency", ["Normal", "Urgent", "Critical"])

            st.markdown("### Product Specifications")
            col1, col2, col3 = st.columns(3)

            with col1:
                size_length = st.number_input("Length (mm)", min_value=0.0, step=0.1)
                gsm_id = st.number_input("GSM ID", min_value=1, step=1)
                ply_id = st.number_input("Ply ID", min_value=1, step=1)

            with col2:
                size_width = st.number_input("Width (mm)", min_value=0.0, step=0.1)
                bf_id = st.number_input("BF ID", min_value=1, step=1)
                dimension_id = st.number_input("Dimension ID", min_value=1, step=1)

            with col3:
                size_height = st.number_input("Height (mm)", min_value=0.0, step=0.1)
                deck_id = st.number_input("Deck ID", min_value=1, step=1)
                flute_id = st.number_input("Flute ID", min_value=1, step=1)

            st.markdown("### Printing & Color")
            col1, col2 = st.columns(2)

            with col1:
                printing_type_id = st.number_input(
                    "Printing Type ID", min_value=0, step=1
                )
                top_paper_color_id = st.number_input(
                    "Top Paper Color ID", min_value=0, step=1
                )

            with col2:
                color_count = st.number_input(
                    "Number of Colors", min_value=0, max_value=4, step=1
                )
                colors = []
                if color_count > 0:
                    st.write("Enter Color IDs:")
                    color_cols = st.columns(4)
                    for i in range(4):
                        with color_cols[i]:
                            if i < color_count:
                                color_id = st.number_input(
                                    f"Color {i+1}",
                                    min_value=1,
                                    step=1,
                                    key=f"color_{i}",
                                )
                                colors.append(color_id)
                            else:
                                colors.append(None)

            st.markdown("### Additional Details")
            remarks = st.text_area("Remarks")
            sample_image_path = st.text_input("Sample Image Path (optional)")

            submitted = st.form_submit_button(
                "➕ Create Order", use_container_width=True
            )

            if submitted:
                data = {
                    "order_number": order_number,
                    "party_id": party_id,
                    "order_date": order_date.isoformat(),
                    "order_quantity": order_quantity,
                    "product_type_id": product_type_id,
                    "product_name_id": product_name_id,
                    "size_length": size_length if size_length > 0 else None,
                    "size_width": size_width if size_width > 0 else None,
                    "size_height": size_height if size_height > 0 else None,
                    "gsm_id": gsm_id,
                    "bf_id": bf_id,
                    "ply_id": ply_id,
                    "deck_id": deck_id,
                    "dimension_id": dimension_id,
                    "flute_id": flute_id,
                    "printing_type_id": (
                        printing_type_id if printing_type_id > 0 else None
                    ),
                    "color_1": colors[0] if len(colors) > 0 else None,
                    "color_2": colors[1] if len(colors) > 1 else None,
                    "color_3": colors[2] if len(colors) > 2 else None,
                    "color_4": colors[3] if len(colors) > 3 else None,
                    "top_paper_color_id": (
                        top_paper_color_id if top_paper_color_id > 0 else None
                    ),
                    "priority": priority,
                    "urgency": urgency,
                    "remarks": remarks if remarks else None,
                    "sample_image_path": (
                        sample_image_path if sample_image_path else None
                    ),
                }

                success, result = create_record(
                    "/corrugation/orders-table/create", data
                )
                if success:
                    st.success("✅ Order created successfully!")
                    if "orders_data" in st.session_state:
                        del st.session_state["orders_data"]
                else:
                    st.error(
                        f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                    )

    with order_tab3:
        st.subheader("Delete Order")

        with st.expander("🗑️ Delete Order"):
            order_id = st.number_input(
                "Order ID to Delete", min_value=1, step=1, key="delete_order"
            )

            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("🗑️ Delete Order", use_container_width=True):
                    success = delete_record(
                        "/corrugation/orders-table/delete", order_id
                    )
                    if success:
                        st.success(f"✅ Order {order_id} deleted successfully!")
                        if "orders_data" in st.session_state:
                            del st.session_state["orders_data"]
                    else:
                        st.error(f"❌ Failed to delete order {order_id}")

            with col2:
                st.warning("⚠️ This action cannot be undone!")

# DIE MANAGEMENT
with management_tab2:
    st.header("🔧 Die Management")

    die_tab1, die_tab2, die_tab3 = st.tabs(
        ["📊 View Dies", "➕ Create Die", "🗑️ Delete Die"]
    )

    with die_tab1:
        st.subheader("All Dies")

        if st.button("🔄 Refresh Dies", use_container_width=True, key="refresh_dies"):
            success, data = fetch_data("/corrugation/die/list_all")
            if success:
                st.session_state["dies_data"] = data
                st.success(f"✅ Loaded {len(data)} dies")
            else:
                st.error(
                    f"❌ Failed to load dies: {data.get('detail', 'Unknown error')}"
                )

        if "dies_data" in st.session_state:
            data = st.session_state["dies_data"]
            if data:
                df = pd.DataFrame(data)

                # Metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Dies", len(df))
                with col2:
                    if "die_type_id" in df.columns:
                        st.metric("Unique Types", df["die_type_id"].nunique())
                with col3:
                    if "party_id" in df.columns:
                        st.metric("Parties", df["party_id"].nunique())

                st.markdown("---")
                st.dataframe(df, use_container_width=True, hide_index=True)

                # Export
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Dies CSV",
                    data=csv,
                    file_name=f"dies_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv",
                )
            else:
                st.info("No dies found")
        else:
            st.info("Click 'Refresh Dies' to load data")

    with die_tab2:
        st.subheader("Create New Die")

        with st.form("create_die_form"):
            col1, col2 = st.columns(2)

            with col1:
                die_number = st.number_input("Die Number*", min_value=0, step=1)
                party_id = st.number_input("Party ID*", min_value=1, step=1)
                product_name_id = st.number_input(
                    "Product Name ID*", min_value=1, step=1
                )
                die_type_id = st.number_input("Die Type ID*", min_value=1, step=1)

            with col2:
                size_length = st.number_input("Length (mm)", min_value=0.0, step=0.1)
                size_width = st.number_input("Width (mm)", min_value=0.0, step=0.1)
                size_height = st.number_input("Height (mm)", min_value=0.0, step=0.1)
                ups = st.number_input("UPS (Units Per Sheet)", min_value=1, step=1)

            remarks = st.text_area("Remarks")

            submitted = st.form_submit_button("➕ Create Die", use_container_width=True)

            if submitted:
                data = {
                    "die_number": die_number,
                    "party_id": party_id,
                    "product_name_id": product_name_id,
                    "die_type_id": die_type_id,
                    "size_length": size_length if size_length > 0 else None,
                    "size_width": size_width if size_width > 0 else None,
                    "size_height": size_height if size_height > 0 else None,
                    "ups": ups,
                    "remarks": remarks if remarks else None,
                }

                success, result = create_record("/corrugation/die/create", data)
                if success:
                    st.success("✅ Die created successfully!")
                    if "dies_data" in st.session_state:
                        del st.session_state["dies_data"]
                else:
                    st.error(
                        f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                    )

    with die_tab3:
        st.subheader("Delete Die")

        with st.expander("🗑️ Delete Die"):
            die_id = st.number_input(
                "Die ID to Delete", min_value=1, step=1, key="delete_die"
            )

            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("🗑️ Delete Die", use_container_width=True):
                    success = delete_record("/corrugation/die/delete", die_id)
                    if success:
                        st.success(f"✅ Die {die_id} deleted successfully!")
                        if "dies_data" in st.session_state:
                            del st.session_state["dies_data"]
                    else:
                        st.error(f"❌ Failed to delete die {die_id}")

            with col2:
                st.warning("⚠️ This action cannot be undone!")

st.markdown("---")
st.info(
    "💡 **Tip:** Orders require configuration of parties, product types, and specifications in Master Data and Lookup Tables. Dies are linked to specific product types and parties."
)
