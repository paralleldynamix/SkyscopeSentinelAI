import importlib.metadata
import io
import sys
from collections import namedtuple
from typing_extensions import Annotated

import typer
from gpt4all import GPT4All
from transformers import AutoModelForCausalLM
from news_api import NewsAPI
from live_weather_api import LiveWeatherAPI
from horoscope_api import HoroscopeAPI
from datasets import load_dataset
from accelerate import Accelerator

MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, how can I help you?"},
]

SPECIAL_COMMANDS = {
    "/reset": lambda messages: messages.clear(),
    "/exit": lambda _: sys.exit(),
    "/help": lambda _: print("Special commands: /reset, /exit, and /help"),
}

VersionInfo = namedtuple('VersionInfo', ['major', 'minor', 'micro'])
VERSION_INFO = VersionInfo(1, 0, 2)
VERSION = '.'.join(map(str, VERSION_INFO))  # convert to string form, like: '1.2.3'

CLI_START_MESSAGE = f"""

    /\ /\
    /  \/  \
    / /\  /\ \
    / /__\/__\ \
    / /\________\ \
    / / \/_____\ \ \
/ /   \/___\ \ \ \
\ \_____/____\ \ \ \
 \_____\______\ \___\
 _____/________\_____/
 / /__\/_____\ \____/
/ / \/___\ \ \___\
\ \_____/____\ \____/
\ \_____/______\_____/

Skyscope Sentinel AI! Version {VERSION}
Type /help for special commands.

"""

# create typer app
app = typer.Typer()

# load the GPT-4 model
model = AutoModelForCausalLM.from_pretrained("mistral-7b-instruct-v0.1.Q4_0.gguf")

# create a GPT4All instance with the loaded model
gpt4all_instance = GPT4All(model)

# create clients for the NewsAPI, LiveWeatherAPI, and HoroscopeAPI
news_api_client = NewsAPI("YOUR_API_KEY")
live_weather_api_client = LiveWeatherAPI("YOUR_API_KEY")
horoscope_api_client = HoroscopeAPI("YOUR_API_KEY")

# load a dataset of text and code
dataset = load_dataset("text", data_files={"train": "train.txt"})

# split the dataset into training and validation sets
train_dataset, validation_dataset = dataset.split("train", "validation")

# train the model on the training set using the accelerator
accelerator = Accelerator()
gpt4all_instance.train(train_dataset, accelerator=accelerator)

# evaluate the model on the validation set using the accelerator
gpt4all_instance.evaluate(validation_dataset, accelerator=accelerator)

@app.command()
def repl():
    """The CLI read-eval-print loop."""

    use_new_loop = False
    try:
        version = importlib.metadata.version('gpt4all')
        version_major = int(version.split('.')[0])
        if version_major >= 1:
            use_new_loop = True
    except:
        pass  # fall back to old loop

    if use_new_loop:
        _new_loop()
    else:
        _old_loop()


def _old_loop():
    while True:
        message = input(" ⇢ ")

        # Check if special command and take action
        if message in SPECIAL_COMMANDS:
            SPECIAL_COMMANDS[message](MESSAGES)
            continue

        # if regular message, append to messages
        MESSAGES.append({"role": "user", "content": message})

        # execute chat completion and ignore the full response since
        # we are outputting it incrementally
        full_response = gpt4all_instance.chat_completion(
            MESSAGES,
            # preferential kwargs for chat ux
            logits_size=0,
            tokens_size
            n_past=0,
            n_ctx=0,
            n_predict=200,
            top_k=40,
            top_p=0.9,
            temp=0.9,
            n_batch=9,
            repeat_penalty=1.1,
            repeat_last_n=64,
            context_erase=0.0,
            # required kwargs for cli ux (incremental response)
            verbose=False,
            streaming=True,
        )

        # record assistant's response to messages
        MESSAGES.append(full_response.get("choices")[0].get("message"))
        print()  # newline before next prompt


def _new_loop():
    with gpt4all_instance.chat_session():
        while True:
            message = input(" ⇢ ")

            # Check if special command and take action
            if message in SPECIAL_COMMANDS:
                SPECIAL_COMMANDS[message](MESSAGES)
                continue

            # if regular message, append to messages
            MESSAGES.append({"role": "user", "content": message})

            # execute chat completion and ignore the full response since
            # we are outputting it incrementally
            response_generator = gpt4all_instance.generate(
                message,
                # preferential kwargs for chat ux
                max_tokens=200,
                temp=0.9,
                top_k=40,
                top_p=0.9,
                repeat_penalty=1.1,
                repeat_last_n=64,
                n_batch=9,
                # required kwargs for cli ux (incremental response)
                streaming=True,
            )
            response = io.StringIO()
            for token in response_generator:
                print(token, end='', flush=True)
                response.write(token)

            # record assistant's response to messages
            response_message = {
                'role': 'assistant',
                'content': response.getvalue()
            }
            response.close()
            gpt4all_instance.current_chat_session.append(response_message)
            MESSAGES.append(response_message)
            print()  # newline before next prompt


@app.command()
def version():
    """The CLI version command."""

    print(f"skyscope-sentinel-ai v{VERSION}")


if __name__ == "__main__":
    app()
