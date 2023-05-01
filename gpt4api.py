import json, queue, re, threading, urllib.request, urllib.parse
from http import HTTPStatus
from typing import Generator
from flask import Flask, request, jsonify

class Completion:
    part1 = '{"role":"assistant","id":"chatcmpl'
    part2 = '"},"index":0,"finish_reason":null}]}}'
    regex = rf'{part1}(.*){part2}'
    message_queue = queue.Queue()
    stream_completed = False

    @staticmethod
    def request(prompt: str):
        headers = {
            'authority': 'chatbot.theb.ai',
            'content-type': 'application/json',
            'origin': 'https://chatbot.theb.ai',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        }

        data = json.dumps({'prompt': prompt}).encode('utf-8')
        req = urllib.request.Request('https://chatbot.theb.ai/api/chat-process', data=data, headers=headers)

        with urllib.request.urlopen(req) as response:
            for chunk in response:
                Completion.handle_stream_response(chunk)
            if response.getcode() != HTTPStatus.OK:
                raise Exception(f"Error: {response.getcode()} {response.reason}")
        Completion.stream_completed = True

    @staticmethod
    def create(prompt: str) -> Generator[str, None, None]:
        threading.Thread(target=Completion.request, args=[prompt]).start()

        while not Completion.stream_completed or not Completion.message_queue.empty():
            try:
                message = Completion.message_queue.get(timeout=0.01)
                for message in re.findall(Completion.regex, message.decode()):
                    yield json.loads(Completion.part1 + message + Completion.part2)['delta']
            except queue.Empty:
                pass

    @staticmethod
    def handle_stream_response(chunk):
        Completion.message_queue.put(chunk)

app = Flask(__name__)

@app.route("/", methods=["POST"])
def complete():
    if not request.is_json:
        return jsonify({"error": "Request must contain JSON data."}), 400
    completions = []
    prompt = request.json.get("prompt")
    if not prompt:
        return jsonify({"error": "Request JSON data must contain a 'prompt' field."}), 400
    for token in Completion.create(prompt):
        completions.append(token)
    full_completion = "".join(completions)
    return full_completion

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
