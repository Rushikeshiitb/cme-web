#!/usr/bin/env python3
"""Build the CME site and serve it locally.

Usage (from the project root, inside the venv):
    python serve.py            # build + serve on http://localhost:8000
    python serve.py --port 9000
    python serve.py --build    # build only, don't serve
"""
import argparse, http.server, os, socketserver, subprocess, sys, functools

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")


def build():
    print("Building site…")
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build.py")], check=True)


def serve(port):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=SITE)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"\n  CME site running →  http://localhost:{port}/index.html\n  (Ctrl-C to stop)\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--build", action="store_true", help="build only, do not serve")
    args = ap.parse_args()
    build()
    if not args.build:
        serve(args.port)
