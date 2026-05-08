from http.server import BaseHTTPRequestHandler
import json
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from google import genai

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            request_json = json.loads(post_data.decode('utf-8'))
            user_message = request_json.get("message", "")

            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("GEMINI_API_KEY is missing from environment variables.")
            
            client = genai.Client(api_key=api_key)
            
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=user_message
            )

            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            response_data = {"reply": response.text}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            error_data = {"error": str(e)}
            self.wfile.write(json.dumps(error_data).encode('utf-8'))