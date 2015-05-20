from truecraft.app import app
from truecraft.config import _cfg, _cfgi

import os

app.static_folder = os.path.join(os.getcwd(), "static")

import os

if __name__ == '__main__':
    app.run(host=_cfg("debug-host"), port=_cfgi('debug-port'), debug=True)
