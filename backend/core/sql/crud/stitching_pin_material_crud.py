from sql import session, logger
from sql.orm_models.stitching_pin_material import StitchingPinMaterial

logging = logger(__name__)


class CRUDStitchingPinMaterial:
    def create(self, **kwargs):
        try:
            logging.info("CRUDStitchingPinMaterial create request")
            material = StitchingPinMaterial(**kwargs)
            with session() as transaction_session:
                transaction_session.add(material)
                transaction_session.commit()
                transaction_session.refresh(material)
            return material.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMaterial create function : {error}")
            raise error

    def read(self, material_id: int):
        try:
            logging.info("CRUDStitchingPinMaterial read request")
            with session() as transaction_session:
                obj: StitchingPinMaterial = transaction_session.query(StitchingPinMaterial).filter(StitchingPinMaterial.material_id == material_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMaterial read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDStitchingPinMaterial read_all request")
            with session() as transaction_session:
                obj: StitchingPinMaterial = transaction_session.query(StitchingPinMaterial).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMaterial read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDStitchingPinMaterial update request")
            with session() as transaction_session:
                transaction_session.query(StitchingPinMaterial).filter(StitchingPinMaterial.material_id == kwargs.get("material_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMaterial update function : {error}")
            raise error

    def delete(self, material_id: int):
        try:
            logging.info("CRUDStitchingPinMaterial delete request")
            with session() as transaction_session:
                obj: StitchingPinMaterial = transaction_session.query(StitchingPinMaterial).filter(StitchingPinMaterial.material_id == material_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDStitchingPinMaterial delete function : {error}")
            raise error
