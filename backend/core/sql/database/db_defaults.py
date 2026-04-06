from sql.crud.user_crud import CRUDUser
from sql.crud.user_roles_crud import CRUDUserRole
from sql.crud.app_config_crud import CRUDAppConfig
from sql.crud.cloud_crud import CRUDCloud
from sql.crud.dimensions_crud import CRUDDimension
from sql.crud.gsms_crud import CRUDGsm
from sql.crud.bfs_crud import CRUDBf
from sql.crud.product_types_crud import CRUDProductType
from sql.crud.products_crud import CRUDProduct
from sql.crud.flute_types_crud import CRUDFluteType
from sql.crud.layer_types_crud import CRUDLayerType
from sql.crud.gum_types_crud import CRUDGumType
from sql.crud.stitching_pin_material_crud import CRUDStitchingPinMaterial
from sql.crud.stitching_pin_types_crud import CRUDStitchingPinType
from sql.crud.stitching_pin_make_crud import CRUDStitchingPinMake
from sql.crud.unit_types_crud import CRUDUnitType
from sql.crud.block_types_crud import CRUDBlockType
from sql.crud.color_job_types_crud import CRUDColorJobType
from sql.crud.gst_config_crud import CRUDGstConfig
from sql.crud.file_types_crud import CRUDFileType
from sql.crud.plate_types_crud import CRUDPlateType
from sql.crud.plate_sizes_crud import CRUDPlateSize
from sql.crud.paper_types_crud import CRUDPaperType
from sql.crud.rejected_item_types_crud import CRUDRejectedItemType
from sql.crud.roll_types_crud import CRUDRollType
from sql.crud.box_types_crud import CRUDBoxType
from sql.crud.single_two_pieces_type_crud import CRUDSingleTwoPiecesType
from sql.crud.print_plain_style_crud import CRUDPrintPlainStyle
from sql.controllers.user_management.user_management_controller import (
    UserManagementController,
)
from sql.apis.schemas.requests.user_management.user_request import Register
from datetime import datetime
import os


def create_user_role(user_role_record: list):
    user_roles = CRUDUserRole().read_all()
    if len(user_roles) == 0:
        for item in user_role_record:
            CRUDUserRole().create(**item)
    else:
        pass


def create_admin_user(admin_user_request):
    existing_admin_user = CRUDUser().read(user_name="admin")
    if not existing_admin_user:
        _ = UserManagementController().register_user_controller(
            request=admin_user_request
        )
    else:
        pass


def create_app_config(app_config_request):
    existing_app_config = CRUDAppConfig().read_all()
    if len(existing_app_config) == 0:
        for item in app_config_request:
            CRUDAppConfig().create(**item)
    else:
        pass


def create_cloud_config(cloud_config_request):
    existing_cloud_config = CRUDCloud().read_all()
    if len(existing_cloud_config) == 0:
        for item in cloud_config_request:
            CRUDCloud().create(**item)
    else:
        pass


def create_dimensions(default_dimensions):
    existing_dimensions = CRUDDimension().read_all()
    if len(existing_dimensions) == 0:
        for item in default_dimensions:
            CRUDDimension().create(**item)
    else:
        pass


def create_bfs(default_bfs):
    existing_bfs = CRUDBf().read_all()
    if len(existing_bfs) == 0:
        for item in default_bfs:
            CRUDBf().create(**item)
    else:
        pass


def create_gsms(default_gsms):
    existing_gsms = CRUDGsm().read_all()
    if len(existing_gsms) == 0:
        for item in default_gsms:
            CRUDGsm().create(**item)
    else:
        pass


def create_products(default_products):
    existing_products = CRUDProduct().read_all()
    if len(existing_products) == 0:
        for item in default_products:
            item["product_name"] = item["product_type_value"]
            del item["product_type_value"]
            CRUDProduct().create(**item)
    else:
        pass


def create_product_types(default_product_types):
    existing_product_types = CRUDProductType().read_all()
    if len(existing_product_types) == 0:
        for item in default_product_types:
            CRUDProductType().create(**item)
    else:
        pass


def create_flute_types(default_flute_types):
    existing_flute_types = CRUDFluteType().read_all()
    if len(existing_flute_types) == 0:
        for item in default_flute_types:
            CRUDFluteType().create(**item)
    else:
        pass


def create_layer_types(default_layer_types):
    existing_layer_types = CRUDLayerType().read_all()
    if len(existing_layer_types) == 0:
        for item in default_layer_types:
            CRUDLayerType().create(**item)
    else:
        pass


def create_gum_types(default_gum_types):
    existing_gum_types = CRUDGumType().read_all()
    if len(existing_gum_types) == 0:
        for item in default_gum_types:
            CRUDGumType().create(**item)
    else:
        pass


def create_stitching_pin_material_types(default_stitching_pin_material_types):
    existing_material_types = CRUDStitchingPinMaterial().read_all()
    if len(existing_material_types) == 0:
        for item in default_stitching_pin_material_types:
            CRUDStitchingPinMaterial().create(**item)
    else:
        pass


def create_sticthing_pin_types(default_sticthing_pin_types):
    existing_pin_types = CRUDStitchingPinType().read_all()
    if len(existing_pin_types) == 0:
        for item in default_sticthing_pin_types:
            CRUDStitchingPinType().create(**item)
    else:
        pass


def create_sticthing_pin_make_types(default_sticthing_pin_make_types):
    existing_make_types = CRUDStitchingPinMake().read_all()
    if len(existing_make_types) == 0:
        for item in default_sticthing_pin_make_types:
            CRUDStitchingPinMake().create(**item)
    else:
        pass


def create_unit_types(default_unit_types):
    existing_unit_types = CRUDUnitType().read_all()
    if len(existing_unit_types) == 0:
        for item in default_unit_types:
            CRUDUnitType().create(**item)
    else:
        pass


def create_block_types(default_block_types):
    existing_block_types = CRUDBlockType().read_all()
    if len(existing_block_types) == 0:
        for item in default_block_types:
            CRUDBlockType().create(**item)
    else:
        pass


def create_color_job_types(default_color_job_types):
    existing_color_job_types = CRUDColorJobType().read_all()
    if len(existing_color_job_types) == 0:
        for item in default_color_job_types:
            CRUDColorJobType().create(**item)
    else:
        pass


def create_gst_configs(default_gst_configs):
    existing_gst_configs = CRUDGstConfig().read_all()
    if len(existing_gst_configs) == 0:
        for item in default_gst_configs:
            CRUDGstConfig().create(**item)
    else:
        pass


def create_file_types(default_file_types):
    existing_file_types = CRUDFileType().read_all()
    if len(existing_file_types) == 0:
        for item in default_file_types:
            CRUDFileType().create(**item)
    else:
        pass


def create_plate_types(default_plate_types):
    existing_plate_types = CRUDPlateType().read_all()
    if len(existing_plate_types) == 0:
        for item in default_plate_types:
            CRUDPlateType().create(**item)
    else:
        pass


def create_plate_sizes(default_plate_sizes):
    existing_plate_sizes = CRUDPlateSize().read_all()
    if len(existing_plate_sizes) == 0:
        for item in default_plate_sizes:
            CRUDPlateSize().create(**item)
    else:
        pass


def create_paper_types(default_paper_types):
    existing_paper_types = CRUDPaperType().read_all()
    if len(existing_paper_types) == 0:
        for item in default_paper_types:
            CRUDPaperType().create(**item)
    else:
        pass


def create_rejected_item_types(default_rejected_item_types):
    existing_rejected_item_types = CRUDRejectedItemType().read_all()
    if len(existing_rejected_item_types) == 0:
        for item in default_rejected_item_types:
            CRUDRejectedItemType().create(**item)
    else:
        pass


def create_roll_types(default_roll_types):
    existing_roll_types = CRUDRollType().read_all()
    if len(existing_roll_types) == 0:
        for item in default_roll_types:
            CRUDRollType().create(**item)
    else:
        pass


def create_box_types(default_box_types):
    existing_box_types = CRUDBoxType().read_all()
    if len(existing_box_types) == 0:
        for item in default_box_types:
            CRUDBoxType().create(**item)
    else:
        pass


def create_piece_types(default_piece_types):
    existing_piece_types = CRUDSingleTwoPiecesType().read_all()
    if len(existing_piece_types) == 0:
        for item in default_piece_types:
            CRUDSingleTwoPiecesType().create(**item)
    else:
        pass


def create_print_plain_styles(default_print_plain_styles):
    existing_print_plain_styles = CRUDPrintPlainStyle().read_all()
    if len(existing_print_plain_styles) == 0:
        for item in default_print_plain_styles:
            CRUDPrintPlainStyle().create(**item)
    else:
        pass


def main():
    user_role_record = [
        {
            "role_name": "admin",
            "role_id": 1,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "role_name": "editor",
            "role_id": 2,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "role_name": "viewer",
            "role_id": 3,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_user_role(user_role_record)

    admin_user_request = Register(
        user_name="admin",
        password=os.environ.get("password", "P@ssw0rd"),
        full_name="Admin User",
        email_id="admin@accuracy_packaging.com",
        role_name="admin",
        role_id=1,
    )
    create_admin_user(admin_user_request)

    default_app_config = [
        {
            "config_parameter": "sample_key",
            "config_value": "sample_value",
        }
    ]
    create_app_config(app_config_request=default_app_config)

    default_cloud_config = [
        {"cloud_id": 0, "cloud_name": "GCP"},
        {"cloud_id": 1, "cloud_name": "Azure"},
        {"cloud_id": 2, "cloud_name": "AWS"},
    ]
    create_cloud_config(cloud_config_request=default_cloud_config)

    default_dimensions = [
        {
            "dimension_value": "inch",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "dimension_value": "mm",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "dimension_value": "cm",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_dimensions(default_dimensions)

    default_gsms = [
        {"gsm_value": "80", "created_at": datetime.now(), "updated_at": datetime.now()},
        {
            "gsm_value": "100",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "gsm_value": "120",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_gsms(default_gsms)

    default_bfs = [
        {"bf_value": "80", "created_at": datetime.now(), "updated_at": datetime.now()},
        {"bf_value": "100", "created_at": datetime.now(), "updated_at": datetime.now()},
    ]
    create_bfs(default_bfs)

    default_product_types = [
        {
            "product_type_value": "kraft_reel",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "duplex_reel",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "imported_reel",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "duplex_paper",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "imported_paper",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "kraft_paper",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "two_ply_sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "three_ply_sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "five_ply_sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "seven_ply_sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "gum",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "stitching_pin",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "spare_parts",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "block_print",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "screen_print",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "file_place",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "offset_plate",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "misc",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "printed_paper_offset",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "printed_paper_screen_print",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "printed_paper_block_print",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "rejected_box",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "rejected_sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "product_type_value": "rejected_paper",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_product_types(default_product_types)
    create_products(default_products=default_product_types)

    default_flute_types = [
        {
            "flute_type_value": "A",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "flute_type_value": "B",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "flute_type_value": "C",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "flute_type_value": "D",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "flute_type_value": "E",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "flute_type_value": "F",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_flute_types(default_flute_types)

    default_layer_types = [
        {
            "layer_type_value": "top",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "layer_type_value": "flute",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "layer_type_value": "plain",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "layer_type_value": "flute_1",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "layer_type_value": "plain_1",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "layer_type_value": "flute_2",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "layer_type_value": "plain_2",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "layer_type_value": "flute_3",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "layer_type_value": "plain_3",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_layer_types(default_layer_types)

    default_gum_types = [
        {
            "gum_type_value": "pasting_gum",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "gum_type_value": "corrugation_gum",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "gum_type_value": "side_pasting_gum",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_gum_types(default_gum_types)

    default_stitching_pin_material_types = [
        {
            "material_value": "steel",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "material_value": "copper",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "material_value": "brass",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "material_value": "rustproof",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "material_value": "silver",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_stitching_pin_material_types(default_stitching_pin_material_types)

    default_sticthing_pin_types = [
        {
            "pin_type_value": "17x25",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "pin_type_value": "13x25",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "pin_type_value": "12x25",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "pin_type_value": "14x25",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_sticthing_pin_types(default_sticthing_pin_types)

    default_sticthing_pin_make_types = [
        {
            "make_value": "drum_type",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "make_value": "coil_type",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_sticthing_pin_make_types(default_sticthing_pin_make_types)

    default_unit_types = [
        {
            "unit_type_value": "kg",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "grams",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "liters",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "milliliters",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "pieces",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "pouch",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "drum",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "single_numbers",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "set_numbers",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "bundle",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "unit_type_value": "roll",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_unit_types(default_unit_types)

    default_block_types = [
        {
            "block_type_value": "3mm",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "block_type_value": "5mm",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_block_types(default_block_types)

    default_color_job_types = [
        {
            "color_job_type_value": "1_color",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "color_job_type_value": "2_color",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "color_job_type_value": "3_color",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "color_job_type_value": "4_color",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_color_job_types(default_color_job_types)

    default_gst_configs = [
        {"gst_value": 0.0, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"gst_value": 5.0, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"gst_value": 12.0, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"gst_value": 18.0, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"gst_value": 28.0, "created_at": datetime.now(), "updated_at": datetime.now()},
    ]
    create_gst_configs(default_gst_configs)

    default_file_types = [
        {
            "file_type_value": "sale_file",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "file_type_value": "voucher_file",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "file_type_value": "purchase_file",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "file_type_value": "bank_statement_file",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "file_type_value": "others",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_file_types(default_file_types)

    default_plate_types = [
        {
            "plate_type_value": "normal",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "plate_type_value": "thermal",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_plate_types(default_plate_types)

    default_plate_sizes = [
        {
            "plate_size_value": "20x30",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "plate_size_value": "24x36",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "plate_size_value": "30x40",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_plate_sizes(default_plate_sizes)

    default_paper_types = [
        {
            "paper_type_value": "kraft",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "paper_type_value": "duplex",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "paper_type_value": "imported",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_paper_types(default_paper_types)

    default_rejected_item_types = [
        {
            "rejected_item_type_value": "box",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "rejected_item_type_value": "sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "rejected_item_type_value": "paper",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_rejected_item_types(default_rejected_item_types)

    default_roll_types = [
        {
            "roll_type_value": "5mm",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "roll_type_value": "6mm",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "roll_type_value": "8mm",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "roll_type_value": "10mm",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_roll_types(default_roll_types)

    default_box_types = [
        {
            "box_type_value": "paper",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "box_type_value": "2-ply-sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "box_type_value": "3-ply-sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "box_type_value": "5-ply-sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "box_type_value": "7-ply-sheet",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "box_type_value": "2-ply-roll",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "box_type_value": "die_punch",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "box_type_value": "universal",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_box_types(default_box_types)

    default_piece_types = [
        {
            "single_two_pieces_type_value": "single",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "single_two_pieces_type_value": "two_piece",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_piece_types(default_piece_types)

    default_print_plain_styles = [
        {
            "print_plain_style_value": "printed",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "print_plain_style_value": "plain",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_print_plain_styles(default_print_plain_styles)
