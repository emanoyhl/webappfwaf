# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

# Copyright 2025 emanoyhl and emanoyhl.net find me at github.com/emanoyhl 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, request, abort, render_template
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Basic rules to block malicious requests add more patterns here
BLOCKED_PATTERNS = [
    "SELECT",  # SQL Injection attempt
    "UNION",   # SQL Injection attempt
    "<script>", # XSS attack
    "DROP",    # SQL Injection attempt
    "eval(",   # Potential code execution
]

def is_malicious_request(data):
    """Check if the request data contains any malicious patterns."""
    for pattern in BLOCKED_PATTERNS:
        if pattern in data:
            logging.debug(f"Blocked pattern found: {pattern}")
            return True
    return False

@app.before_request
def filter_requests():
    """Filter incoming requests for malicious content."""
    data = request.form.get('data', '') # Get data from form
    logging.debug(f"Received data: {data}") # Log the received data
    if is_malicious_request(data):
        abort(403)  # Forbidden

@app.route('/submit', methods=['POST'])
def submit():
    """Example endpoint to submit data."""
    return "Data submitted successfully!", 200

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/')
def index():
    return "Welcome to the Web Application Firewall!", 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # Run the app with HTTPS
    # app.run(ssl_context=('cert.pem', 'key.pem'), debug=True, port=5000) ensure cert.pem and key.pem are in same dir as script
