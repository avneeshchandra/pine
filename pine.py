from datetime import datetime
from good import good_print
from bad import bad_print
from ugly import ugly_print, look_print
from safe import safe_print
import logger

class Pine():
    def __init__(self,log_name:str = 'default',log:bool = True):
        self.log_name = log_name
        self.log = log

        self.init_timestamp = datetime.now()
        self.init_timestamp_str = str(self.init_timestamp).split(".")[0]
        self.line_sep = '---'
        
        self.line = ''.join([self.line_sep for i in range(10)])
        
        logger.init_log(self.init_timestamp_str,self.log_name)
        logger.append_log(log_line=self.line,log_name = self.log_name)
            
        
    def lookup(
            self,
            category:str,
    ):
        if category == '+':
            return good_print
        elif category == '-':
            return bad_print
        elif category == '!':    
            return ugly_print
        elif category == '<':
            return safe_print
        elif category == '>':
            return look_print
        else:
            return print
        
    def preserve(
            self,
            text
            ):
        #save to file
        pass

    def needle(
            self,
            text:str = None
    ):
        """
        + is good
        - is bad
        ! is ugly
        < is safe
        > is attention
        """
        if self.log:
            logger.append_log(log_line=text,log_name = self.log_name,timestamp=str(datetime.now()).split('.')[0])
        self.preserve(text)

        print("Printing",text)
        if text:
            category = text[0]
            func = self.lookup(category)
            func(text)
        else:
            print()
