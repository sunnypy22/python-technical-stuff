# Method 1: Using ipaddress Module

'''IPv4 Validation
'''

import ipaddress

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

# Example usage
print(is_valid_ipv4("192.168.1.1"))  # Output: True
print(is_valid_ipv4("999.999.999.999"))  # Output: False

'''IPv6 Validation
'''

import ipaddress

def is_valid_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

# Example usage
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Output: True
print(is_valid_ipv6("2001:db8::85a3::8a2e:370:7334"))  # Output: False

# Method 2: Using Regular Expressions

'''IPv4 Validation
'''

import re

def is_valid_ipv4(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(pattern.match(ip))

# Example usage
print(is_valid_ipv4("192.168.1.1"))  # Output: True
print(is_valid_ipv4("999.999.999.999"))  # Output: False

'''IPv6 Validation
'''

import re

def is_valid_ipv6(ip):
    pattern = re.compile(r'([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})')
    return bool(pattern.match(ip))

# Example usage
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Output: True
print(is_valid_ipv6("2001:db8::85a3::8a2e:370:7334"))  # Output: False

# Method 3: Using socket Module

'''IPv4 Validation
'''

import socket

def is_valid_ipv4(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return True
    except socket.error:
        return False

# Example usage
print(is_valid_ipv4("192.168.1.1"))  # Output: True
print(is_valid_ipv4("999.999.999.999"))  # Output: False


'''IPv6 Validation
'''

import socket

def is_valid_ipv6(ip):
    try:
        socket.inet_pton(socket.AF_INET6, ip)
        return True
    except socket.error:
        return False

# Example usage
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Output: True
print(is_valid_ipv6("2001:db8::85a3::8a2e:370:7334"))  # Output: False

# Method 4: Using validators Third-Party Library

'''pip install validators'''

'''Validation'''

import validators

def is_valid_ipv4(ip):
    return validators.ipv4(ip)

def is_valid_ipv6(ip):
    return validators.ipv6(ip)

# Example usage
print(is_valid_ipv4("192.168.1.1"))  # Output: True
print(is_valid_ipv4("999.999.999.999"))  # Output: False
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Output: True
print(is_valid_ipv6("2001:db8::85a3::8a2e:370:7334"))  # Output: False

# Method 5: Custom Function (IPv4 Only)

def is_valid_ipv4(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    return True

# Example usage
print(is_valid_ipv4("192.168.1.1"))  # Output: True
print(is_valid_ipv4("999.999.999.999"))  # Output: False
