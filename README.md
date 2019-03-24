From the list of available languages I only have experience with
Python 2.x for web development. A little old, I know.

I used [web.py][webpy] to build the server and the standard
library to parse JSON.

If [Nix][nix] is available you can get the dependency by
executing `nix-shell`. In any other case it's assumed it is in
`$PYTHONPATH`.

To start the server simple cd into the repo and then execute
`python server.py`.

Execute `python demo.py` to run a demonstration while the server
is running.

[nix]: https://nixos.org/nix/
[webpy]: http://webpy.org/
