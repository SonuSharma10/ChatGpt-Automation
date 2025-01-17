# ChatGPT Automation with Selenium 🎨

Welcome to the **ChatGPT Automation** project! This repository provides a Python script that automates interactions with ChatGPT using Selenium. You can automate sending prompts and retrieving responses, making it perfect for structuring and automating tasks like API calls without paying for any premium subscriptions. 

[Watch the Demo Video 🎥](#demo-video)

For cookie handling, I used the **Cookie-Editor** browser extension to extract ChatGPT cookies and saved them in a file named `mycookie.json`.

---

## Features 🎮

- Automates sending multiple prompts to ChatGPT.
- Supports loading cookies for seamless login.
- Handles dynamic content with Selenium waits.
- Save ChatGPT responses directly to text files.

---

## Installation Guide ⚖️

Follow these steps to set up the project on your local machine:

### Prerequisites
1. **Python 3.7+**: Ensure Python is installed on your machine. [Download Python](https://www.python.org/downloads/)
2. **Google Chrome**: Install the latest version of Google Chrome. [Download Chrome](https://www.google.com/chrome/)
3. **ChromeDriver**: Match your Chrome version with the appropriate ChromeDriver.
4. **Install Selenium and Undetected-Chromedriver:**
   ```bash
   pip install selenium undetected-chromedriver
   ```

### Clone the Repository
```bash
git clone https://github.com/SonuSharma10/ChatGpt-Automation.git
cd ChatGpt-Automation
```

### Add Cookies
- Create a `mycookie.json` file in the project directory.

### Run the Script
```bash
python main.py
```

---

## How It Works ⚛️

1. **Load Cookies:** Log in to ChatGPT manually, export your cookies using the Cookie-Editor extension, and load them into the script for authenticated access.
2. **Send Prompts:** A predefined list of prompts is sent to ChatGPT using Selenium.
3. **Retrieve Responses:** The script waits for responses, extracts the content, and saves it to `.txt` files.
4. **Automation Video:** Check out the [Demo Video](#demo-video) to see it in action!

---

## File Structure 📁

```
ChatGpt-Automation/
|-- main.py                # Main automation script
|-- mycookie.json          # Your saved ChatGPT cookies
|-- chatgpt_response1.txt  # Sample response file
|-- README.md              # Documentation
```

---

## Example Prompts 🔹
Here’s a list of sample prompts used in the script:

1. "Give a brief explanation of the UTXO model of Bitcoin."
2. "Which is greater: 9.9 or 9.11?"
3. "Is it okay to automate ChatGPT using Selenium?"

---

## Demo Video 🎥

https://github.com/user-attachments/assets/601d12da-0446-42f9-96c6-2d51363090bc

---

## Contributing 💪

Feel free to contribute to the project! Here’s how:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

