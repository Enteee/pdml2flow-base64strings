# vim: set fenc=utf8 ts=4 sw=4 et :
from pdml2flow.plugin import Plugin2
from argparse import ArgumentParser
from base64 import b64decode
from re import findall

AFTER_B64_CHARS = ' ='

argparser = ArgumentParser('Extracts all base64 encoded strings')

def walk(d, path=None):
    for k, v in d.items():
        new_path = '{}.{}'.format(path,k) if path else str(k)
        if isinstance(v, dict):
            walk(v, new_path)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, str):
                    for j in findall(
                        '(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})(?:['+ AFTER_B64_CHARS +']|$)',
                        i
                    ):
                        try:
                            print('{}, {}, {}'.format(
                                new_path,
                                j,
                                b64decode(j,validate=True)
                            ))
                        except:
                            pass

class Plugin(Plugin2):

    @staticmethod
    def help():
        """Return a help string."""
        return argparser.format_help()

    def __init__(self, *args):
        """Called once during startup."""
        argparser.parse_args(args)

    def __deinit__(self):
        """Called once during shutdown."""
        pass

    def flow_new(self, flow, frame):
        """Called every time a new flow is opened."""
        pass

    def flow_expired(self, flow):
        """Called every time a flow expired, before printing the flow."""
        pass

    def flow_end(self, flow):
        """Called every time a flow ends, before printing the flow."""
        pass

    def frame_new(self, frame, flow):
        """Called for every new frame."""
        walk(frame)

if __name__ == '__main__':
    print(Plugin.help())
