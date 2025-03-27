import sys

def error_message_detail(error, error_details:sys):
    _,_,exe_tb = error_details.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    error_message = "Error occured python scirpt name {0} line number [{1}]".format(
        file_name, exe_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_details = error_details
        )
    
    def __str__(self):
        return self.error_message
