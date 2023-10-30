# SkyscopeSentinelAI

SkyscopeSentinelAI

SkyscopeSentinelAI is a self-contained script based on the gpt4all and typer packages. It offers a REPL to communicate with a language model similar to the chat GUI application, but more basic.
Features

    REPL interface to interact with the GPT-4 language model
    Support for special commands to control the REPL
    Simple and easy to use

Installation

For Linux platforms:

1. Create a virtual environment:

bash
python3 -m venv SkyscopeSentinelAI-CLI


2. Activate the virtual environment:

```bash
. SkyscopeSentinelAI/bin/activate

3. Install the required libraries:

python3 -m pip install gpt4all typer deepspeed deepthink sentencepiece fastai colossalai news-api live-weather-api horoscope-api transformers datasets accelerate tqdm wandb

Once you have installed the required libraries, you can start the SkyscopeSentinelAI REPL by running the following command:


python app.py repl


## Usage

Once the REPL has started, you can type in prompts and the model will generate responses. You can also use special commands to control the REPL, such as `/reset` to clear the chat history or `/exit` to quit the REPL.

## Example

Here is an example of how to use the SkyscopeSentinelAI REPL:


SkyscopeSentinelAI! Version 1.0.2
Type /help for special commands.

⇢ Hello there.
assistant: Hi, how can I help you?

⇢ What is the meaning of life?
assistant: The meaning of life is a question that has been pondered by philosophers and theologians for centuries. There is no one answer that will satisfy everyone, but some possible answers include finding happiness, making a difference in the world, and connecting with something larger than oneself.

⇢ Thank you for your insights.
assistant: You're welcome.


## License

SkyscopeSentinelAI is licensed under the MIT License.

## Contributing

Contributions to SkyscopeSentinelAI are welcome. Please fork this repository and create a pull request with your changes.

