# Q12. Write a Python program to remove leading zeros from an IP address.


import re


valid_ip = re.compile(r"^[^0]\d{0,3}\.\d{0,3}.\d{0,3}.\d{0,3}")
ip_with_leading_zeros = re.compile(r"^0+\d{0,3}\.\d{0,3}.\d{0,3}.\d{0,3}")


def is_valid(ip):
    if re.match(valid_ip, ip) is not None:
        return ip + " is valid IP"
    elif re.match(valid_ip, ip) is None and \
            re.match(ip_with_leading_zeros, ip) is None:
        return ip + " is invalid IP"
    elif re.match(ip_with_leading_zeros, ip) is not None:
        return "IP after removing leading zeros: " + ip.lstrip("0")


def main():
    ip = input("Please input an IP address : ")
    print(is_valid(ip))


main()
