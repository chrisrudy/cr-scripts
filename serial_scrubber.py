import json
import glob
from re import sub

def grab_files():
    path = ('/Users/chrisrudy/Downloads/all/')

    json_glob = glob.glob(f'{path}*.json')
    txt_glob = glob.glob(f'{path}*.txt')

    with open('/Users/chrisrudy/Desktop/serials.txt', 'w+') as new_file:
        for r in txt_glob:
            outfile = open(r, 'r')
            data_list = outfile.readlines()
            writeable_list = '\n'.join(data_list)
            r = sub(f"{path}|-merchant_tokens.txt", " ", r)
            new_file.write(f'{r}: Serial: ' + writeable_list)

    with open('/Users/chrisrudy/Desktop/json_serials.txt', 'w+') as json_file:
        for s in json_glob:
            data = open(s, 'r')
            outfile_j = json.load(data)
            for i in outfile_j:
                serial = i['serial_number']
                s = sub(f"{path}|.json", " ", s)
                json_file.write(f'{s}: Serial: {serial}\n')

grab_files()