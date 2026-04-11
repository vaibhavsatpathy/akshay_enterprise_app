import streamlit as st
import requests
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Accuracy Packaging Management System",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Session state initialization
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "token" not in st.session_state:
    st.session_state.token = None
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "user_role" not in st.session_state:
    st.session_state.user_role = None

# Custom CSS for better UI
st.markdown(
    """
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #555;
        text-align: center;
        margin-bottom: 3rem;
    }
    .feature-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .feature-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Main Home Page
def main():
    # Header
    st.markdown(
        '<h1 class="main-header">📦 Accuracy Packaging Management System</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="sub-header">Complete End-to-End Corrugation Box Manufacturing Solution</p>',
        unsafe_allow_html=True,
    )

    # Authentication status
    if st.session_state.authenticated:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.success(
                f"✅ Logged in as: **{st.session_state.user_name}** ({st.session_state.user_role})"
            )
        with col3:
            if st.button("🚪 Logout"):
                st.session_state.authenticated = False
                st.session_state.token = None
                st.session_state.user_name = None
                st.session_state.user_role = None
                st.rerun()
    else:
        st.warning("⚠️ Please login from the sidebar to access all features")

    st.markdown("---")

    # About Section
    st.header("🏭 About Accuracy Packaging")
    st.write(
        """
    **Accuracy Packaging** is a comprehensive manufacturing management system designed specifically for 
    corrugation box production facilities. Our system streamlines the entire manufacturing workflow from 
    raw material procurement to final product dispatch.
    """
    )

    # Key Features
    st.header("✨ Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class="feature-box">
            <div class="feature-title">📊 Inventory Management</div>
            <ul>
                <li>Real-time inventory tracking</li>
                <li>Raw material management</li>
                <li>Product reels, papers, flutes</li>
                <li>Spare parts & consumables</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="feature-box">
            <div class="feature-title">🎨 Printing Operations</div>
            <ul>
                <li>Block printing management</li>
                <li>Screen printing tracking</li>
                <li>Offset plate inventory</li>
                <li>Color job management</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="feature-box">
            <div class="feature-title">📋 Order Management</div>
            <ul>
                <li>Customer order tracking</li>
                <li>Party/vendor management</li>
                <li>Die specifications</li>
                <li>Box customization</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="feature-box">
            <div class="feature-title">⚙️ Job Processing</div>
            <ul>
                <li>Corrugation job tracking</li>
                <li>Paper cutting operations</li>
                <li>Stitching & pasting jobs</li>
                <li>Quality control</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="feature-box">
            <div class="feature-title">🚚 Dispatch Management</div>
            <ul>
                <li>Shipment tracking</li>
                <li>Transporter management</li>
                <li>Delivery scheduling</li>
                <li>Invoice generation</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="feature-box">
            <div class="feature-title">👥 User Management</div>
            <ul>
                <li>Role-based access control</li>
                <li>Employee management</li>
                <li>Activity logging</li>
                <li>Secure authentication</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # System Modules
    st.header("🔧 System Modules")

    modules = [
        (
            "📏 Master Data",
            "Manage dimensions, GSM, BF, product types, and other enumeration values",
        ),
        (
            "🏢 Lookup Tables",
            "Configure locations, shades, vendors, transporters, and parties",
        ),
        (
            "📦 Inventory",
            "Track all inventory items including reels, papers, flutes, and consumables",
        ),
        (
            "🖨️ Printing",
            "Manage printing operations including block, screen, and offset printing",
        ),
        ("📝 Orders & Die", "Handle customer orders and die specifications"),
        (
            "⚡ Job Processing",
            "Track all manufacturing jobs from corrugation to bundling",
        ),
        ("🚛 Dispatch", "Manage product dispatch and delivery"),
    ]

    for module, description in modules:
        with st.expander(f"**{module}**"):
            st.write(description)

    st.markdown("---")

    # Quick Stats (if authenticated)
    if st.session_state.authenticated:
        st.header("📈 Quick Statistics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Active Orders", "0", "0")
        with col2:
            st.metric("Pending Jobs", "0", "0")
        with col3:
            st.metric("Inventory Items", "0", "0")
        with col4:
            st.metric("Dispatches Today", "0", "0")

    # Footer
    st.markdown("---")
    st.markdown(
        """
    <div style="text-align: center; color: #666; padding: 2rem 0;">
        <p><strong>Accuracy Packaging Management System</strong> v0.1 Beta</p>
        <p>© 2025 All Rights Reserved</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
