from collections import OrderedDict
import glob
import os
from cStringIO import StringIO

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, 'data')


def escape(string):
    if '\\' in string:
        string = string.replace('\\', '\\\\')

    if '\n' in string:
        string = string.replace('\n', '\\\n')
        
    if '"' in string:
        string = string.replace('"', '\\"')

    return string


def convert_data():
    file_name_pattern = 'x0*.py'
    pattern = os.path.join(DATA_DIR, file_name_pattern)
    data_dict = OrderedDict((i, None) for i in xrange(256))
    for file in glob.iglob(pattern):
        mod_hex_name = os.path.basename(file)[:-3]
        mod_dec_name = int('0' + mod_hex_name, base=16)
        mod = __import__('data.%s' % mod_hex_name, [], [], ['data'])
        data = list(mod.data)
        if len(data) != 256:
            diff = 256 - len(data)
            data.extend(['' for _ in xrange(diff)])
        data_dict[mod_dec_name] = data

    for k, v in data_dict.items():
        if v is None:
            data_dict[k] = ['' for _ in xrange(256)]

    for i in xrange(32, 128):
        data_dict[0][i] = chr(i)

    with open(os.path.join(CUR_DIR, 'data.h'), 'w') as s:
        s.write('char* data[256][256] = {\n')

        for strings in data_dict.values():
            s.write('\t{\n')

            s.write(
                '\n'.join('\t\t"%s",' % escape(string) for string in strings)
            )

            s.write('\n\t},\n')

        s.write('};\n')


if __name__ == '__main__':
    convert_data()
