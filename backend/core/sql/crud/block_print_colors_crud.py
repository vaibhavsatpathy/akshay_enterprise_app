from sql import session, logger
from sql.orm_models.block_print_colors import BlockPrintColor

logging = logger(__name__)


class CRUDBlockPrintColor:
    def create(self, **kwargs):
        try:
            logging.info("CRUDBlockPrintColor create request")
            color = BlockPrintColor(**kwargs)
            with session() as transaction_session:
                transaction_session.add(color)
                transaction_session.commit()
                transaction_session.refresh(color)
            return color.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBlockPrintColor create function : {error}")
            raise error

    def read(self, color_id: int):
        try:
            logging.info("CRUDBlockPrintColor read request")
            with session() as transaction_session:
                obj: BlockPrintColor = transaction_session.query(BlockPrintColor).filter(BlockPrintColor.color_id == color_id).first()
            return obj.__dict__ if obj is not None else None
        except Exception as error:
            logging.error(f"Error in CRUDBlockPrintColor read function : {error}")
            raise error

    def read_all(self):
        try:
            logging.info("CRUDBlockPrintColor read_all request")
            with session() as transaction_session:
                obj: BlockPrintColor = transaction_session.query(BlockPrintColor).all()
            return [row.__dict__ for row in obj] if obj is not None else []
        except Exception as error:
            logging.error(f"Error in CRUDBlockPrintColor read_all function : {error}")
            raise error

    def update(self, **kwargs):
        try:
            logging.info("CRUDBlockPrintColor update request")
            with session() as transaction_session:
                transaction_session.query(BlockPrintColor).filter(BlockPrintColor.color_id == kwargs.get("color_id")).update(kwargs, synchronize_session=False)
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDBlockPrintColor update function : {error}")
            raise error

    def delete(self, color_id: int):
        try:
            logging.info("CRUDBlockPrintColor delete request")
            with session() as transaction_session:
                obj: BlockPrintColor = transaction_session.query(BlockPrintColor).filter(BlockPrintColor.color_id == color_id).first()
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDBlockPrintColor delete function : {error}")
            raise error
