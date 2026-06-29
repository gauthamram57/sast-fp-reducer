"""
Simple logger for controlling CLI output.
"""

VERBOSE = False


def debug(message):

    if VERBOSE:
        print(message)


def info(message):

    print(message)
