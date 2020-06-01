import logging
import logging.handlers


class Logger:
    '''
    Объект этого класса - обертка над syslog
    Объект будет передаваться во все части, которые должны вести лог
    '''

    _logger = None
    _levels = None

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        handler = logging.handlers.SysLogHandler(address='/dev/log')
        formatter = logging.Formatter('WebServiceSystemctl: %(message)s')
        handler.setFormatter(formatter)

        self._logger.addHandler(handler)

        self._levels = {
                'debug':    self._logger.debug,
                'critical': self._logger.critical,
                'error':    self._logger.error,
                'warning':  self._logger.warning,
                'info':     self._logger.info
            }

    def Message(self, msg:str, level:str = 'error'):
        if level in self._levels.keys():
            self._levels[level](level + ': ' + msg)
        else:
            self.Message('Unknown Level Error...')


def TestLogger():
    log = Logger()
    log.Message('this is debug', 'debug')
    log.Message('this is critical', 'critical')
    log.Message('It is error', 'error')
    log.Message('', 'qwerty')

if __name__ == '__main__':
    TestLogger()