import math
import re


def is_cidr_netmask(netmask):
    netmask = (to_int(netmask) ^ 0xffffffff) + 1
    return (netmask == 0 or math.modf(math.log(netmask, 2))[0] == 0.0)


validator = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$")

def to_int(address):
    match = validator.match(address)
    if match:
        ip = 0

        for i in range(0, 4):
            multiplier = pow(2, 8 * (3 - i))
            value = int(match.group(i + 1))
            if value < 0 or value > 255:
                raise ValueError("IP address %s contains out of range octet %d" % (address, value))
            ip += multiplier * value

        return ip
    raise ValueError("Invalid IP address %s" % address)
