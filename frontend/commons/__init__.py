"""
Commons package for Streamlit frontend utilities
"""

from .api_helpers import (
    get_auth_headers,
    fetch_data,
    create_record,
    update_record,
    delete_record,
    login,
    register_user,
    change_password,
    API_BASE_URL,
)

from .ui_helpers import (
    check_authentication,
    display_user_info,
    display_metrics,
    create_delete_section,
    show_dataframe_with_export,
    refresh_button,
)

__all__ = [
    # API helpers
    "get_auth_headers",
    "fetch_data",
    "create_record",
    "update_record",
    "delete_record",
    "login",
    "register_user",
    "change_password",
    "API_BASE_URL",
    # UI helpers
    "check_authentication",
    "display_user_info",
    "display_metrics",
    "create_delete_section",
    "show_dataframe_with_export",
    "refresh_button",
]

# Lookup tables configuration
LOOKUP_CONFIG = {
    "Locations": {
        "endpoint": "/corrugation/locations",
        "id_field": "location_id",
        "fields": [
            {
                "name": "location_name",
                "label": "Location Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Shades": {
        "endpoint": "/corrugation/shades",
        "id_field": "shade_id",
        "fields": [
            {
                "name": "shade_value",
                "label": "Shade Value",
                "type": "text",
                "required": True,
            },
            {
                "name": "product_type_id",
                "label": "Product Type ID",
                "type": "dropdown",
                "required": True,
            },
        ],
    },
    "Vendors": {
        "endpoint": "/corrugation/vendors",
        "id_field": "vendor_id",
        "fields": [
            {
                "name": "vendor_name",
                "label": "Vendor Name",
                "type": "text",
                "required": True,
            },
            {
                "name": "address",
                "label": "Address",
                "type": "textarea",
                "required": True,
            },
            {
                "name": "contact",
                "label": "Contact",
                "type": "text",
                "required": True,
            },
        ],
    },
    "Transporters": {
        "endpoint": "/corrugation/transporters",
        "id_field": "transporter_id",
        "fields": [
            {
                "name": "transporter_name",
                "label": "Transporter Name",
                "type": "text",
                "required": True,
            },
            {
                "name": "contact",
                "label": "Contact",
                "type": "text",
                "required": True,
            },
        ],
    },
    "Products": {
        "endpoint": "/corrugation/products",
        "id_field": "product_id",
        "fields": [
            {
                "name": "product_name",
                "label": "Product Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Parties (Customers)": {
        "endpoint": "/corrugation/party-table",
        "id_field": "party_id",
        "fields": [
            {
                "name": "party_name",
                "label": "Party Name",
                "type": "text",
                "required": True,
            },
            {
                "name": "address",
                "label": "Address",
                "type": "textarea",
                "required": True,
            },
            {
                "name": "state",
                "label": "State Code",
                "type": "text",
                "required": True,
            },
            {
                "name": "contact",
                "label": "Contact",
                "type": "text",
                "required": True,
            },
            {
                "name": "gstin",
                "label": "GST Number",
                "type": "text",
                "required": True,
            },
        ],
    },
}

# Inventory types
inventory_types = {
    "Main Inventory": {
        "endpoint": "/corrugation/inventory",
        "description": "Manage main inventory entries with vendor and transporter details",
        "id_field": "inventory_id",
        "id_param": "inventory_id",
    },
    "Product Reels": {
        "endpoint": "/corrugation/product-reels",
        "description": "Track product reels with GSM, BF, and location",
        "id_field": "reel_id",
        "id_param": "reel_id",
    },
    "Paper Bundles": {
        "endpoint": "/corrugation/product-paper-bundles",
        "description": "Manage paper bundles inventory",
        "id_field": "bundle_id",
        "id_param": "bundle_id",
    },
    "Product Papers": {
        "endpoint": "/corrugation/product-papers",
        "description": "Track individual paper products",
        "id_field": "gross_id",
        "id_param": "gross_id",
    },
    "Product Flutes": {
        "endpoint": "/corrugation/product-flutes",
        "description": "Manage flute products",
        "id_field": "flute_id",
        "id_param": "flute_id",
    },
    "Ply Sheets": {
        "endpoint": "/corrugation/product-ply-sheets",
        "description": "Track ply sheet inventory",
        "id_field": "sheet_id",
        "id_param": "sheet_id",
    },
    "Gum": {
        "endpoint": "/corrugation/product-gum",
        "description": "Manage gum inventory",
        "id_field": "gum_id",
        "id_param": "gum_id",
    },
    "Stitching Pins": {
        "endpoint": "/corrugation/product-stitching-pin",
        "description": "Track stitching pin inventory",
        "id_field": "pin_id",
        "id_param": "pin_id",
    },
    "Spare Parts": {
        "endpoint": "/corrugation/product-spare-parts",
        "description": "Manage spare parts inventory",
        "id_field": "part_id",
        "id_param": "part_id",
    },
    "Miscellaneous": {
        "endpoint": "/corrugation/miscellaneous",
        "description": "Track miscellaneous items",
        "id_field": "misc_id",
        "id_param": "misc_id",
    },
}

# Master data configuration
MASTER_DATA_CONFIG = {
    "Dimensions": {
        "endpoint": "/corrugation/dimensions",
        "id_field": "dimension_id",
        "name_field": "dimension_value",
        "fields": [
            {
                "name": "dimension_value",
                "label": "Dimension Value",
                "type": "text",
                "required": True,
            }
        ],
    },
    "GSM": {
        "endpoint": "/corrugation/gsms",
        "id_field": "gsm_id",
        "name_field": "gsm_value",
        "fields": [
            {
                "name": "gsm_value",
                "label": "GSM Value",
                "type": "text",
                "required": True,
            }
        ],
    },
    "BF": {
        "endpoint": "/corrugation/bfs",
        "id_field": "bf_id",
        "name_field": "bf_value",
        "fields": [
            {"name": "bf_value", "label": "BF Value", "type": "text", "required": True}
        ],
    },
    "Product Types": {
        "endpoint": "/corrugation/product-types",
        "id_field": "product_type_id",
        "name_field": "product_type_value",
        "fields": [
            {
                "name": "product_type_value",
                "label": "Product Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Flute Types": {
        "endpoint": "/corrugation/flute-types",
        "id_field": "flute_type_id",
        "name_field": "flute_type_value",
        "fields": [
            {
                "name": "flute_type_value",
                "label": "Flute Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Layer Types": {
        "endpoint": "/corrugation/layer-types",
        "id_field": "layer_type_id",
        "name_field": "layer_type_value",
        "fields": [
            {
                "name": "layer_type_value",
                "label": "Layer Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Gum Types": {
        "endpoint": "/corrugation/gum-types",
        "id_field": "gum_type_id",
        "name_field": "gum_type_value",
        "fields": [
            {
                "name": "gum_type_value",
                "label": "Gum Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Unit Types": {
        "endpoint": "/corrugation/unit-types",
        "id_field": "unit_type_id",
        "name_field": "unit_type_name",
        "fields": [
            {
                "name": "unit_type_name",
                "label": "Unit Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Block Types": {
        "endpoint": "/corrugation/block-types",
        "id_field": "block_type_id",
        "name_field": "block_type_name",
        "fields": [
            {
                "name": "block_type_name",
                "label": "Block Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Color Job Types": {
        "endpoint": "/corrugation/color-job-types",
        "id_field": "color_job_type_id",
        "name_field": "color_job_type_name",
        "fields": [
            {
                "name": "color_job_type_name",
                "label": "Color Job Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "File Types": {
        "endpoint": "/corrugation/file-types",
        "id_field": "file_type_id",
        "name_field": "file_type_name",
        "fields": [
            {
                "name": "file_type_name",
                "label": "File Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Plate Types": {
        "endpoint": "/corrugation/plate-types",
        "id_field": "plate_type_id",
        "name_field": "plate_type_name",
        "fields": [
            {
                "name": "plate_type_name",
                "label": "Plate Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Plate Sizes": {
        "endpoint": "/corrugation/plate-sizes",
        "id_field": "plate_size_id",
        "name_field": "plate_size_value",
        "fields": [
            {
                "name": "plate_size_value",
                "label": "Plate Size Value",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Paper Types": {
        "endpoint": "/corrugation/paper-types",
        "id_field": "paper_type_id",
        "name_field": "paper_type_name",
        "fields": [
            {
                "name": "paper_type_name",
                "label": "Paper Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Box Types": {
        "endpoint": "/corrugation/box-types",
        "id_field": "box_type_id",
        "name_field": "box_type_name",
        "fields": [
            {
                "name": "box_type_name",
                "label": "Box Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Roll Types": {
        "endpoint": "/corrugation/roll-types",
        "id_field": "roll_type_id",
        "name_field": "roll_type_name",
        "fields": [
            {
                "name": "roll_type_name",
                "label": "Roll Type Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "Print/Plain Style": {
        "endpoint": "/corrugation/print-plain-style",
        "id_field": "print_plain_style_id",
        "name_field": "print_plain_style_name",
        "fields": [
            {
                "name": "print_plain_style_name",
                "label": "Print/Plain Style Name",
                "type": "text",
                "required": True,
            }
        ],
    },
    "GST Config": {
        "endpoint": "/corrugation/gst-config",
        "id_field": "gst_config_id",
        "name_field": "gst_value",
        "fields": [
            {
                "name": "gst_value",
                "label": "GST Percentage",
                "type": "number",
                "required": True,
            }
        ],
    },
}
