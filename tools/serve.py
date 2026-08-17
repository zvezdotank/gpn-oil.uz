#!/usr/bin/env python3
"""Локальный сервер с «красивыми» адресами: /industrial отдаёт industrial.html.

Так же ведут себя GitHub Pages, Cloudflare Pages и Netlify, поэтому локально
надо проверять именно этот вариант — иначе внутренние ссылки будут врать.
"""
import http.server
import os
import socketserver

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 4326


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def translate_path(self, path):
        p = super().translate_path(path)
        if os.path.isdir(p):
            index = os.path.join(p, "index.html")
            if os.path.exists(index):
                return index
        if not os.path.exists(p) and not p.endswith(".html"):
            html = p + ".html"
            if os.path.exists(html):
                return html
        return p

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            page = os.path.join(ROOT, "404.html")
            if os.path.exists(page):
                body = open(page, "rb").read()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
        super().send_error(code, message, explain)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("http://localhost:%d" % PORT)
        httpd.serve_forever()
