"""Working with CSV Data."""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Takes in file and stores data in each column."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8") # what is the filename
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_vals(table: list[dict[str, str]], column: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table:
        result.append(row[column])
    return result