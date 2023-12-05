"""Dictionary related utility functions."""

__author__ = "730699792"

from csv import DictReader


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Take in all rows of a csv file and output them as a list of dictionaries."""
    result: list[dict[str, str]] = []
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table:
        result.append(row[column])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a list of rows to a dictionary of columns."""
    result: dict[str, list[str]] = {}
    # loop through column values
    for dic in table:
        for row in dic:
            if row in result:
                result[row].append(dic[row])
            else:
                result[row] = [dic[row]]
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns the first N rows of a table."""
    if (rows >= len(table)):
        return table
    result: dict[str, list[str]] = {}
    for column in table:
        result[column] = []
        for idx in range(0, rows):
            result[column].append(table[column][idx])
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Returns only select columns in a new table."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Merges two tables together."""
    result: dict[str, list[str]] = table1
    for column in table2:
        if (column in table1):
            result[column] += table2[column]
        else:
            result[column] = table2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the occurances of each value in a list."""
    result: dict[str, int] = {}
    for val in values:
        if val in result:
            result[val] += 1
        else:
            result[val] = 1
    return result