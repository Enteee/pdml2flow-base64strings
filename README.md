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

Extract all valid base64 data:
```
$ tshark -i any -T pdml 2>/dev/null | pdml2flow +base64strings
{"frames": [1, 2, 5, 7], "path": "frame.interface_name.raw", "raw": "anyanyanyany", "decoded": "b'j|\\x9a\\x9f&\\xa7\\xc9\\xa9\\xf2'"}
{"frames": [1, 2, 5, 7], "path": "sll.etype.raw", "raw": "0x000008000x000008000x000008000x00000800", "decoded": "b'\\xd3\\x1d4\\xd3M<\\xd3M1\\xd3M4\\xd3\\xcd4\\xd3\\x1d4\\xd3M<\\xd3M1\\xd3M4\\xd3\\xcd4'"}
{"frames": [1, 2, 5, 7], "path": "ip.dsfield.raw", "raw": "0x000000000x000000000x000000000x00000000", "decoded": "b'\\xd3\\x1d4\\xd3M4\\xd3M1\\xd3M4\\xd3M4\\xd3\\x1d4\\xd3M4\\xd3M1\\xd3M4\\xd3M4'"}
```

Extract only base64 encoded ascii strings:
```
$ tshark -i any -T pdml 2>/dev/null | pdml2flow +base64strings --ascii
^C{"frames": [66, 80, 84, 103, 106, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145], "path": "http.authorization.raw", "raw": "ZW50ZTpnZ2dnZ2c=", "decoded": "ente:gggggg"}
{"frames": [67, 82, 85, 108, 110], "path": "http.authorization.raw", "raw": "ZW50ZTpnZ2dnZ2c=", "decoded": "ente:gggggg"}
```

Extract only base64 data longer than 100 bytes:
```
$ tshark -i any -T pdml 2>/dev/null | pdml2frame +base64strings '--minlength 100'
{"frames": [74], "path": "ssl.handshake.sig_hash_alg.raw", "raw": "000004030x000005030x000006030x000008040x000008050x000008060x000004010x000005010x000006010x000002030x00000201", "decoded": "b'\\xd3M4\\xd3\\x8d7\\xd3\\x1d4\\xd3M9\\xd3}1\\xd3M4\\xd3\\xad7\\xd3\\x1d4\\xd3M<\\xd3\\x8d1\\xd3M4\\xd3\\xcd9\\xd3\\x1d4\\xd3M<\\xd3\\xad1\\xd3M4\\xd3\\x8d5\\xd3\\x1d4\\xd3M9\\xd3]1\\xd3M4\\xd3\\xad5\\xd3\\x1d4\\xd3M6\\xd3}1\\xd3M4\\xd3m5'"}
```

[pdml2flow]: https://github.com/Enteee/pdml2flow
