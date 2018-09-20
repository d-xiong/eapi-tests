import logging
from datetime import datetime
import os


class BaseLogger(object):
    """The base Logger object."""

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        log_dir = str(dir_path.split("python")[0]) + "python/logs/"

        # The faker lib now outputs its logs as DEBUG. Setting the log level
        #   for faker to be 'ERROR', to stop the spamming of the logs.
        logging.getLogger('faker.factory').setLevel(logging.ERROR)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        if not len(self.logger.handlers):  # Prevent duplicate logs.
            formatter = logging.Formatter(
                '%(asctime)s\t[%(levelname)s]\t%(message)s',
                '%Y-%m-%d %H:%M:%S'
            )
            fh = logging.FileHandler(
                "{0}logs{1}.log".format(
                    log_dir,
                    datetime.today().strftime('%Y%m%d'))
            )
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        self.error_count = 0
        self.step_count = 1

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message, raise_error=False):
        self.logger.error(message)
        self.error_count += 1
        if raise_error:
            raise AssertionError(message)

    def exception(self, message, raise_error=False):
        self.logger.exception(message)
        self.error_count += 1
        if raise_error:
            raise AssertionError(message)

    def critical(self, message):
        self.logger.critical(message)
        self.error_count += 1
        raise AssertionError(message)

    def pass_msg(self, message):
        self.logger.info("PASS - " + message)

    def fail_msg(self, message, raise_error=False):
        self.logger.error(">>>>> FAIL - " + message)
        if raise_error:
            raise AssertionError(message)

    def start_test(self, message):
        self.step_count = 1
        self.logger.info("===== TEST - NAME: {}".format(message))

    def end_test(self):
        self.logger.info("END TEST - ERRORS: {}".format(self.error_count))
