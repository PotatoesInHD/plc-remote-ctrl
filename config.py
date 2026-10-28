import os
import sys
import configparser

from dotenv import load_dotenv

from exceptions import FatalConfigError
from utils import get_file_path

'''class EnvVariables:
    def __init__(self) -> None:
        load_dotenv()
        self.TWILIO_API_KEY1 = os.environ["TWILIO_API_KEY"]
        self.TWILIO_API_SECRET = os.environ["TWILIO_API_SECRET"]
        self.TWILIO_SID = os.environ["TWILIO_SID"]
        self.TO_NUMBER = os.environ["TO_NUMBER"]
        self.FROM_NUMBER = os.environ["FROM_NUMBER"]
        self.EMAIL_PW = os.environ["EMAIL_PW"]
        self.EMAIL_LOGIN = os.environ["EMAIL_LOGIN"]
        self.TO_EMAIL = os.environ["T0_EMAIL"]'''


class Config:
    def __init__(self, file_path: str = "config.ini") -> None:
        # Detects if running compiled inside PyInstaller:
        if getattr(sys, "frozen", False):
            # If running as exe then working directory is where sys.executable is
            working_directory = os.path.dirname(os.path.abspath(sys.executable))
        else:
            # If running as py script then working directory is where script is
            working_directory = os.path.dirname(os.path.abspath(__file__))

        config_path = get_file_path(working_directory, file_path)
        c = configparser.ConfigParser()
        c.read(config_path, encoding="utf-8")

        ### still need to rework below here. just copy pasted from previous project as a template.
        ## use env variables as fallbacks
        load_dotenv()
        # [TWILIO]
        self.TWILIO_API_KEY = c.get("TWILIO", "TWILIO_API_KEY", fallback=os.environ["TWILIO_API_KEY"])
        self.TO_PLC_FILE_WRITE_DETECTED_NODE = c.get("OPCUA_NODE", "TO_PLC_FILE_WRITE_DETECTED_NODE")
        self.OPCUA_SERVER_STATE = c.get("OPCUA_NODE", "OPCUA_SERVER_STATE")

        # Detects if configs without fallbacks are empty and creates error message for logging.
        if not self.TO_PLC_HEARTBEAT_NODE:
            raise FatalConfigError(f"Config.ini - TO_PLC_HEARTBEAT_NODE value missing")
        if not self.TO_PLC_FILE_WRITE_DETECTED_NODE:
            raise FatalConfigError(f"Config.ini - TO_PLC_FILE_WRITE_DETECTED_NODE value missing")
        if not self.OPCUA_SERVER_STATE:
            raise FatalConfigError(f"Config.ini - OPCUA_SERVER_STATE value missing")
        if not self.OPCUA_URL:
            raise FatalConfigError(f"Config.ini - OPCUA_URL value missing")
