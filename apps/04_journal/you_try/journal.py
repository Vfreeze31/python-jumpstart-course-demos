"""
The journal module.
"""

import os

def load(name):
    """
    This is a description of the defined function

    :param name: is the name of the file to be loaded.
    :return: a structured list of journal items.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
               data.append(entry.rstrip())

    return data



def get_full_pathname(name):
    return os.path.abspath(os.path.join('.', 'journals', name +'.jrl'))

def save(name, data):
    """
    This defined function will save the exisitng journal data.

    :param name: Name of the journal file.
    :param data: The structured journal file to be passed through to the file.
    :return: NOTHING
    """
    filename = get_full_pathname(name)
    print('..... saving to: {}'.format(filename))
    
    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry + '\n')


def add_entry(text, journal_data):
    journal_data.append(text)

