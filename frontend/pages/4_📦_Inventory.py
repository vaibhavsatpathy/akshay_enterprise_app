import streamlit as st
import pandas as pd
from datetime import datetime
import json
import sys
from pathlib import Path

from commons import inventory_types, LOOKUP_CONFIG, MASTER_DATA_CONFIG

# Add parent directory to path to import commons
sys.path.insert(0, str(Path(__file__).parent.parent))

from commons import fetch_data, create_record, check_authentication, display_user_info

product_in_db = fetch_data(LOOKUP_CONFIG["Products"]["endpoint"] + "/list_all")[1]
products_dict = {prod["product_name"]: prod["product_id"] for prod in product_in_db}
reverse_products_dict = {v: k for k, v in products_dict.items()}

inventory_in_db = fetch_data(
    inventory_types["Main Inventory"]["endpoint"] + "/list_all"
)[1]
inventory_dict = {
    reverse_products_dict[inv["product_id"]]: inv["inventory_id"]
    for inv in inventory_in_db
}

locations_in_db = fetch_data(f"{LOOKUP_CONFIG['Locations']['endpoint']}/list_all")[1]
locations_dict = {loc["location_name"]: loc["location_id"] for loc in locations_in_db}

gst_configs_in_db = fetch_data(
    f"{MASTER_DATA_CONFIG['GST Config']['endpoint']}/list_all"
)[1]
gst_configs_dict = {gst["gst_value"]: gst["gst_config_id"] for gst in gst_configs_in_db}

unit_types_in_db = fetch_data(
    MASTER_DATA_CONFIG["Unit Types"]["endpoint"] + "/list_all"
)[1]
unit_types_dict = {ut["unit_type_value"]: ut["unit_type_id"] for ut in unit_types_in_db}

vendors_in_db = fetch_data(LOOKUP_CONFIG["Vendors"]["endpoint"] + "/list_all")[1]
vendors_dict = {vendor["vendor_name"]: vendor["vendor_id"] for vendor in vendors_in_db}

shades_in_db = fetch_data(LOOKUP_CONFIG["Shades"]["endpoint"] + "/list_all")[1]
shades_dict = {shade["shade_value"]: shade["shade_id"] for shade in shades_in_db}

gsms_in_db = fetch_data(MASTER_DATA_CONFIG["GSM"]["endpoint"] + "/list_all")[1]
gsms_dict = {gsm["gsm_value"]: gsm["gsm_id"] for gsm in gsms_in_db}

bfs_in_db = fetch_data(MASTER_DATA_CONFIG["BF"]["endpoint"] + "/list_all")[1]
bfs_dict = {bf["bf_value"]: bf["bf_id"] for bf in bfs_in_db}

dimensions_in_db = fetch_data(
    MASTER_DATA_CONFIG["Dimensions"]["endpoint"] + "/list_all"
)[1]
dimensions_dict = {
    dim["dimension_value"]: dim["dimension_id"] for dim in dimensions_in_db
}

transporters_in_db = fetch_data(
    LOOKUP_CONFIG["Transporters"]["endpoint"] + "/list_all"
)[1]
transporters_dict = {
    transp["transporter_name"]: transp["transporter_id"]
    for transp in transporters_in_db
}

# Page configuration
st.set_page_config(
    page_title="Inventory Management - Accuracy Packaging",
    page_icon="📦",
    layout="wide",
)


def compute_cost(
    no_of_units: int,
    rate_per_unit: float,
    gst_value: float,
):
    total_amount = no_of_units * rate_per_unit
    total_gst_cost = total_amount * gst_value
    total_cost = total_amount + total_gst_cost
    return total_amount, total_gst_cost, total_cost


# Main UI
st.title("📦 Inventory Management")

check_authentication()
display_user_info()
st.markdown("---")

# Select inventory type
selected_type = st.selectbox(
    "📂 Select Inventory Type", options=list(inventory_types.keys())
)

if len(inventory_dict) == 0:
    st.warning("No inventory items found. Please add items to Main Inventory first.")

if selected_type:
    config = inventory_types[selected_type]

    st.info(f"ℹ️ {config['description']}")

    tab1, tab2 = st.tabs(
        [
            "📋 View Inventory",
            "➕ Add Entry",
        ]
    )

    with tab1:
        st.subheader(f"{selected_type} - All Records")

        col1, col2 = st.columns([3, 1])
        with col1:
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
                    if "weight" in df.columns:
                        st.metric("Total Weight (kg)", f"{df['weight'].sum():.2f}")
                    elif "total_weight_kg" in df.columns:
                        st.metric(
                            "Total Weight (kg)", f"{df['total_weight_kg'].sum():.2f}"
                        )
                with col3:
                    if "quantity" in df.columns:
                        st.metric("Total Quantity", int(df["quantity"].sum()))

                st.markdown("---")

                # Dataframe with filters
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
            st.info("Click 'Refresh Data' to load inventory records")

    with tab2:
        st.subheader(f"Add New {selected_type} Entry")

        # Different forms based on inventory type
        if selected_type == "Main Inventory":
            with st.form("inventory_form"):
                col1, col2 = st.columns(2)

                with col1:
                    invoice_number = st.text_input("Invoice Number")
                    vendor_value = st.selectbox(
                        "Vendor", options=list(vendors_dict.keys())
                    )
                    product_value = st.selectbox(
                        "Product", options=list(products_dict.keys())
                    )
                    vehicle_number = st.text_input("Vehicle Number")
                    driver_name = st.text_input("Driver Name")
                    transporter_value = st.selectbox(
                        "Transporter", options=list(transporters_dict.keys())
                    )
                    vehicle_type = st.text_input("Vehicle Type")

                with col2:
                    entry_date = st.date_input("Entry Date", value=datetime.now())
                    freight_charges = st.number_input(
                        "Freight Charges", min_value=0.0, step=0.01
                    )
                    total_weight_kg = st.number_input(
                        "Total Weight (kg)", min_value=0.0, step=0.01
                    )
                    basic_cost_per_unit = st.number_input(
                        "Basic Cost of Material", min_value=0.0, step=0.01
                    )

                submitted = st.form_submit_button(
                    "➕ Add Inventory Entry", use_container_width=True
                )

                if submitted:
                    per_kg_freight_charges = (
                        freight_charges / total_weight_kg
                        if total_weight_kg > 0
                        else 0.0
                    )
                    per_kg_cost_of_material = (
                        basic_cost_per_unit + per_kg_freight_charges
                        if total_weight_kg > 0
                        else 0.0
                    )
                    total_cost = per_kg_cost_of_material * total_weight_kg
                    data = {
                        "invoice_number": invoice_number,
                        "vendor_id": vendors_dict[vendor_value],
                        "product_id": products_dict[product_value],
                        "entry_date": entry_date.isoformat(),
                        "transporter_id": transporters_dict[transporter_value],
                        "vehicle_number": vehicle_number,
                        "vehicle_type": vehicle_type,
                        "driver_name": driver_name,
                        "freight_charges": freight_charges,
                        "basic_cost_of_material": basic_cost_per_unit,
                        "total_weight_kg": total_weight_kg,
                        "per_kg_freight_charges": per_kg_freight_charges,
                        "per_kg_cost_of_material": per_kg_cost_of_material,
                        "total_cost_of_material": total_cost,
                    }

                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Inventory entry created successfully!")
                        if f"{selected_type}_data" in st.session_state:
                            del st.session_state[f"{selected_type}_data"]
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        elif selected_type == "Product Reels":
            with st.expander("reels_form", expanded=True):
                col1, col2 = st.columns(2)

                with col1:
                    shade_value = st.selectbox(
                        "Shade", options=list(shades_dict.keys())
                    )
                    gsm_value = st.selectbox("GSM", options=list(gsms_dict.keys()))
                    bf_value = st.selectbox("BF", options=list(bfs_dict.keys()))
                    location_value = st.selectbox(
                        "Location", options=list(locations_dict.keys())
                    )
                    inventory_value = st.selectbox(
                        "Inventory Item", options=list(inventory_dict.keys())
                    )
                    inventory_id = inventory_dict[inventory_value]
                    product_type = st.selectbox(
                        "Product Type", options=list(products_dict.keys())
                    )

                with col2:
                    dimension_value = st.selectbox(
                        "Dimension", options=list(dimensions_dict.keys())
                    )
                    height_size = st.number_input(
                        "Height Size", min_value=0.0, step=0.01
                    )
                    radius_size = st.number_input(
                        "Radius Size", min_value=0.0, step=0.01
                    )
                    number_of_units = st.number_input(
                        "Number of Units", min_value=1, step=1
                    )

                load_data_entry_button = st.button("Load Data Entry")
                if load_data_entry_button:
                    weights = []
                    for i in range(int(number_of_units)):
                        weight = st.number_input(
                            f"Weight of Reel {i+1} (kg)",
                            min_value=0.0,
                            step=0.01,
                            key=f"reel_weight_{i}",
                        )
                        weights.append(weight)
                    st.write(weights)
                submitted = st.button("➕ Add Product Reel", use_container_width=True)

                if submitted:
                    data = {
                        "shade_id": shades_dict[shade_value],
                        "gsm_id": gsms_dict[gsm_value],
                        "bf_id": bfs_dict[bf_value],
                        "dimension_id": dimensions_dict[dimension_value],
                        "size": f"{height_size}x{radius_size}",
                        "weight": weight,
                        "location_id": locations_dict[location_value],
                        "inventory_id": inventory_id,
                    }

                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Product reel created successfully!")
                        if f"{selected_type}_data" in st.session_state:
                            del st.session_state[f"{selected_type}_data"]
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        elif selected_type == "Product Papers":
            with st.form("papers_form"):
                product_type = st.selectbox(
                    "Product Type", options=list(products_dict.keys())
                )
                shade_value = st.selectbox("Shade", options=list(shades_dict.keys()))
                gsm_value = st.selectbox("GSM", options=list(gsms_dict.keys()))
                bf_value = st.selectbox("BF", options=list(bfs_dict.keys()))
                dimension_value = st.selectbox(
                    "Dimension", options=list(dimensions_dict.keys())
                )
                reel_size = st.number_input("Reel Size", min_value=0.0, step=0.01)
                cutting_size = st.number_input("Cutting Size", min_value=0.0, step=0.01)
                weight = st.number_input("Weight (kg)", min_value=0.0, step=0.01)
                number_of_units = st.number_input(
                    "Number of Units", min_value=1, step=1
                )
                location_value = st.selectbox(
                    "Location", options=list(locations_dict.keys())
                )
                inventory_id = st.number_input("Inventory ID", min_value=1, step=1)

                submitted = st.form_submit_button(
                    "➕ Add Product Paper", use_container_width=True
                )

                if submitted:
                    data = {
                        "shade_id": shades_dict[shade_value],
                        "gsm_id": gsms_dict[gsm_value],
                        "bf_id": bfs_dict[bf_value],
                        "dimension_id": dimensions_dict[dimension_value],
                        "reel_size": reel_size,
                        "cutting_size": cutting_size,
                        "weight": weight,
                        "number_of_gross": number_of_units,
                        "location_id": locations_dict[location_value],
                        "inventory_id": inventory_id,
                    }

        elif selected_type == "Miscellaneous":
            fetch_locations = fetch_data(LOOKUP_CONFIG["Locations"]["endpoint"])

            with st.form("misc_form"):
                item_name = st.text_input("Item Name")
                unit_type_value = st.selectbox(
                    "Unit Type",
                    options=list(unit_types_dict.keys()),
                )
                number_of_units = st.number_input(
                    "Number of Units", min_value=0.0, step=0.01
                )
                rate_per_unit = st.number_input(
                    "Rate per Unit", min_value=0.0, step=0.01
                )
                gst_value = st.selectbox(
                    "GST Configuration",
                    options=list(gst_configs_dict.keys()),
                )
                location = st.selectbox(
                    "Location",
                    options=list(locations_dict.keys()),
                )
                total_base_cost, total_gst_cost, total_cost = compute_cost(
                    int(number_of_units),
                    float(rate_per_unit),
                    float(gst_value),
                )

                submitted = st.form_submit_button(
                    "➕ Add Miscellaneous Item", use_container_width=True
                )

                if submitted:
                    data = {
                        "misc_name": item_name,
                        "unit_type_id": unit_types_dict[unit_type_value],
                        "number_of_units": number_of_units,
                        "rate_per_unit": rate_per_unit,
                        "total_base_cost": total_base_cost,
                        "total_gst_cost": total_gst_cost,
                        "total_cost": total_cost,
                        "location_id": locations_dict[location],
                    }

                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Miscellaneous item created successfully!")
                        if f"{selected_type}_data" in st.session_state:
                            del st.session_state[f"{selected_type}_data"]
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        else:
            st.info(
                "📝 Please select a specific inventory type to see the add form, or use the API directly for complex entries."
            )
            st.code(
                f"""
# API Endpoint: {config['endpoint']}/create
# Method: POST
# Requires: JWT Token in Authorization header
            """
            )

st.markdown("---")
st.info(
    "💡 **Tip:** Ensure vendors, products, and locations are configured in Lookup Tables before adding inventory entries."
)
