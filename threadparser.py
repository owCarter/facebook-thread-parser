import requests
import sys

example = 'python threadparser.py filewithconvo filetosaveparsedconvo'

if __name__ == '__main__':
    thread_file = ''
    output_file = ''
    redact_names = []

    if len(sys.argv) > 1:
        thread_file = sys.argv[1]
        if len(sys.argv) > 2:
            output_file = sys.argv[2]
            if len(sys.argv) > 3:
                redact_names = sys.argv[3].split(',')
        else:
            print('Need more than 1 param! -> ex: %s' % example)
    else:
        print('Need params! -> ex: %s' % example)
