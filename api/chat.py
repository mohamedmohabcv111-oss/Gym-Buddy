from http.server import BaseHTTPRequestHandler
import json
import os
import urllib.request

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

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

            api_key = os.environ.get("GROQ_API_KEY")
            if not api_key:
                raise ValueError("GROQ_API_KEY is missing from environment variables.")
            
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "llama3-8b-8192",
                "messages": [{"role": "user", "content": user_message}]
            }
            
            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))
            
            reply_text = response_json["choices"][0]["message"]["content"]

            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            response_data = {"reply": reply_text}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            error_data = {"error": str(e)}
            self.wfile.write(json.dumps(error_data).encode('utf-8'))