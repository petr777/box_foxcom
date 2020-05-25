from colorama import Fore, Back, Style


def log_print(proxy='', url='',  status='', message='', error='', performed = 0, left_execute = 0):

    log_msg = ''
    if message == 'OK':
        log_msg += Fore.GREEN + "OK!\t" + Fore.RESET
    if message == 'BAD':
        log_msg += Fore.RED + "FAIL\t" + Fore.RESET

    log_msg += proxy + '\t'
    log_msg += status + '\t\t'
    log_msg += 'Выполнено: ' + str(performed) + '\t'
    log_msg += 'Осталось: ' + str(left_execute) + '\t\t'
    log_msg += url + '\t\t'
    log_msg += error + '\t\t\t'
    print(log_msg)



