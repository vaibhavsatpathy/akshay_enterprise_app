from sql import session, logger
from sql.orm_models.block_types import BlockType

logging = logger(__name__)


class CRUDBlockType:
    def create(self, **kwargs):
        try:
            logging.info("CRUDBlockType create request")
            block_type = BlockType(**kwargs)
            with session() as transaction_session:
                transaction_session.add(block_type)
                transaction_session.commit()
                transaction_session.refresh(block_type)
            return block_type.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBlockType create function : {error}")
            raise error

    def read(self, block_type_id: int):
        try:
            logging.info("CRUDBlockType read request")
            with session() as transaction_session:
                obj: BlockType = transaction_session.query(BlockType).filter(BlockType.block_type_id == block_type_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDBlockType read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDBlockType read_all request")
            with session() as transaction_session:
                obj: BlockType = transaction_session.query(BlockType).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDBlockType read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDBlockType update request")
            with session() as transaction_session:
                transaction_session.query(BlockType).filter(BlockType.block_type_id == kwargs.get("block_type_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDBlockType update function : {error}")
            raise error

    def delete(self, block_type_id: int):
        try:
            logging.info("CRUDBlockType delete request")
            with session() as transaction_session:
                obj: BlockType = transaction_session.query(BlockType).filter(BlockType.block_type_id == block_type_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBlockType delete function : {error}")
            raise error
