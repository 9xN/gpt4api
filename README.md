# gpt4api
Artificial Intelligence Application Programming Interface Chatbot Powered by State of the Art models such as gpt3.5-turbo && gpt4

## About
gpt4api is an AI Chatbot API that uses state-of-the-art language models to provide responses to user prompts. The chatbot is powered by models such as gpt3.5-turbo and gpt4. Currently, the application only uses the gpt3.5-turbo model, but support for gpt4 is in progress.

## Usage
To use the application, send a POST request to the server with a JSON payload containing a "prompt" field. The server will respond with the chatbot's response to the prompt.
### YOU CAN EITHER USE THE ALREADY HOSTED API FOUND [HERE](https://ai-api.s0cial.repl.co) OR YOU CAN SELF HOST IT FOLLOWING [THIS](https://github.com/9xN/gpt4api/main/README.md#deployment-)
#### cURL
```bash
curl --location --request POST 'http://localhost:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "prompt": "Hello, how are you?"
}'
```
#### wget
```bash
wget --no-check-certificate --quiet \
  --method POST \
  --timeout=0 \
  --header 'Content-Type: application/json' \
  --body-data '{
  "prompt": "Hello, how are you?"
}
' \
   'http://localhost:5000/'
   ```
#### NodeJS (vanilla)
```js
var https = require('follow-redirects').https;
var fs = require('fs');

var options = {
  'method': 'POST',
  'hostname': 'localhost:5000',
  'path': '/',
  'headers': {
    'Content-Type': 'application/json'
  },
  'maxRedirects': 20
};

var req = https.request(options, function (res) {
  var chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function (chunk) {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });

  res.on("error", function (error) {
    console.error(error);
  });
});

var postData = JSON.stringify({
  "prompt": "Hello, how are you?"
});

req.write(postData);

req.end();
```

#### Python (requests)
```py
import requests
import json

url = "http://localhost:5000/"

payload = json.dumps({
  "prompt": "Hello, how are you?"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```
## Deployment <a name="Deployment"></a>

The application can be deployed on a variety of platforms, including Replit:

#### local


Note: Make sure to have `Python` installed on your system before proceeding with the steps below.


1. Clone the repository and navigate to the project directory
   ```bash
   git clone https://github.com/9xN/gpt4api.git
   cd gpt4api
   ```
2. Install the necessary packages (if needed) using pip:
   ```bash
   pip install Flask
   ```
3. Start the application:
   ```bash
   python gpt4api.py
   ```
4. The application should now be running on `http://127.0.0.1:5000/`. You can test it using a tool such as cURL or Postman.

#### replit


1. Clone the repository and navigate to the project directory
   ```bash
   git clone https://github.com/9xN/gpt4api.git
   cd gpt4api
   ```
2. Create a new Replit project by importing the project directory
3. Set the language to Python set the name to whatever you want
4. Run the application

## Disclaimer

This application is not affiliated with any specific language model provider. The models used by this application have been reverse-engineered to provide an API that is compatible with the models' original API. Use of this application may be subject to the terms of service of the model provider.
