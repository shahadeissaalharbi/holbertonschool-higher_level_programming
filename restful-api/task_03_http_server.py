#!/usr/bin/python3
"""Simple HTTP API built using Python's http.server module."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler that serves a few simple GET endpoints."""

    def do_GET(self):
        """Route GET requests to the appropriate endpoint handler."""
        if self.path == "/":
            self._send_text_response(
                200, "Hello, this is a simple API!"
            )

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json_response(200, data)

        elif self.path == "/status":
            self._send_text_response(200, "OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self._send_json_response(200, info)

        else:
            self._send_text_response(404, "Endpoint not found")

    def _send_text_response(self, status_code, message):
        """Send a plain text response with the given status code."""
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json_response(self, status_code, data):
        """Send a JSON response with the given status code."""
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Starting server on port 8000...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
        httpd.server_close()
