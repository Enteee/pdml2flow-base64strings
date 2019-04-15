#!/usr/bin/env bash
set -exuo pipefail

TOPLEVEL="$( cd "$(dirname "$0")" ; pwd -P )/../"

# install plugin
sudo pip install --upgrade -e "${TOPLEVEL}"

cat <<EOF > "${TOPLEVEL}/README.md"
# pdml2flow-plugin-skeleton [![PyPI version](https://badge.fury.io/py/pdml2flow-plugin-skeleton.svg)](https://badge.fury.io/py/pdml2flow-plugin-skeleton) 
_[pdml2flow] plugin skeleton_

| Branch  | Build  | Coverage |
| ------- | ------ | -------- |
| master  | [![Build Status master]](https://travis-ci.org/Username/pdml2flow-plugin-skeleton) | [![Coverage Status master]](https://coveralls.io/github/Username/pdml2flow-plugin-skeleton?branch=master) |
| develop  | [![Build Status develop]](https://travis-ci.org/Username/pdml2flow-plugin-skeleton) | [![Coverage Status develop]](https://coveralls.io/github/Username/pdml2flow-plugin-skeleton?branch=develop) |

## Prerequisites

$( cat "${TOPLEVEL}/.travis.yml" | 
    sed -n -e '/# VERSION START/,/# VERSION END/ p' |
    sed -e '1d;$d' |
    tr -d \'\"  |
    sed -e 's/\s*-\(.*\)/  -\1/g' |
    sed -e 's/python/\* [python\]/g'
)
* [pip](https://pypi.python.org/pypi/pip)

## Installation

\`\`\`shell
$ sudo pip install pdml2flow-plugin-skeleton
\`\`\`

## Usage

\`\`\`shell
$(python "${TOPLEVEL}/plugin/plugin.py")
\`\`\`

## Example

[pdml2flow]: https://github.com/Enteee/pdml2flow
[python]: https://www.python.org/
[wireshark]: https://www.wireshark.org/

[Build Status master]: https://travis-ci.org/Username/pdml2flow-plugin-skeleton.svg?branch=master
[Coverage Status master]: https://coveralls.io/repos/github/Username/pdml2flow-plugin-skeleton/badge.svg?branch=master
[Build Status develop]: https://travis-ci.org/Username/pdml2flow-plugin-skeleton.svg?branch=develop
[Coverage Status develop]: https://coveralls.io/repos/github/Username/pdml2flow-plugin-skeleton/badge.svg?branch=develop
EOF
