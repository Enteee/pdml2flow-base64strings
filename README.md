# pdml2flow-base64strings
_[pdml2flow] plugin to extract strings encoded in base64_

## Installation

1. Install dependencies: `pip install -r requirements.txt`
2. install plugin: `python setup.py install`

## Usage

```
usage: Extracts all base64 encoded strings [-h] [--minlength MIN_LENGTH]
                                           [--terminator TERMINATORS] [--utf8]
                                           [--ascii]
optional arguments:
  -h, --help            show this help message and exit
  --minlength MIN_LENGTH
                        minimun length of base64 in bytes [default: 6]
  --terminator TERMINATORS
                        Terminating characters of the base64 encoded strings
                        [default: ^\w]
  --utf8                Decoded base64 must be utf8 [default: False]
  --ascii               Decoded base64 must be ascii (implies --utf8)
                        [default: False]
```

## Example

```
$ tshark -i any -T pdml 2>/dev/null | pdml2flow +base64strings
{"frames": [1, 2, 5, 7], "path": "frame.interface_name.raw", "raw": "anyanyanyany", "decoded": "b'j|\\x9a\\x9f&\\xa7\\xc9\\xa9\\xf2'"}
{"frames": [1, 2, 5, 7], "path": "sll.etype.raw", "raw": "0x000008000x000008000x000008000x00000800", "decoded": "b'\\xd3\\x1d4\\xd3M<\\xd3M1\\xd3M4\\xd3\\xcd4\\xd3\\x1d4\\xd3M<\\xd3M1\\xd3M4\\xd3\\xcd4'"}
{"frames": [1, 2, 5, 7], "path": "ip.dsfield.raw", "raw": "0x000000000x000000000x000000000x00000000", "decoded": "b'\\xd3\\x1d4\\xd3M4\\xd3M1\\xd3M4\\xd3M4\\xd3\\x1d4\\xd3M4\\xd3M1\\xd3M4\\xd3M4'"}
{"frames": [1, 2, 5, 7], "path": "ip.id.raw", "raw": "0x000029110x000029120x000029130x00002914", "decoded": "b'\\xd3\\x1d4\\xd3M\\xbd\\xd7]1\\xd3M4\\xdb\\xddv\\xd3\\x1d4\\xd3M\\xbd\\xd7}1\\xd3M4\\xdb\\xddx'"}
{"frames": [1, 2, 5, 7], "path": "ip.flags.raw", "raw": "0x000040000x000040000x000040000x00004000", "decoded": "b'\\xd3\\x1d4\\xd3N4\\xd3M1\\xd3M4\\xe3M4\\xd3\\x1d4\\xd3N4\\xd3M1\\xd3M4\\xe3M4'"}
```



[pdml2flow]: https://github.com/Enteee/pdml2flow
