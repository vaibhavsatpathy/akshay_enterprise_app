from sql import session, logger
from sql.orm_models.layer_types import LayerType

logging = logger(__name__)


class CRUDLayerType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDLayerType create request")
            layer_type = LayerType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(layer_type)
                transaction_session.commit()
                transaction_session.refresh(layer_type)
            return layer_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDLayerType create function : {error}")
            raise error

    def read(self, layer_type_id: int):
        try:
            logging.info("CRUDLayerType read request")
            with session() as transaction_session:
                obj: LayerType = (
                    transaction_session.query(LayerType)
                    .filter(LayerType.layer_type_id == layer_type_id)
                    .first()
                )
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDLayerType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDLayerType read_all request")
            with session() as transaction_session:
                obj: LayerType = transaction_session.query(LayerType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDLayerType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDLayerType update request")
            with session() as transaction_session:
                transaction_session.query(LayerType).filter(
                    LayerType.layer_type_id == kwargs.get("layer_type_id")
                ).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDLayerType update function : {error}")
            raise error

    def delete(self, layer_type_id: int):
        try:
            logging.info("CRUDLayerType delete request")
            with session() as transaction_session:
                obj: LayerType = (
                    transaction_session.query(LayerType)
                    .filter(LayerType.layer_type_id == layer_type_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDLayerType delete function : {error}")
            raise error
