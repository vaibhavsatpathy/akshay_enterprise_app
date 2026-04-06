from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

# User Management
from sql.apis.routes.user_manageent.user_router import user_router

# Configuration
from sql.apis.routes.custom.app_router import app_config_router
from sql.apis.routes.custom.cloud_router import cloud_router

# Enum Tables
from sql.apis.routes.custom.dimensions_router import dimensions_router
from sql.apis.routes.custom.gsms_router import gsms_router
from sql.apis.routes.custom.bfs_router import bfs_router
from sql.apis.routes.custom.product_types_router import product_types_router
from sql.apis.routes.custom.flute_types_router import flute_types_router
from sql.apis.routes.custom.layer_types_router import layer_types_router
from sql.apis.routes.custom.gum_types_router import gum_types_router
from sql.apis.routes.custom.stitching_pin_material_router import (
    stitching_pin_material_router,
)
from sql.apis.routes.custom.stitching_pin_types_router import stitching_pin_types_router
from sql.apis.routes.custom.stitching_pin_make_router import stitching_pin_make_router
from sql.apis.routes.custom.unit_types_router import unit_types_router
from sql.apis.routes.custom.block_types_router import block_types_router
from sql.apis.routes.custom.color_job_types_router import color_job_types_router
from sql.apis.routes.custom.gst_config_router import gst_config_router
from sql.apis.routes.custom.file_types_router import file_types_router
from sql.apis.routes.custom.plate_types_router import plate_types_router
from sql.apis.routes.custom.plate_sizes_router import plate_sizes_router
from sql.apis.routes.custom.paper_types_router import paper_types_router
from sql.apis.routes.custom.rejected_item_types_router import rejected_item_types_router
from sql.apis.routes.custom.roll_types_router import roll_types_router
from sql.apis.routes.custom.box_types_router import box_types_router
from sql.apis.routes.custom.single_two_pieces_type_router import (
    single_two_pieces_type_router,
)
from sql.apis.routes.custom.print_plain_style_router import print_plain_style_router

# Lookup Tables
from sql.apis.routes.custom.locations_router import locations_router
from sql.apis.routes.custom.shades_router import shades_router
from sql.apis.routes.custom.vendors_router import vendors_router
from sql.apis.routes.custom.transporters_router import transporters_router
from sql.apis.routes.custom.products_router import products_router
from sql.apis.routes.custom.party_table_router import party_table_router

# Inventory Management
from sql.apis.routes.custom.inventory_router import inventory_router
from sql.apis.routes.custom.product_reels_router import product_reels_router
from sql.apis.routes.custom.product_paper_bundles_router import (
    product_paper_bundles_router,
)
from sql.apis.routes.custom.product_papers_router import product_papers_router
from sql.apis.routes.custom.product_flutes_router import product_flutes_router
from sql.apis.routes.custom.product_ply_sheets_router import product_ply_sheets_router
from sql.apis.routes.custom.product_gum_router import product_gum_router
from sql.apis.routes.custom.product_stitching_pin_router import (
    product_stitching_pin_router,
)
from sql.apis.routes.custom.product_spare_parts_router import product_spare_parts_router
from sql.apis.routes.custom.miscellaneous_router import miscellaneous_router

# Printing Operations
from sql.apis.routes.custom.block_print_colors_router import block_print_colors_router
from sql.apis.routes.custom.product_block_printing_router import (
    product_block_printing_router,
)
from sql.apis.routes.custom.screen_printing_router import screen_printing_router
from sql.apis.routes.custom.offset_plate_router import offset_plate_router
from sql.apis.routes.custom.printing_paper_offset_router import (
    printing_paper_offset_router,
)
from sql.apis.routes.custom.printing_paper_block_screen_router import (
    printing_paper_block_screen_router,
)

# Additional Inventory
from sql.apis.routes.custom.rejected_items_router import rejected_items_router
from sql.apis.routes.custom.strap_roll_router import strap_roll_router
from sql.apis.routes.custom.bundling_rope_router import bundling_rope_router
from sql.apis.routes.custom.color_table_router import color_table_router
from sql.apis.routes.custom.binding_cloth_router import binding_cloth_router
from sql.apis.routes.custom.file_placing_router import file_placing_router

# Orders & Die
from sql.apis.routes.custom.die_router import die_router
from sql.apis.routes.custom.orders_table_router import orders_table_router

# Job Processing
from sql.apis.routes.custom.corrugation_job_router import corrugation_job_router
from sql.apis.routes.custom.paper_cutting_job_router import paper_cutting_job_router
from sql.apis.routes.custom.printing_job_router import printing_job_router
from sql.apis.routes.custom.pasting_job_router import pasting_job_router
from sql.apis.routes.custom.rotory_job_router import rotory_job_router
from sql.apis.routes.custom.slot_job_router import slot_job_router
from sql.apis.routes.custom.die_punching_job_router import die_punching_job_router
from sql.apis.routes.custom.rs4_job_router import rs4_job_router
from sql.apis.routes.custom.chilai_job_router import chilai_job_router
from sql.apis.routes.custom.stitching_job_router import stitching_job_router
from sql.apis.routes.custom.side_pasting_job_router import side_pasting_job_router
from sql.apis.routes.custom.bundeling_job_router import bundeling_job_router

# Dispatch
from sql.apis.routes.custom.dispatch_table_router import dispatch_table_router

app = FastAPI(
    title="accuracy_packaging_server",
    version="0.1 - Beta",
    redoc_url="/documentation",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# User Management & Configuration
app.include_router(user_router, tags=["Authentication"])
app.include_router(app_config_router, tags=["App Config"])
app.include_router(cloud_router, tags=["Cloud"])

# Enum Tables
app.include_router(dimensions_router, tags=["Enums - Dimensions"])
app.include_router(gsms_router, tags=["Enums - GSM"])
app.include_router(bfs_router, tags=["Enums - BF"])
app.include_router(product_types_router, tags=["Enums - Product Types"])
app.include_router(flute_types_router, tags=["Enums - Flute Types"])
app.include_router(layer_types_router, tags=["Enums - Layer Types"])
app.include_router(gum_types_router, tags=["Enums - Gum Types"])
app.include_router(
    stitching_pin_material_router, tags=["Enums - Stitching Pin Material"]
)
app.include_router(stitching_pin_types_router, tags=["Enums - Stitching Pin Types"])
app.include_router(stitching_pin_make_router, tags=["Enums - Stitching Pin Make"])
app.include_router(unit_types_router, tags=["Enums - Unit Types"])
app.include_router(block_types_router, tags=["Enums - Block Types"])
app.include_router(color_job_types_router, tags=["Enums - Color Job Types"])
app.include_router(gst_config_router, tags=["Enums - GST Config"])
app.include_router(file_types_router, tags=["Enums - File Types"])
app.include_router(plate_types_router, tags=["Enums - Plate Types"])
app.include_router(plate_sizes_router, tags=["Enums - Plate Sizes"])
app.include_router(paper_types_router, tags=["Enums - Paper Types"])
app.include_router(rejected_item_types_router, tags=["Enums - Rejected Item Types"])
app.include_router(roll_types_router, tags=["Enums - Roll Types"])
app.include_router(box_types_router, tags=["Enums - Box Types"])
app.include_router(
    single_two_pieces_type_router, tags=["Enums - Single/Two Pieces Type"]
)
app.include_router(print_plain_style_router, tags=["Enums - Print/Plain Style"])

# Lookup Tables
app.include_router(locations_router, tags=["Lookup - Locations"])
app.include_router(shades_router, tags=["Lookup - Shades"])
app.include_router(vendors_router, tags=["Lookup - Vendors"])
app.include_router(transporters_router, tags=["Lookup - Transporters"])
app.include_router(products_router, tags=["Lookup - Products"])
app.include_router(party_table_router, tags=["Lookup - Parties"])

# Inventory Management
app.include_router(inventory_router, tags=["Inventory - Main"])
app.include_router(product_reels_router, tags=["Inventory - Product Reels"])
app.include_router(product_paper_bundles_router, tags=["Inventory - Paper Bundles"])
app.include_router(product_papers_router, tags=["Inventory - Papers"])
app.include_router(product_flutes_router, tags=["Inventory - Flutes"])
app.include_router(product_ply_sheets_router, tags=["Inventory - Ply Sheets"])
app.include_router(product_gum_router, tags=["Inventory - Gum"])
app.include_router(product_stitching_pin_router, tags=["Inventory - Stitching Pins"])
app.include_router(product_spare_parts_router, tags=["Inventory - Spare Parts"])
app.include_router(miscellaneous_router, tags=["Inventory - Miscellaneous"])

# Printing Operations
app.include_router(block_print_colors_router, tags=["Printing - Block Colors"])
app.include_router(product_block_printing_router, tags=["Printing - Block Printing"])
app.include_router(screen_printing_router, tags=["Printing - Screen Printing"])
app.include_router(offset_plate_router, tags=["Printing - Offset Plate"])
app.include_router(printing_paper_offset_router, tags=["Printing - Paper Offset"])
app.include_router(
    printing_paper_block_screen_router, tags=["Printing - Paper Block/Screen"]
)

# Additional Inventory
app.include_router(
    rejected_items_router, tags=["Additional Inventory - Rejected Items"]
)
app.include_router(strap_roll_router, tags=["Additional Inventory - Strap Roll"])
app.include_router(bundling_rope_router, tags=["Additional Inventory - Bundling Rope"])
app.include_router(color_table_router, tags=["Additional Inventory - Colors"])
app.include_router(binding_cloth_router, tags=["Additional Inventory - Binding Cloth"])
app.include_router(file_placing_router, tags=["Additional Inventory - File Placing"])

# Orders & Die
app.include_router(die_router, tags=["Orders - Die"])
app.include_router(orders_table_router, tags=["Orders - Main"])

# Job Processing
app.include_router(corrugation_job_router, tags=["Jobs - Corrugation"])
app.include_router(paper_cutting_job_router, tags=["Jobs - Paper Cutting"])
app.include_router(printing_job_router, tags=["Jobs - Printing"])
app.include_router(pasting_job_router, tags=["Jobs - Pasting"])
app.include_router(rotory_job_router, tags=["Jobs - Rotory"])
app.include_router(slot_job_router, tags=["Jobs - Slot"])
app.include_router(die_punching_job_router, tags=["Jobs - Die Punching"])
app.include_router(rs4_job_router, tags=["Jobs - RS4"])
app.include_router(chilai_job_router, tags=["Jobs - Chilai"])
app.include_router(stitching_job_router, tags=["Jobs - Stitching"])
app.include_router(side_pasting_job_router, tags=["Jobs - Side Pasting"])
app.include_router(bundeling_job_router, tags=["Jobs - Bundeling"])

# Dispatch
app.include_router(dispatch_table_router, tags=["Dispatch"])


@app.get("/")
def ping():
    """
    [ping func provides a health check]

    Returns:
        [dict]: [success response for the health check]
    """
    return {"response": "ping to jointpole inference server successful"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="accuracy_packaging_server",
        version="0.1 - Beta",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
