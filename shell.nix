with import <nixpkgs> {};

(python.withPackages (ps: [ps.web])).env
