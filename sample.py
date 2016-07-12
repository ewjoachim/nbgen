#!/usr/bin/env python3
import sys
import json

if __name__ == '__main__':
    data = sys.argv[1]
    print(json.dumps([
        {
            "cell_type": "markdown",
            "source": "# Yay {}".format(data),
            "metadata": {'slideshow': {'slide_type': 'slide'}},
        },
        {
            "cell_type": "code",
            "source": data,
            "metadata": {},
        },
        {
            "cell_type": "markdown",
            "source": "This is the second slide",
            "metadata": {'slideshow': {'slide_type': 'slide'}},
        },
    ]))
