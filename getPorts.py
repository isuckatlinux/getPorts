#!/usr/bin/env python3
import re
import argparse
import os
import pyperclip

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--file', help='Grepeable nmap file', required=True)
args = parser.parse_args()
args = vars(args)


def check_file_exist(file):
    if not os.path.isfile(file):
        raise EOFError(f'File {file} not found!')


def file_to_string(file):
    f = open(file, "r")
    string = f.read()
    f.close()
    return string


def get_ip(string):
    pattern = re.compile(r"Host:.*\(\)")
    matches = pattern.search(string)
    string = matches.group()
    pattern = re.compile(r"[0-9.]+")
    matches = pattern.search(string)
    return matches.group()


def get_data(string):
    host = get_ip(string)
    open_ports = []

    pattern2 = re.compile(r"[0-9]+")
    pattern = re.compile(r"[0-9]+/open")
    matches = pattern.finditer(string)
    for match in matches:
        open_ports.append(pattern2.search(match.group()).group())
    return host, open_ports


def parse_ports(op):
    ports = ''
    for port in op:
        ports += f"{port},"
    ports = ports[:-1]
    return ports


def print_data(h, p):
    print(f'Host -> {h}')
    print(f'Open ports -> {p}')


def copy_clipboard(op):
    pyperclip.copy(op)
    print('Ports copied to the clipboard')


def main():
    file = args['file']
    check_file_exist(file)
    s = file_to_string(file)
    h, op = get_data(s)
    op = parse_ports(op)
    print_data(h, op)
    copy_clipboard(op)


main()
