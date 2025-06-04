import logging
import src.logging_to_file
from src.operations.cover_page_operations  import get_cover_page_display_in_GUI
from src.constans import OPER_GET_LIST_SUCCEEDED, OPER_GET_LIST_FAILED

operation_status = get_cover_page_display_in_GUI()
if operation_status == OPER_GET_LIST_SUCCEEDED:
    logging.info('Cover page list was displayed in GUI')
elif operation_status == OPER_GET_LIST_FAILED:
    logging.warning('No Cover pages to display')