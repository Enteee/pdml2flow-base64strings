# vim: set fenc=utf8 ts=4 sw=4 et :
from pdml2flow.plugin import Plugin2
from argparse import ArgumentParser
from base64 import b64decode
from re import findall
from binascii import Error
from json import dumps

argparser = ArgumentParser('Extracts all base64 encoded strings')

DEFAULT_MIN_LENGTH = 6
argparser.add_argument(
    '--minlength',
    dest='min_length',
    default=DEFAULT_MIN_LENGTH,
    type=int,
    help='minimun length of base64 in bytes [default: {}]'.format(
        DEFAULT_MIN_LENGTH
    )
)

DEFAULT_TERMINATORS = '^\w'
argparser.add_argument(
    '--terminator',
    dest='terminators',
    default=DEFAULT_TERMINATORS,
    type=str,
    help='Terminating characters of the base64 encoded strings [default: {}]'.format(
        DEFAULT_TERMINATORS,
    )
)

DEFAULT_UTF8 = False
argparser.add_argument(
    '--utf8',
    dest='utf8',
    default=DEFAULT_UTF8,
    action='store_true',
    help='Decoded base64 must be utf8 [default: {}]'.format(
        DEFAULT_UTF8,
    )
)

DEFAULT_ASCII = False
argparser.add_argument(
    '--ascii',
    dest='ascii',
    default=DEFAULT_ASCII,
    action='store_true',
    help='Decoded base64 must be ascii (implies --utf8) [default: {}]'.format(
        DEFAULT_ASCII,
    )
)

def walk(d, path=None):
    for k, v in d.items():
        new_path = '{}.{}'.format(path,k) if path else str(k)
        if isinstance(v, dict):
            yield from walk(v, new_path)
        elif isinstance(v, list):
            if not all(isinstance(i, str) for i in v):
                return
            for b64 in findall(
                '(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})(?:['+ ARGS.terminators +']|$)',
                ''.join(v)
            ):
                if len(b64) > ARGS.min_length:
                    try:
                        decoded = b64decode(b64, validate=True)
                    except (TypeError, Error):
                        return
                    if ARGS.utf8:
                        try:
                            decoded = decoded.decode('utf-8')
                        except UnicodeDecodeError:
                            return
                        if ARGS.ascii:
                            try:
                                if not all(ord(c) < 128 for c in decoded):
                                    return
                            except TypeError:
                                return
                    yield {
                        'path': new_path,
                        'raw': b64,
                        'decoded': str(decoded),
                    }

class Plugin(Plugin2):

    @staticmethod
    def help():
        """Return a help string."""
        return argparser.format_help()

    def __init__(self, *args):
        """Called once during startup."""
        global ARGS
        ARGS = argparser.parse_args(args)
        if ARGS.ascii:
            ARGS.utf8 = True

    def flow_end(self, flow):
        for result in walk(flow.frames):
            print(
                dumps({
                **{
                    'frames': flow.frames['num']['raw']
                },
                **result
                })
            )

if __name__ == '__main__':
    print(Plugin.help())
