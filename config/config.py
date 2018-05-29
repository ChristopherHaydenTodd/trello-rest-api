"""
    Configuration Class and SubClasses for Maintaining
    Global Variables and Tiered config files (Prod, QA, UAT, and Dev)
"""

import os
import logging
import inspect


def get_caller_info():
    """
        Getting Filename and Path of Caller
    """

    frame = inspect.stack()[2]
    module = inspect.getmodule(frame[0])
    caller = module.__file__
    filename = os.path.splitext(os.path.basename(caller))[0]
    current_path = os.path.dirname(os.path.realpath(caller))

    return filename, current_path


class Config():
    """
        Base Config Class
    """

    @classmethod
    def get(cls, env=None, caller_info=True):
        """
            Get specific config instance

            This method will use the value of the env argument (if provided)
            to determine which configuration tier to use.  If not supplied,
            the method will default to the tier that can be determined from
            the hostname command.
        """

        if env is None:
            env = os.environ.get('ENVIRONMENT', None)
            env = 'prod'

        if env in ('prod', 'production'):
            CONFIGS = cls.Production()
        elif env in ('test', 'testing', 'qa'):
            CONFIGS = cls.Test()
        elif env in ('uat'):
            CONFIGS = cls.Uat()
        elif env in ('dev', 'development'):
            CONFIGS = cls.Development()
        else:
            error_message = 'Cannot Determine Environment'
            logging.error(error_message)
            raise(error_message)

        if caller_info:
            CONFIGS.FILENAME, CONFIGS.CURRENT_PATH = get_caller_info()

        return CONFIGS

    class Production():
        """
            Production instance of base class
        """

        ###
        # Environmental Variable Configs
        ###

        ENV = 'prod'

        ###
        # Trello Configs
        ###

        TRELLO_APP_KEY = None
        TRELLO_APP_TOKEN = None

        ###
        # LOG CONFIGS
        ###

        LOG_LEVEL = logging.INFO
        LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
        LOG_DATEFORMAT = '%a, %d %b %Y %H:%M:%S'
        LOG_FILEMODE = 'a'
        LOG_BASE_PATH = '../log/'

        def get_logging(self):
            """
                Setting logging module to default configurations

            Examples:
                >>> from scripts_capacity.config.config import Config
                >>> CONFIGS = Config.get()
                >>> logging = CONFIGS.get_logging()
            """

            logging.basicConfig(
                level=self.LOG_LEVEL, format=self.LOG_FORMAT,
                datefmt=self.LOG_DATEFORMAT, filemode=self.LOG_FILEMODE,
                filename='{0}{1}.log'.format(
                    self.LOG_BASE_PATH, self.FILENAME)
            )

            return logging

    class Uat(Production):
        """
            UAT instance of base class
        """

        ###
        # Environmental Variable Configs
        ###

        ENV = 'uat'

    class Test(Uat):
        """
            Test instance of base class
        """

        ###
        # Environmental Variable Configs
        ###

        ENV = 'qa'

    class Development(Test):
        """
            Development instance of base class
        """

        ###
        # Environmental Variable Configs
        ###

        ENV = 'dev'

        ###
        # LOG CONFIGS
        ###

        LOG_LEVEL = logging.DEBUG
