# import signal
from PasswordManager import PasswordManager


if __name__ == "__main__":
    pm = PasswordManager("pwfile.db", "test")
    pm.app.run()