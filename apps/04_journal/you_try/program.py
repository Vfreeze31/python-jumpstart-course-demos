import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------')
    print('     JOURNAL APP')
    print('-----------------------')


def run_event_loop():
    print('What would you like to do?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = str(input('[L]ist entries, [A]dd an entry, E[x]it: ')).lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, i don't understand {}. Please select another command.".format(cmd))

    print('Done. Goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    entries = reversed(data)

    for index, entry in enumerate(entries):
        print('   [{}] - {}'.format(index + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)

if __name__ == '__main__'
    main()