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
    page_title="Job Processing - Accuracy Packaging", page_icon="⚙️", layout="wide"
)

# Main UI
st.title("⚙️ Job Processing")

check_authentication()
display_user_info()
st.markdown("---")

# Job types configuration
job_types = {
    "Corrugation": {
        "endpoint": "/corrugation/corrugation-job",
        "icon": "📦",
        "description": "Corrugation process jobs",
    },
    "Paper Cutting": {
        "endpoint": "/corrugation/paper-cutting-job",
        "icon": "✂️",
        "description": "Paper cutting operations",
    },
    "Printing": {
        "endpoint": "/corrugation/printing-job",
        "icon": "🖨️",
        "description": "Printing job management",
    },
    "Pasting": {
        "endpoint": "/corrugation/pasting-job",
        "icon": "📎",
        "description": "Pasting operations",
    },
    "Rotary": {
        "endpoint": "/corrugation/rotory-job",
        "icon": "🔄",
        "description": "Rotary cutting jobs",
    },
    "Slot": {
        "endpoint": "/corrugation/slot-job",
        "icon": "📏",
        "description": "Slotting operations",
    },
    "Die Punching": {
        "endpoint": "/corrugation/die-punching-job",
        "icon": "🔨",
        "description": "Die punching jobs",
    },
    "RS4": {
        "endpoint": "/corrugation/rs4-job",
        "icon": "🏭",
        "description": "RS4 machine operations",
    },
    "Chilai": {
        "endpoint": "/corrugation/chilai-job",
        "icon": "📄",
        "description": "Chilai operations",
    },
    "Stitching": {
        "endpoint": "/corrugation/stitching-job",
        "icon": "🧵",
        "description": "Stitching operations",
    },
    "Side Pasting": {
        "endpoint": "/corrugation/side-pasting-job",
        "icon": "📐",
        "description": "Side pasting jobs",
    },
    "Bundling": {
        "endpoint": "/corrugation/bundeling-job",
        "icon": "📦",
        "description": "Bundling operations",
    },
}

# Sidebar for job type selection
with st.sidebar:
    st.header("Job Type Selection")
    selected_job = st.selectbox(
        "Select Job Type",
        options=list(job_types.keys()),
        format_func=lambda x: f"{job_types[x]['icon']} {x}",
    )

    st.markdown("---")
    st.info(job_types[selected_job]["description"])

    st.markdown("---")
    st.markdown("### Quick Stats")
    if st.button("📊 Refresh Stats", use_container_width=True):
        total_jobs = 0
        for job_name, config in job_types.items():
            success, data = fetch_data(f"{config['endpoint']}/list_all")
            if success:
                total_jobs += len(data)
        st.metric("Total Jobs (All Types)", total_jobs)

# Main content area
if selected_job:
    config = job_types[selected_job]

    st.header(f"{config['icon']} {selected_job} Jobs")

    tab1, tab2, tab3 = st.tabs(["📊 View Jobs", "➕ Create Job", "🗑️ Delete Job"])

    # VIEW JOBS TAB
    with tab1:
        st.subheader(f"All {selected_job} Jobs")

        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button(
                "🔄 Refresh Jobs",
                use_container_width=True,
                key=f"refresh_{selected_job}",
            ):
                success, data = fetch_data(f"{config['endpoint']}/list_all")
                if success:
                    st.session_state[f"{selected_job}_jobs"] = data
                    st.success(f"✅ Loaded {len(data)} jobs")
                else:
                    st.error(
                        f"❌ Failed to load jobs: {data.get('detail', 'Unknown error')}"
                    )

        if f"{selected_job}_jobs" in st.session_state:
            data = st.session_state[f"{selected_job}_jobs"]
            if data:
                df = pd.DataFrame(data)

                # Metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Jobs", len(df))
                with col2:
                    if "job_quantity" in df.columns:
                        st.metric("Total Quantity", int(df["job_quantity"].sum()))
                    elif "quantity" in df.columns:
                        st.metric("Total Quantity", int(df["quantity"].sum()))
                with col3:
                    if "order_id" in df.columns:
                        st.metric("Unique Orders", df["order_id"].nunique())
                with col4:
                    if "party_id" in df.columns:
                        st.metric("Parties", df["party_id"].nunique())

                st.markdown("---")

                # Filters
                if "job_date" in df.columns or "date" in df.columns:
                    date_col = "job_date" if "job_date" in df.columns else "date"
                    col1, col2 = st.columns(2)
                    with col1:
                        start_date = st.date_input(
                            "From Date", value=None, key=f"start_{selected_job}"
                        )
                    with col2:
                        end_date = st.date_input(
                            "To Date", value=None, key=f"end_{selected_job}"
                        )

                    if start_date and end_date:
                        df[date_col] = pd.to_datetime(df[date_col])
                        df = df[
                            (df[date_col] >= pd.to_datetime(start_date))
                            & (df[date_col] <= pd.to_datetime(end_date))
                        ]

                # Display dataframe
                st.dataframe(df, use_container_width=True, hide_index=True)

                # Export
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download CSV",
                    data=csv,
                    file_name=f"{selected_job}_jobs_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv",
                )
            else:
                st.info("No jobs found")
        else:
            st.info("Click 'Refresh Jobs' to load data")

    # CREATE JOB TAB
    with tab2:
        st.subheader(f"Create New {selected_job} Job")

        # Generic job creation form
        with st.form(f"create_{selected_job}_form"):
            st.markdown("### Basic Information")
            col1, col2 = st.columns(2)

            with col1:
                job_number = st.number_input(
                    "Job Number*", min_value=0, step=1, key=f"job_num_{selected_job}"
                )
                order_id = st.number_input(
                    "Order ID", min_value=0, step=1, key=f"order_{selected_job}"
                )
                party_id = st.number_input(
                    "Party ID", min_value=0, step=1, key=f"party_{selected_job}"
                )

            with col2:
                job_date = st.date_input(
                    "Job Date*", value=datetime.now(), key=f"date_{selected_job}"
                )
                job_quantity = st.number_input(
                    "Quantity*", min_value=1, step=1, key=f"qty_{selected_job}"
                )
                product_name_id = st.number_input(
                    "Product Name ID", min_value=0, step=1, key=f"prod_{selected_job}"
                )

            # Additional fields based on job type
            st.markdown("### Job-Specific Details")

            # Size fields (common for most jobs)
            col1, col2, col3 = st.columns(3)
            with col1:
                size_length = st.number_input(
                    "Length (mm)", min_value=0.0, step=0.1, key=f"len_{selected_job}"
                )
            with col2:
                size_width = st.number_input(
                    "Width (mm)", min_value=0.0, step=0.1, key=f"wid_{selected_job}"
                )
            with col3:
                size_height = st.number_input(
                    "Height (mm)", min_value=0.0, step=0.1, key=f"hgt_{selected_job}"
                )

            # Material specifications
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                gsm_id = st.number_input(
                    "GSM ID", min_value=0, step=1, key=f"gsm_{selected_job}"
                )
            with col2:
                bf_id = st.number_input(
                    "BF ID", min_value=0, step=1, key=f"bf_{selected_job}"
                )
            with col3:
                ply_id = st.number_input(
                    "Ply ID", min_value=0, step=1, key=f"ply_{selected_job}"
                )
            with col4:
                dimension_id = st.number_input(
                    "Dimension ID", min_value=0, step=1, key=f"dim_{selected_job}"
                )

            # Job-specific fields
            if selected_job == "Die Punching":
                die_id = st.number_input(
                    "Die ID", min_value=0, step=1, key=f"die_{selected_job}"
                )

            if selected_job in ["Printing", "Pasting"]:
                printing_type_id = st.number_input(
                    "Printing Type ID", min_value=0, step=1, key=f"print_{selected_job}"
                )

            if selected_job == "Stitching":
                stitching_type_id = st.number_input(
                    "Stitching Type ID",
                    min_value=0,
                    step=1,
                    key=f"stitch_{selected_job}",
                )

            # Common fields
            remarks = st.text_area("Remarks", key=f"remarks_{selected_job}")

            submitted = st.form_submit_button("➕ Create Job", use_container_width=True)

            if submitted:
                # Build data dict with common fields
                data = {
                    "job_number": job_number,
                    "job_date": job_date.isoformat(),
                    "job_quantity": job_quantity,
                }

                # Add optional fields
                if order_id > 0:
                    data["order_id"] = order_id
                if party_id > 0:
                    data["party_id"] = party_id
                if product_name_id > 0:
                    data["product_name_id"] = product_name_id
                if size_length > 0:
                    data["size_length"] = size_length
                if size_width > 0:
                    data["size_width"] = size_width
                if size_height > 0:
                    data["size_height"] = size_height
                if gsm_id > 0:
                    data["gsm_id"] = gsm_id
                if bf_id > 0:
                    data["bf_id"] = bf_id
                if ply_id > 0:
                    data["ply_id"] = ply_id
                if dimension_id > 0:
                    data["dimension_id"] = dimension_id
                if remarks:
                    data["remarks"] = remarks

                # Add job-specific fields
                if selected_job == "Die Punching" and die_id > 0:
                    data["die_id"] = die_id
                if selected_job in ["Printing", "Pasting"] and printing_type_id > 0:
                    data["printing_type_id"] = printing_type_id
                if selected_job == "Stitching" and stitching_type_id > 0:
                    data["stitching_type_id"] = stitching_type_id

                success, result = create_record(f"{config['endpoint']}/create", data)
                if success:
                    st.success(f"✅ {selected_job} job created successfully!")
                    if f"{selected_job}_jobs" in st.session_state:
                        del st.session_state[f"{selected_job}_jobs"]
                else:
                    st.error(
                        f"❌ Create failed: {result.get('detail', 'Unknown error')}"
                    )

    # DELETE JOB TAB
    with tab3:
        st.subheader(f"Delete {selected_job} Job")

        with st.expander("🗑️ Delete Job"):
            job_id = st.number_input(
                "Job ID to Delete", min_value=1, step=1, key=f"delete_{selected_job}"
            )

            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button(
                    "🗑️ Delete Job",
                    use_container_width=True,
                    key=f"delete_btn_{selected_job}",
                ):
                    success = delete_record(f"{config['endpoint']}/delete", job_id)
                    if success:
                        st.success(f"✅ Job {job_id} deleted successfully!")
                        if f"{selected_job}_jobs" in st.session_state:
                            del st.session_state[f"{selected_job}_jobs"]
                    else:
                        st.error(f"❌ Failed to delete job {job_id}")

            with col2:
                st.warning("⚠️ This action cannot be undone!")

st.markdown("---")

# Job workflow info
with st.expander("ℹ️ Job Processing Workflow"):
    st.markdown(
        """
    ### Typical Job Flow:
    1. **Corrugation** - Create corrugated sheets from paper reels
    2. **Paper Cutting** - Cut sheets to required sizes
    3. **Printing** - Apply graphics and text (if required)
    4. **Pasting** - Join multiple layers (if required)
    5. **Rotary/Slot/Die Punching** - Shape the product
    6. **Stitching** - Join edges with wire (if required)
    7. **Side Pasting** - Final assembly
    8. **Bundling** - Package for dispatch
    
    ### Notes:
    - Jobs are typically linked to orders via `order_id`
    - Each job type has specific requirements and parameters
    - Track job dates and quantities for production planning
    - Use remarks for special instructions or issues
    """
    )

st.info(
    "💡 **Tip:** Jobs should be created based on confirmed orders. Ensure all master data (GSM, BF, Ply, etc.) is configured before creating jobs."
)
