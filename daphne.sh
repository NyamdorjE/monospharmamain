#!/bin/bash
set -e  # exit on error
. /var/www/monospharm/env/bin/activate
exec daphne -b 0.0.0.0 -p 8080 monospharma.asgi:application
