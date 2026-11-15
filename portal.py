cat << 'EOF' > ~/Noraportal/portal.py
import http.server
import socketserver
import subprocess

INTERFACE = "wlp8s0"   # Wi-Fi hotspot interface (check with 'nmcli device status')
WAN = "enp7s0"         # Internet source interface (check with 'nmcli device status')
PORT = 80

HTML_PAGE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🚐 FBI Surveillance Van 9 — WiFi</title>
  <style>
    body {
      font-family: sans-serif;
      text-align: center;
      padding-top: 20vh;
      background: linear-gradient(135deg, #1a1a2e, #16213e);
      min-height: 80vh;
      margin: 0;
    }
    .card {
      background: white;
      padding: 40px 30px;
      border-radius: 16px;
      max-width: 360px;
      margin: 0 auto;
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
      color: #1a1a2e;
    }
    h1 {
      color: #e63946;
      font-size: 22px;
      margin-bottom: 10px;
    }
    p {
      color: #555;
      font-size: 15px;
      margin-bottom: 25px;
    }
    button {
      background: #1a1a2e;
      color: white;
      border: none;
      padding: 14px 30px;
      font-size: 17px;
      border-radius: 10px;
      cursor: pointer;
      width: 100%;
      font-weight: bold;
    }
    button:hover {
      background: #e63946;
    }
    .footer {
      font-size: 12px;
      color: #999;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>🚐 Welcome!!!</h1>
    <p>Don't worry — we're not actually watching you 😂<br>Just be cool, be nice, enjoy the internet!!!</p>

    <form method="POST" action="/login">
      <button type="submit">✅ I Accept — Connect Me!</button>
    </form>

    <p class="footer">Powered by nitro 7 and blood 🩸⚫</p>
  </div>
</body>
</html>"""

class CaptivePortalHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode("utf-8"))

    def do_POST(self):
        client_ip = self.client_address[0]
        print(f"Authorizing Device IP: {client_ip}")
        subprocess.run(["iptables", "-t", "nat", "-I", "PREROUTING", "1", "-s", client_ip, "-i", INTERFACE, "-p", "tcp", "--dport", "80", "-j", "ACCEPT"])
        subprocess.run(["iptables", "-I", "FORWARD", "1", "-s", client_ip, "-i", INTERFACE, "-o", WAN, "-j", "ACCEPT"])
        
        user_agent = self.headers.get("User-Agent", "").lower()
        if "android" in user_agent:
            # Return HTTP 204 so Android automatically dismisses its captive portal sheet
            self.send_response(204)
            self.end_headers()
        else:
            # Return Apple's expected Success HTML for iOS/macOS
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>")

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), CaptivePortalHandler) as httpd:
    print(f"Noraportal running on {INTERFACE} (port {PORT})...")
    httpd.serve_forever()
EOF
