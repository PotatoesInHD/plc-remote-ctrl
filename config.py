import os
import sys

from dotenv import load_dotenv

class EnvVariables():
    def __init__(self) -> None:
        load_dotenv()
        self.TWILIO_API_KEY = os.environ["TWILIO_API_KEY"]
        self.TWILIO_API_SECRET = os.environ["TWILIO_API_SECRET"]
        self.TWILIO_SID = os.environ["TWILIO_SID"]
        self.TO_NUMBER = os.environ["TO_NUMBER"]
        self.FROM_NUMBER = os.environ["FROM_NUMBER"]
        self.EMAIL_PW = os.environ["EMAIL_PW"]
        self.EMAIL_LOGIN = os.environ["EMAIL_LOGIN"]
        self.TO_EMAIL = os.environ["T0_EMAIL"]
        self.PLC_IP = os.environ["PLC_IP"]
