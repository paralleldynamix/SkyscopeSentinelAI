Skyscope Sentinel AI

Copyright (c) 2023 Skyscope Sentinel Intelligence

SkyscopeSentinelAI is a self-contained script based on the gpt4all and typer packages. It offers a REPL to communicate with a language model similar to the chat GUI application, but more basic.

Features

    REPL interface to interact with the GPT-4 language model
    Support for special commands to control the REPL
    Simple and easy to use

Installation

For Linux platforms:

Create a virtual environment:

bash
python3 -m venv SkyscopeSentinelAI-CLI


Activate the virtual environment

. SkyscopeSentinelAI/bin/activate

Install the required libraries
    
pip3 install gpt4all typer deepspeed deepthink sentencepiece fastai colossalai news-api live-weather-api horoscope-api  transformers datasets accelerate tqdm wandb
   
For Windows platforms:
   
py -3 -m venv SkyscopeSentinelAI-CLI
SkyscopeSentinelAI-CLI\Scripts\activate
py -m pip install gpt4all typer

Installation Notes: If having any difficulties installing pip packages please append to end of list --break-system-packages. Usually this type of issue can arise if not using a Python virtual env for installation but I do list the solution in case anyone does face issues with installation of pip libraries.

Usage

Once you have installed the required libraries, you can start the SkyscopeSentinelAI REPL by running the following command:

Within a Linux Terminal or other:

python app.py repl
[This will commence download of the default chatbot model quantized 4q for perfect performance on any PC or Laptop]

Or run the amazing code completion and generation model starcoder using this automated script:

Linux:
mkdir -p ~/.starcoder/ && curl -L https://gpt4all.io/models/gguf/starcoder-q4_0.gguf -o ~/.starcoder/starcoder-q4_0.gguf
wget https://github.com/paralleldynamix/SkyscopeSentinelAI/blob/main/app.py -O ~/.starcoder/app.py
cd ~/.starcoder/ && python app.py repl --model starcoder-q4_0.gguf

Windows [You can usually use the same code as above for Linux provided you have installed the Windows Subsystem for Linux by opening PowerShell as Administrator and typing in 'wsl --install' then wsl --install -d Ubuntu' ]

# Create the directory if it doesn't exist
if (!Test-Path -Path ~/.starcoder) {
    New-Item -Path ~/.starcoder -ItemType Directory -Force
}

# Download the StarCoder model
Invoke-WebRequest -Uri "https://gpt4all.io/models/gguf/starcoder-q4_0.gguf" -OutFile "~/.starcoder/starcoder-q4_0.gguf" -UseBasicParsing

# Download the app.py file
Invoke-WebRequest -Uri "https://github.com/paralleldynamix/SkyscopeSentinelAI/blob/main/app.py" -OutFile "~/.starcoder/app.py" -UseBasicParsing

# Navigate to the directory
cd ~/.starcoder

# Start the REPL with the StarCoder model
py app.py repl --model starcoder-q4_0.gguf


Once the REPL has started, you can type in prompts and the model will generate responses. You can also use special commands to control the REPL, such as `/reset` to clear the chat history or `/exit` to quit the REPL.

License

Skyscope Sentinel AI is licensed under the MIT License.
