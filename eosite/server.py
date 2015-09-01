#!/usr/bin/env python
import os
import sys

from swampdragon.swampdragon_server import run_server

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eosite.settings")

host_port = sys.argv[1] if len(sys.argv) > 1 else None

run_server(host_port=host_port)
