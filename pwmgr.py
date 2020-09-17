# import signal
from PasswordManager import APP, DB, db_filename
import os
import argparse

_prog_description="""
Application to spin up back end service for password manager,
initialize database/config file for the back end service, or
to delete the database file as specified in the config file.
"""
_start_description="""
Start up the back end service for the password manager. If the
database file is not found, then the program wil prompt user to
run the program again with the --init prompt.
"""
_init_description="""
Initialize database file and populate tables with schemas
"""

if __name__ == "__main__":
    # TODO: mutually exclusive arguments to create DB/delete DB/run
    ap = argparse.ArgumentParser(description=_prog_description)
    grp = ap.add_mutually_exclusive_group()
    grp.add_argument("--start", action="store_true", default=False,
                     help=_start_description)
    grp.add_argument("--init", action="store_true", default=False,
                     help=_init_description)
    args = ap.parse_args()

    if args.start:
        if os.path.exists(f"{db_filename}"):
            APP.run(debug=True)
        else:
            print(f"Database file {db_filename} does not exist. Run '{__file__} --init' first")
    elif args.init:
        DB.create_all()
    else:
        print("Run with --start")
