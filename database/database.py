import csv
import os
from datetime import date
from pathlib import Path

DATABASE_NAME = 'database.csv'
DATABASE_PATH = os.path.join(Path(__file__).parent.parent, DATABASE_NAME)

CSV_DELIMETER = ','
CSV_QUOTECHAR = '|'
CSV_NEWLINE = ''


def create_database(database_path: str) -> bool:
    """
    Check exists database file.
    :param database_path:
    :return bool:
    """
    if not os.path.exists(database_path):
        return True
    return False


def write_page_database(name: str) -> bool:
    """
    Write new info in database.
    :param name:
    :return: bool
    """
    date_current = date.today()  # Get today data
    try:
        with open(DATABASE_PATH, 'a', newline=CSV_NEWLINE) as csvfile:
            writer = csv.writer(csvfile, delimiter=CSV_DELIMETER,
                                quotechar=CSV_QUOTECHAR, quoting=csv.QUOTE_MINIMAL)
            writer.writerow([name, date_current])  # Write info in database
            return True
    except Exception("Failed to write data to the file.") as ex:
        raise ex


def check_page_database(name: str) -> bool:
    """
    Check info in database
    :param name:
    :return: bool
    """
    if create_database(DATABASE_PATH):  # Create database file if not exists
        open(DATABASE_PATH, 'a').close()

    with open(DATABASE_PATH, newline=CSV_NEWLINE) as csvfile:  # Check info
        reader = csv.reader(csvfile, delimiter=CSV_DELIMETER, quotechar=CSV_QUOTECHAR)
        data = [x[0] for x in reader]
        if name in data:
            return True
        return False
