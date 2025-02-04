# Importing The Libraries:
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize The Model And Tokenizer:
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


# Inititialize the FastAPI App:
App = FastAPI()

# Define The Base Model:
class Message(BaseModel):
    user_message: str

@App.post("/chat")
async def chat (message: Message):
    input = tokenizer.decode(message.user_message, return_tensor = "pt")
    response = model.generate(input, num_return_sequences = 1, max_length = 50)
    bot_reply = tokenizer.decode(response[0], skip_special_tokens = True)
    return {"Message": bot_reply}




