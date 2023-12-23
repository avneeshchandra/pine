from datetime import datetime

def init_log(
        timestamp:str,
        log_name:str,
):
    with open(f'{log_name}.txt', 'a+') as file:
        file.write(f'//\\ STARTING LOG: {log_name}\n')
        file.write(f'INITIALIZATION TIME: {timestamp}\n')

def append_log(
        log_line:str,
        log_name:str,
        timestamp:str = None
):
    with open(f'{log_name}.txt', 'a') as file:
        if timestamp:
            file.write(f'{timestamp}: {log_line}\n')
        else:
            file.write(f'{log_line}\n')