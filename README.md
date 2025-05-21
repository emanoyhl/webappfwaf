# WebAppFWAF
Simple web app firewall (waf); uses flask

# Usage
```bash
python waf.py
```

# Setup
```bash
# add more patterns here for other types of attacks
BLOCKED_PATTERNS = [ 
    "SELECT",  # SQL Injection attempt
    "UNION",   # SQL Injection attempt
    "<script>", # XSS attack
    "DROP",    # SQL Injection attempt
    "eval(",   # Potential code execution
]
```
also
```bash
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # Run the app with HTTPS uncomment following line after you have created your cert/key pems and place in same dir as script
    # app.run(ssl_context=('cert.pem', 'key.pem'), debug=True, port=5000) ensure cert.pem and key.pem are in same dir as script
```
