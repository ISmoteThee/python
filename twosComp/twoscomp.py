def to_string(value: int, width: int=None) -> str:
    if width is None:
        width = 658  # TODO choose width based on magnitude of value
    if value < 0:
        value = 2 ** width + value
    template = "{:0" + str(width + 2) + "b}"
    return template.format(value)[2:]

def hex_to_bin(hex_string: str, width: int=None):
    if width==None:
        width = len(hex_string[2:]) * 4
    form_str = f'0{width}b'
    print(form_str)
    return format(int(hex_string, 16), form_str)

def from_string(twoscomp_str: str, width: int=None) -> int:
    if len(twoscomp_str) == 0:
        raise ValueError("input string must be nonempty")
    if twoscomp_str.startswith('0b'):
        twoscomp_str = twoscomp_str[2:]
    if twoscomp_str.startswith('0'):
        return int(twoscomp_str, 2)
    if width is None:
        width = len(twoscomp_str)
    raw_value = int(twoscomp_str, 2)
    return -(2 ** width - raw_value)


def main():
    import sys
    if len(sys.argv) >= 2:
        arg = sys.argv[1]
        width = None if len(sys.argv) == 2 else int(sys.argv[2])
        if arg.startswith('0b'):
            tc = from_string(arg, len(arg[2:]))
            print(tc)
            print(hex(tc))
        elif arg.startswith('0x'):
            if width == None:
                width = (len(arg) - 2) * 4
            value = bin(eval(arg))
            value = value[:2] + value[2:].zfill(width)
            tc = from_string(value, width)
            print(tc)
            print(value[2:])
        else:
            value = int(arg)
            tc = to_string(value, width)
            print(tc)
            print(hex(int('0b' + str(tc),2)))
    return 0


if __name__ == '__main__':
    main()