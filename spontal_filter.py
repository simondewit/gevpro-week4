#!/opt/local/bin/python3.4
# Simon de Wit, februari 2015

import xml.etree.ElementTree as ET
import sys


def main(argv):
    inp_f = argv[1]
    outp_f = argv[2]
    tree = ET.parse(inp_f)
    root = tree.getroot()
    for point in root.findall('POINT'):
        bottom = float(point.find('BOTTOM_HZ').text)
        top = float(point.find('TOP_HZ').text)
        start = float(point.find('F0_START').text)
        end = float(point.find('F0_END').text)
        if not bottom <= start <= top or not bottom <= end <= top:
            root.remove(point)
    tree.write(outp_f)



if __name__ == '__main__':
    main(sys.argv)
