import streamlit as st
import pandas as pd
from datetime import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from commons import (
    inventory_types,
    LOOKUP_CONFIG,
    MASTER_DATA_CONFIG,
    fetch_data,
    create_record,
    delete_record,
    check_authentication,
    display_user_info,
)

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Inventory Management - Accuracy Packaging",
    page_icon="📦",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Load all lookup data needed across forms
# ---------------------------------------------------------------------------
product_in_db = fetch_data(LOOKUP_CONFIG["Products"]["endpoint"] + "/list_all")[1] or []
products_dict = {prod["product_name"]: prod["product_id"] for prod in product_in_db}
reverse_products_dict = {v: k for k, v in products_dict.items()}

inventory_in_db = (
    fetch_data(inventory_types["Main Inventory"]["endpoint"] + "/list_all")[1] or []
)
inventory_dict = {}
for inv in inventory_in_db:
    pid = inv.get("product_id")
    label = reverse_products_dict.get(pid, f"Inventory #{inv['inventory_id']}")
    inventory_dict[label] = inv["inventory_id"]

locations_in_db = (
    fetch_data(f"{LOOKUP_CONFIG['Locations']['endpoint']}/list_all")[1] or []
)
locations_dict = {loc["location_name"]: loc["location_id"] for loc in locations_in_db}

gst_configs_in_db = (
    fetch_data(f"{MASTER_DATA_CONFIG['GST Config']['endpoint']}/list_all")[1] or []
)
gst_configs_dict = {gst["gst_value"]: gst["gst_config_id"] for gst in gst_configs_in_db}
# Map gst_value (string like "18") → float for calculation
gst_rate_dict = {
    gst["gst_value"]: float(gst["gst_value"]) / 100.0 for gst in gst_configs_in_db
}

unit_types_in_db = (
    fetch_data(MASTER_DATA_CONFIG["Unit Types"]["endpoint"] + "/list_all")[1] or []
)
unit_types_dict = {ut["unit_type_value"]: ut["unit_type_id"] for ut in unit_types_in_db}

vendors_in_db = fetch_data(LOOKUP_CONFIG["Vendors"]["endpoint"] + "/list_all")[1] or []
vendors_dict = {vendor["vendor_name"]: vendor["vendor_id"] for vendor in vendors_in_db}

shades_in_db = fetch_data(LOOKUP_CONFIG["Shades"]["endpoint"] + "/list_all")[1] or []
shades_dict = {shade["shade_value"]: shade["shade_id"] for shade in shades_in_db}

gsms_in_db = fetch_data(MASTER_DATA_CONFIG["GSM"]["endpoint"] + "/list_all")[1] or []
gsms_dict = {gsm["gsm_value"]: gsm["gsm_id"] for gsm in gsms_in_db}

bfs_in_db = fetch_data(MASTER_DATA_CONFIG["BF"]["endpoint"] + "/list_all")[1] or []
bfs_dict = {bf["bf_value"]: bf["bf_id"] for bf in bfs_in_db}

dimensions_in_db = (
    fetch_data(MASTER_DATA_CONFIG["Dimensions"]["endpoint"] + "/list_all")[1] or []
)
dimensions_dict = {
    dim["dimension_value"]: dim["dimension_id"] for dim in dimensions_in_db
}

transporters_in_db = (
    fetch_data(LOOKUP_CONFIG["Transporters"]["endpoint"] + "/list_all")[1] or []
)
transporters_dict = {
    transp["transporter_name"]: transp["transporter_id"]
    for transp in transporters_in_db
}

layer_types_in_db = (
    fetch_data(MASTER_DATA_CONFIG["Layer Types"]["endpoint"] + "/list_all")[1] or []
)
layer_types_dict = {
    lt["layer_type_name"]: lt["layer_type_id"] for lt in layer_types_in_db
}

flute_types_in_db = (
    fetch_data(MASTER_DATA_CONFIG["Flute Types"]["endpoint"] + "/list_all")[1] or []
)
flute_types_dict = {
    ft["flute_type_name"]: ft["flute_type_id"] for ft in flute_types_in_db
}

gum_types_in_db = (
    fetch_data(MASTER_DATA_CONFIG["Gum Types"]["endpoint"] + "/list_all")[1] or []
)
gum_types_dict = {gt["gum_type_name"]: gt["gum_type_id"] for gt in gum_types_in_db}

pin_material_in_db = fetch_data("/corrugation/stitching-pin-material/list_all")[1] or []
pin_material_dict = {m["material_value"]: m["material_id"] for m in pin_material_in_db}

pin_types_in_db = fetch_data("/corrugation/stitching-pin-types/list_all")[1] or []
pin_types_dict = {pt["pin_type_value"]: pt["pin_type_id"] for pt in pin_types_in_db}

pin_make_in_db = fetch_data("/corrugation/stitching-pin-make/list_all")[1] or []
pin_make_dict = {mk["make_value"]: mk["make_id"] for mk in pin_make_in_db}


# ---------------------------------------------------------------------------
# Helper: cost computation
# ---------------------------------------------------------------------------
def compute_cost(number_of_units: float, rate_per_unit: float, gst_rate: float):
    total_base = number_of_units * rate_per_unit
    total_gst = total_base * gst_rate
    total = total_base + total_gst
    return total_base, total_gst, total


# ---------------------------------------------------------------------------
# Main UI
# ---------------------------------------------------------------------------
st.title("📦 Inventory Management")

check_authentication()
display_user_info()
st.markdown("---")

selected_type = st.selectbox(
    "📂 Select Inventory Type", options=list(inventory_types.keys())
)

if selected_type:
    config = inventory_types[selected_type]
    st.info(f"ℹ️ {config['description']}")

    tab1, tab2, tab3 = st.tabs(["📋 View Inventory", "➕ Add Entry", "🗑️ Delete"])

    # -----------------------------------------------------------------------
    # TAB 1 — VIEW
    # -----------------------------------------------------------------------
    with tab1:
        st.subheader(f"{selected_type} — All Records")
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
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Records", len(df))
                with col2:
                    for wt_col in (
                        "weight",
                        "total_weight_kg",
                        "total_weight_act",
                        "total_weight",
                    ):
                        if wt_col in df.columns:
                            st.metric("Total Weight (kg)", f"{df[wt_col].sum():.2f}")
                            break
                with col3:
                    for qty_col in (
                        "quantity",
                        "number_of_units",
                        "number_of_bundles",
                        "number_of_coils",
                    ):
                        if qty_col in df.columns:
                            st.metric("Total Qty", int(df[qty_col].sum()))
                            break
                st.markdown("---")
                st.dataframe(df, use_container_width=True, hide_index=True)
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

    # -----------------------------------------------------------------------
    # TAB 2 — ADD ENTRY
    # -----------------------------------------------------------------------
    with tab2:
        st.subheader(f"Add New {selected_type} Entry")

        # ── Main Inventory ──────────────────────────────────────────────────
        if selected_type == "Main Inventory":
            with st.form("inventory_form"):
                col1, col2 = st.columns(2)
                with col1:
                    invoice_number = st.number_input(
                        "Invoice Number", min_value=0, step=1
                    )
                    vendor_value = st.selectbox(
                        "Vendor", options=list(vendors_dict.keys()) or ["—"]
                    )
                    product_value = st.selectbox(
                        "Product", options=list(products_dict.keys()) or ["—"]
                    )
                    vehicle_number = st.text_input("Vehicle Number")
                    driver_name = st.text_input("Driver Name")
                    transporter_value = st.selectbox(
                        "Transporter", options=list(transporters_dict.keys()) or ["—"]
                    )
                    vehicle_type = st.text_input("Vehicle Type")
                with col2:
                    entry_date = st.date_input("Entry Date", value=datetime.now())
                    freight_charges = st.number_input(
                        "Freight Charges (₹)", min_value=0.0, step=0.01
                    )
                    total_weight_kg = st.number_input(
                        "Total Weight (kg)", min_value=0.0, step=0.01
                    )
                    basic_cost_per_unit = st.number_input(
                        "Basic Cost per kg (₹)", min_value=0.0, step=0.01
                    )

                submitted = st.form_submit_button(
                    "➕ Add Inventory Entry", use_container_width=True
                )
                if submitted:
                    per_kg_freight = (
                        freight_charges / total_weight_kg
                        if total_weight_kg > 0
                        else 0.0
                    )
                    per_kg_cost = basic_cost_per_unit + per_kg_freight
                    total_cost = per_kg_cost * total_weight_kg
                    data = {
                        "invoice_number": (
                            invoice_number if invoice_number > 0 else None
                        ),
                        "vendor_id": vendors_dict.get(vendor_value),
                        "product_id": products_dict.get(product_value),
                        "entry_date": entry_date.isoformat(),
                        "transporter_id": transporters_dict.get(transporter_value),
                        "vehicle_number": vehicle_number or None,
                        "vehicle_type": vehicle_type or None,
                        "driver_name": driver_name or None,
                        "freight_charges": freight_charges,
                        "basic_cost_of_material": basic_cost_per_unit,
                        "total_weight_kg": total_weight_kg,
                        "per_kg_freight_charges": per_kg_freight,
                        "per_kg_cost_of_material": per_kg_cost,
                        "total_cost_of_material": total_cost,
                    }
                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Inventory entry created successfully!")
                        st.session_state.pop(f"{selected_type}_data", None)
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        # ── Product Reels ────────────────────────────────────────────────────
        elif selected_type == "Product Reels":
            with st.form("reels_form"):
                col1, col2 = st.columns(2)
                with col1:
                    shade_value = st.selectbox(
                        "Shade", options=list(shades_dict.keys()) or ["—"]
                    )
                    gsm_value = st.selectbox(
                        "GSM", options=list(gsms_dict.keys()) or ["—"]
                    )
                    bf_value = st.selectbox(
                        "BF", options=list(bfs_dict.keys()) or ["—"]
                    )
                    dimension_value = st.selectbox(
                        "Dimension", options=list(dimensions_dict.keys()) or ["—"]
                    )
                with col2:
                    size = st.number_input("Size (mm)", min_value=0.0, step=0.1)
                    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.01)
                    location_value = st.selectbox(
                        "Location", options=list(locations_dict.keys()) or ["—"]
                    )
                    inventory_value = st.selectbox(
                        "Inventory Item", options=list(inventory_dict.keys()) or ["—"]
                    )

                submitted = st.form_submit_button(
                    "➕ Add Product Reel", use_container_width=True
                )
                if submitted:
                    data = {
                        "shade_id": shades_dict.get(shade_value),
                        "gsm_id": gsms_dict.get(gsm_value),
                        "bf_id": bfs_dict.get(bf_value),
                        "dimension_id": dimensions_dict.get(dimension_value),
                        "size": size if size > 0 else None,
                        "weight": weight if weight > 0 else None,
                        "location_id": locations_dict.get(location_value),
                        "inventory_id": inventory_dict.get(inventory_value),
                    }
                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Product reel created successfully!")
                        st.session_state.pop(f"{selected_type}_data", None)
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        # ── Paper Bundles ────────────────────────────────────────────────────
        elif selected_type == "Paper Bundles":
            with st.form("bundles_form"):
                col1, col2 = st.columns(2)
                with col1:
                    inventory_value = st.selectbox(
                        "Inventory Item", options=list(inventory_dict.keys()) or ["—"]
                    )
                    number_of_bundles = st.number_input(
                        "Number of Bundles", min_value=1, step=1
                    )
                with col2:
                    bundle_weight = st.number_input(
                        "Weight per Bundle (kg)", min_value=0.0, step=0.01
                    )
                    total_papers = st.number_input(
                        "Total Papers", min_value=0.0, step=1.0
                    )

                submitted = st.form_submit_button(
                    "➕ Add Paper Bundle", use_container_width=True
                )
                if submitted:
                    total_weight = number_of_bundles * bundle_weight
                    data = {
                        "inventory_id": inventory_dict.get(inventory_value),
                        "number_of_bundles": number_of_bundles,
                        "bundle_weight": bundle_weight if bundle_weight > 0 else None,
                        "total_weight": total_weight if total_weight > 0 else None,
                        "total_papers": total_papers if total_papers > 0 else None,
                    }
                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Paper bundle created successfully!")
                        st.session_state.pop(f"{selected_type}_data", None)
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        # ── Product Papers ───────────────────────────────────────────────────
        elif selected_type == "Product Papers":
            with st.form("papers_form"):
                col1, col2 = st.columns(2)
                with col1:
                    bundle_id = st.number_input(
                        "Bundle ID", min_value=1, step=1, help="ID from Paper Bundles"
                    )
                    gsm_value = st.selectbox(
                        "GSM", options=list(gsms_dict.keys()) or ["—"]
                    )
                    bf_value = st.selectbox(
                        "BF", options=list(bfs_dict.keys()) or ["—"]
                    )
                    reel_size = st.number_input(
                        "Reel Size (mm)", min_value=0.0, step=0.1
                    )
                    cutting_size = st.number_input(
                        "Cutting Size (mm)", min_value=0.0, step=0.1
                    )
                with col2:
                    weight_per_gross = st.number_input(
                        "Weight per Gross (kg)", min_value=0.0, step=0.01
                    )
                    number_of_gross = st.number_input(
                        "Number of Gross", min_value=1, step=1
                    )
                    number_of_paper_per_gross = st.number_input(
                        "Papers per Gross", min_value=1, step=1, value=144
                    )
                    location_value = st.selectbox(
                        "Location", options=list(locations_dict.keys()) or ["—"]
                    )
                    inventory_value = st.selectbox(
                        "Inventory Item", options=list(inventory_dict.keys()) or ["—"]
                    )

                submitted = st.form_submit_button(
                    "➕ Add Product Paper", use_container_width=True
                )
                if submitted:
                    data = {
                        "bundle_id": bundle_id,
                        "gsm_id": gsms_dict.get(gsm_value),
                        "bf_id": bfs_dict.get(bf_value),
                        "reel_size": reel_size if reel_size > 0 else None,
                        "cutting_size": cutting_size if cutting_size > 0 else None,
                        "weight_per_gross": (
                            weight_per_gross if weight_per_gross > 0 else None
                        ),
                        "number_of_gross": number_of_gross,
                        "number_of_paper_per_gross": number_of_paper_per_gross,
                        "location_id": locations_dict.get(location_value),
                        "inventory_id": inventory_dict.get(inventory_value),
                    }
                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Product paper created successfully!")
                        st.session_state.pop(f"{selected_type}_data", None)
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        # ── Product Flutes ───────────────────────────────────────────────────
        elif selected_type == "Product Flutes":
            with st.form("flutes_form"):
                col1, col2 = st.columns(2)
                with col1:
                    layer_type_value = st.selectbox(
                        "Layer Type", options=list(layer_types_dict.keys()) or ["—"]
                    )
                    flute_type_value = st.selectbox(
                        "Flute Type", options=list(flute_types_dict.keys()) or ["—"]
                    )
                    flute_percent = st.number_input(
                        "Flute Percent (%)", min_value=0.0, max_value=100.0, step=0.1
                    )
                    layer_gsm_value = st.selectbox(
                        "Layer GSM", options=list(gsms_dict.keys()) or ["—"]
                    )
                with col2:
                    layer_bf_value = st.selectbox(
                        "Layer BF", options=list(bfs_dict.keys()) or ["—"]
                    )
                    sheet_id = st.number_input(
                        "Ply Sheet ID",
                        min_value=1,
                        step=1,
                        help="ID from Ply Sheets — view Ply Sheets tab to look up",
                    )
                    inventory_value = st.selectbox(
                        "Inventory Item", options=list(inventory_dict.keys()) or ["—"]
                    )

                submitted = st.form_submit_button(
                    "➕ Add Product Flute", use_container_width=True
                )
                if submitted:
                    data = {
                        "layer_type_id": layer_types_dict.get(layer_type_value),
                        "flute_type_id": flute_types_dict.get(flute_type_value),
                        "flute_percent": flute_percent if flute_percent > 0 else None,
                        "layer_gsm_id": gsms_dict.get(layer_gsm_value),
                        "layer_bf_id": bfs_dict.get(layer_bf_value),
                        "sheet_id": sheet_id,
                        "inventory_id": inventory_dict.get(inventory_value),
                    }
                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Product flute created successfully!")
                        st.session_state.pop(f"{selected_type}_data", None)
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        # ── Ply Sheets ───────────────────────────────────────────────────────
        elif selected_type == "Ply Sheets":
            with st.form("ply_sheets_form"):
                col1, col2 = st.columns(2)
                with col1:
                    reel_size = st.number_input(
                        "Reel Size (mm)", min_value=0.0, step=0.1
                    )
                    cutting_size = st.number_input(
                        "Cutting Size (mm)", min_value=0.0, step=0.1
                    )
                    number_of_sheets = st.number_input(
                        "Number of Sheets", min_value=1, step=1
                    )
                    gsm_calc = st.number_input("GSM of Paper", min_value=0.0, step=0.1)
                    per_sheet_weight_act = st.number_input(
                        "Actual Weight per Sheet (kg)",
                        min_value=0.0,
                        step=0.001,
                        format="%.3f",
                    )
                with col2:
                    total_weight_act = st.number_input(
                        "Actual Total Weight (kg)", min_value=0.0, step=0.01
                    )
                    location_value = st.selectbox(
                        "Location", options=list(locations_dict.keys()) or ["—"]
                    )
                    inventory_value = st.selectbox(
                        "Inventory Item", options=list(inventory_dict.keys()) or ["—"]
                    )

                # Computed fields shown read-only
                sheet_size = reel_size * cutting_size
                per_sheet_weight_calc = (
                    (gsm_calc * sheet_size) / 1_000_000
                    if sheet_size > 0 and gsm_calc > 0
                    else 0.0
                )
                total_weight_calc = per_sheet_weight_calc * number_of_sheets
                variation = total_weight_act - total_weight_calc

                st.markdown("**Computed Values (preview)**")
                cc1, cc2, cc3, cc4 = st.columns(4)
                cc1.metric("Sheet Size (mm²)", f"{sheet_size:.1f}")
                cc2.metric("Calc Weight/Sheet (kg)", f"{per_sheet_weight_calc:.4f}")
                cc3.metric("Calc Total Weight (kg)", f"{total_weight_calc:.3f}")
                cc4.metric("Variation (kg)", f"{variation:.3f}")

                submitted = st.form_submit_button(
                    "➕ Add Ply Sheet", use_container_width=True
                )
                if submitted:
                    data = {
                        "reel_size": reel_size if reel_size > 0 else None,
                        "cutting_size": cutting_size if cutting_size > 0 else None,
                        "sheet_size": sheet_size if sheet_size > 0 else None,
                        "per_sheet_weight_calc": (
                            per_sheet_weight_calc if per_sheet_weight_calc > 0 else None
                        ),
                        "gsm_calc": gsm_calc if gsm_calc > 0 else None,
                        "per_sheet_weight_act": (
                            per_sheet_weight_act if per_sheet_weight_act > 0 else None
                        ),
                        "number_of_sheets": number_of_sheets,
                        "variation_in_weight": variation,
                        "total_weight_calc": (
                            total_weight_calc if total_weight_calc > 0 else None
                        ),
                        "total_weight_act": (
                            total_weight_act if total_weight_act > 0 else None
                        ),
                        "location_id": locations_dict.get(location_value),
                        "inventory_id": inventory_dict.get(inventory_value),
                    }
                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Ply sheet created successfully!")
                        st.session_state.pop(f"{selected_type}_data", None)
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        # ── Gum ──────────────────────────────────────────────────────────────
        elif selected_type == "Gum":
            with st.form("gum_form"):
                col1, col2 = st.columns(2)
                with col1:
                    gum_name = st.text_input("Gum Name")
                    gum_type_value = st.selectbox(
                        "Gum Type", options=list(gum_types_dict.keys()) or ["—"]
                    )
                    unit_type_value = st.selectbox(
                        "Unit Type", options=list(unit_types_dict.keys()) or ["—"]
                    )
                    number_of_units = st.number_input(
                        "Number of Units", min_value=1, step=1
                    )
                    rate_per_unit = st.number_input(
                        "Rate per Unit (₹)", min_value=0.0, step=0.01
                    )
                with col2:
                    weight_per_bag = st.number_input(
                        "Weight per Bag (kg)", min_value=0.0, step=0.01
                    )
                    total_weight_act = st.number_input(
                        "Actual Total Weight (kg)", min_value=0.0, step=0.01
                    )
                    ratio_prescribed = st.text_input(
                        "Ratio Prescribed", placeholder="e.g. 1:3"
                    )
                    gst_value = st.selectbox(
                        "GST %", options=list(gst_rate_dict.keys()) or ["0"]
                    )
                    location_value = st.selectbox(
                        "Location", options=list(locations_dict.keys()) or ["—"]
                    )
                    inventory_value = st.selectbox(
                        "Inventory Item", options=list(inventory_dict.keys()) or ["—"]
                    )

                total_weight_calc = number_of_units * weight_per_bag
                variation = total_weight_act - total_weight_calc
                gst_rate = gst_rate_dict.get(gst_value, 0.0)
                total_base, total_gst, total_cost = compute_cost(
                    number_of_units, rate_per_unit, gst_rate
                )

                st.markdown("**Computed Values (preview)**")
                cc1, cc2, cc3, cc4 = st.columns(4)
                cc1.metric("Calc Total Weight (kg)", f"{total_weight_calc:.2f}")
                cc2.metric("Variation (kg)", f"{variation:.2f}")
                cc3.metric("Base Cost (₹)", f"{total_base:.2f}")
                cc4.metric("Total Cost w/ GST (₹)", f"{total_cost:.2f}")

                submitted = st.form_submit_button(
                    "➕ Add Gum", use_container_width=True
                )
                if submitted:
                    if not gum_name:
                        st.error("❌ Gum name is required")
                    else:
                        data = {
                            "gum_name": gum_name,
                            "gum_type_id": gum_types_dict.get(gum_type_value),
                            "unit_type_id": unit_types_dict.get(unit_type_value),
                            "number_of_units": number_of_units,
                            "rate_per_unit": rate_per_unit,
                            "weight_per_bag": (
                                weight_per_bag if weight_per_bag > 0 else None
                            ),
                            "ratio_prescribed": ratio_prescribed or None,
                            "total_weight_calc": (
                                total_weight_calc if total_weight_calc > 0 else None
                            ),
                            "total_weight_act": (
                                total_weight_act if total_weight_act > 0 else None
                            ),
                            "variation_in_weight": variation,
                            "total_base_cost": total_base,
                            "total_gst_cost": total_gst,
                            "total_cost": total_cost,
                            "location_id": locations_dict.get(location_value),
                            "inventory_id": inventory_dict.get(inventory_value),
                        }
                        success, result = create_record(
                            f"{config['endpoint']}/create", data
                        )
                        if success:
                            st.success("✅ Gum entry created successfully!")
                            st.session_state.pop(f"{selected_type}_data", None)
                        else:
                            st.error(
                                f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                            )

        # ── Stitching Pins ───────────────────────────────────────────────────
        elif selected_type == "Stitching Pins":
            with st.form("stitching_pins_form"):
                col1, col2 = st.columns(2)
                with col1:
                    pin_material_value = st.selectbox(
                        "Pin Material", options=list(pin_material_dict.keys()) or ["—"]
                    )
                    pin_type_value = st.selectbox(
                        "Pin Type", options=list(pin_types_dict.keys()) or ["—"]
                    )
                    pin_make_value = st.selectbox(
                        "Pin Make", options=list(pin_make_dict.keys()) or ["—"]
                    )
                    rate_per_kg = st.number_input(
                        "Rate per kg (₹)", min_value=0.0, step=0.01
                    )
                    weight_per_coil = st.number_input(
                        "Weight per Coil (kg)", min_value=0.0, step=0.01
                    )
                    number_of_coils = st.number_input(
                        "Number of Coils", min_value=1, step=1
                    )
                with col2:
                    total_weight_act = st.number_input(
                        "Actual Total Weight (kg)", min_value=0.0, step=0.01
                    )
                    gst_value = st.selectbox(
                        "GST %", options=list(gst_rate_dict.keys()) or ["0"]
                    )
                    location_value = st.selectbox(
                        "Location", options=list(locations_dict.keys()) or ["—"]
                    )
                    inventory_value = st.selectbox(
                        "Inventory Item", options=list(inventory_dict.keys()) or ["—"]
                    )

                total_weight_calc = number_of_coils * weight_per_coil
                variation = total_weight_act - total_weight_calc
                gst_rate = gst_rate_dict.get(gst_value, 0.0)
                total_base, total_gst, total_cost = compute_cost(
                    total_weight_act, rate_per_kg, gst_rate
                )

                st.markdown("**Computed Values (preview)**")
                cc1, cc2, cc3, cc4 = st.columns(4)
                cc1.metric("Calc Total Weight (kg)", f"{total_weight_calc:.2f}")
                cc2.metric("Variation (kg)", f"{variation:.2f}")
                cc3.metric("Base Cost (₹)", f"{total_base:.2f}")
                cc4.metric("Total Cost w/ GST (₹)", f"{total_cost:.2f}")

                submitted = st.form_submit_button(
                    "➕ Add Stitching Pins", use_container_width=True
                )
                if submitted:
                    data = {
                        "pin_material_id": pin_material_dict.get(pin_material_value),
                        "pin_type_id": pin_types_dict.get(pin_type_value),
                        "pin_make_id": pin_make_dict.get(pin_make_value),
                        "rate_per_kg": rate_per_kg if rate_per_kg > 0 else None,
                        "weight_per_coil": (
                            weight_per_coil if weight_per_coil > 0 else None
                        ),
                        "number_of_coils": number_of_coils,
                        "total_weight_calc": (
                            total_weight_calc if total_weight_calc > 0 else None
                        ),
                        "total_weight_act": (
                            total_weight_act if total_weight_act > 0 else None
                        ),
                        "variation_in_weight": variation,
                        "total_base_cost": total_base,
                        "total_gst_cost": total_gst,
                        "total_cost": total_cost,
                        "location_id": locations_dict.get(location_value),
                        "inventory_id": inventory_dict.get(inventory_value),
                    }
                    success, result = create_record(
                        f"{config['endpoint']}/create", data
                    )
                    if success:
                        st.success("✅ Stitching pins entry created successfully!")
                        st.session_state.pop(f"{selected_type}_data", None)
                    else:
                        st.error(
                            f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                        )

        # ── Spare Parts ──────────────────────────────────────────────────────
        elif selected_type == "Spare Parts":
            with st.form("spare_parts_form"):
                col1, col2 = st.columns(2)
                with col1:
                    part_name = st.text_input("Part Name*")
                    unit_type_value = st.selectbox(
                        "Unit Type", options=list(unit_types_dict.keys()) or ["—"]
                    )
                    number_of_units = st.number_input(
                        "Number of Units", min_value=1, step=1
                    )
                    rate_per_unit = st.number_input(
                        "Rate per Unit (₹)", min_value=0.0, step=0.01
                    )
                with col2:
                    reference_machine = st.text_input("Reference Machine")
                    gst_value = st.selectbox(
                        "GST %", options=list(gst_rate_dict.keys()) or ["0"]
                    )
                    location_value = st.selectbox(
                        "Location", options=list(locations_dict.keys()) or ["—"]
                    )
                    inventory_value = st.selectbox(
                        "Inventory Item", options=list(inventory_dict.keys()) or ["—"]
                    )

                gst_rate = gst_rate_dict.get(gst_value, 0.0)
                total_base, total_gst, total_cost = compute_cost(
                    number_of_units, rate_per_unit, gst_rate
                )

                st.markdown("**Computed Values (preview)**")
                cc1, cc2, cc3 = st.columns(3)
                cc1.metric("Base Cost (₹)", f"{total_base:.2f}")
                cc2.metric("GST Cost (₹)", f"{total_gst:.2f}")
                cc3.metric("Total Cost (₹)", f"{total_cost:.2f}")

                submitted = st.form_submit_button(
                    "➕ Add Spare Part", use_container_width=True
                )
                if submitted:
                    if not part_name:
                        st.error("❌ Part name is required")
                    else:
                        data = {
                            "part_name": part_name,
                            "unit_type_id": unit_types_dict.get(unit_type_value),
                            "number_of_units": number_of_units,
                            "rate_per_unit": rate_per_unit,
                            "reference_machine": reference_machine or None,
                            "total_base_cost": total_base,
                            "total_gst_cost": total_gst,
                            "total_cost": total_cost,
                            "location_id": locations_dict.get(location_value),
                            "inventory_id": inventory_dict.get(inventory_value),
                        }
                        success, result = create_record(
                            f"{config['endpoint']}/create", data
                        )
                        if success:
                            st.success("✅ Spare part created successfully!")
                            st.session_state.pop(f"{selected_type}_data", None)
                        else:
                            st.error(
                                f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                            )

        # ── Miscellaneous ────────────────────────────────────────────────────
        elif selected_type == "Miscellaneous":
            with st.form("misc_form"):
                col1, col2 = st.columns(2)
                with col1:
                    misc_name = st.text_input("Item Name*")
                    unit_type_value = st.selectbox(
                        "Unit Type", options=list(unit_types_dict.keys()) or ["—"]
                    )
                    number_of_units = st.number_input(
                        "Number of Units", min_value=0.0, step=0.01
                    )
                    rate_per_unit = st.number_input(
                        "Rate per Unit (₹)", min_value=0.0, step=0.01
                    )
                with col2:
                    gst_value = st.selectbox(
                        "GST %", options=list(gst_rate_dict.keys()) or ["0"]
                    )
                    location_value = st.selectbox(
                        "Location", options=list(locations_dict.keys()) or ["—"]
                    )
                    inventory_value = st.selectbox(
                        "Inventory Item (optional)",
                        options=["— None —"] + list(inventory_dict.keys()),
                    )

                gst_rate = gst_rate_dict.get(gst_value, 0.0)
                total_base, total_gst, total_cost = compute_cost(
                    number_of_units, rate_per_unit, gst_rate
                )

                st.markdown("**Computed Values (preview)**")
                cc1, cc2, cc3 = st.columns(3)
                cc1.metric("Base Cost (₹)", f"{total_base:.2f}")
                cc2.metric("GST Cost (₹)", f"{total_gst:.2f}")
                cc3.metric("Total Cost (₹)", f"{total_cost:.2f}")

                submitted = st.form_submit_button(
                    "➕ Add Miscellaneous Item", use_container_width=True
                )
                if submitted:
                    if not misc_name:
                        st.error("❌ Item name is required")
                    else:
                        inv_id = (
                            inventory_dict.get(inventory_value)
                            if inventory_value != "— None —"
                            else None
                        )
                        data = {
                            "misc_name": misc_name,
                            "unit_type_id": unit_types_dict.get(unit_type_value),
                            "number_of_units": int(number_of_units),
                            "rate_per_unit": rate_per_unit,
                            "total_base_cost": total_base,
                            "total_gst_cost": total_gst,
                            "total_cost": total_cost,
                            "location_id": locations_dict.get(location_value),
                            "inventory_id": inv_id,
                        }
                        success, result = create_record(
                            f"{config['endpoint']}/create", data
                        )
                        if success:
                            st.success("✅ Miscellaneous item created successfully!")
                            st.session_state.pop(f"{selected_type}_data", None)
                        else:
                            st.error(
                                f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                            )

    # -----------------------------------------------------------------------
    # TAB 3 — DELETE
    # -----------------------------------------------------------------------
    with tab3:
        st.subheader(f"Delete {selected_type} Record")
        with st.expander("🗑️ Delete Record", expanded=True):
            record_id = st.number_input(
                f"{config['id_field']} to Delete",
                min_value=1,
                step=1,
                key=f"delete_{selected_type}",
            )
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button(
                    "🗑️ Delete", use_container_width=True, key=f"del_btn_{selected_type}"
                ):
                    success = delete_record(
                        f"{config['endpoint']}/delete",
                        record_id,
                        id_param=config["id_param"],
                    )
                    if success:
                        st.success(f"✅ Record {record_id} deleted successfully!")
                        st.session_state.pop(f"{selected_type}_data", None)
                    else:
                        st.error(f"❌ Failed to delete record {record_id}")
            with col2:
                st.warning("⚠️ This action cannot be undone!")

st.markdown("---")
st.info(
    "💡 **Tip:** Ensure vendors, products, and locations are configured in Lookup Tables before adding inventory entries. "
    "Main Inventory entries must exist before linking sub-items (Reels, Papers, Gum, etc.)."
)
