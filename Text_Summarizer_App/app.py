# fastapi 
from fastapi import FastAPI , Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration , T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates #UI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


# initialzie our fastapi app
app = FastAPI(title="Text Summarizer App" , description= "Text summarization using T5" , version="1.0")

# load model and tokenizer

model = T5ForConditionalGeneration.from_pretrained(
    "Jitender89/t5-text-summarizer-samsum"
)

tokenizer = T5Tokenizer.from_pretrained(
    "Jitender89/t5-text-summarizer-samsum"
)


# device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")   
model.to(device)

# tempalting 
templates = Jinja2Templates(directory=".")


# input schema ffor dialogue => string
class DialogueInput(BaseModel):
    dialogue: str


# summarization function
def summarize_dialogue(dialogue):
    dialogue = re.sub(r"\r\n", " ", dialogue)
    dialogue = re.sub(r"\s+", " ", dialogue)
    dialogue = re.sub(r"<.*?>", " ", dialogue)
    dialogue = dialogue.strip().lower()
    # clean
    # clean

    #tokenize
    inputs = tokenizer(
        dialogue, 
        padding = "max_length",
        max_length = 512,
        truncation = True,
        return_tensors = "pt"
    ).to(device)
    

    #generate the summary => token ids
    model.to(device)
    targets = model.generate(
        input_ids = inputs["input_ids"],
        attention_mask = inputs["attention_mask"],
        max_length = 150,
        num_beams = 4,# 4 diff ouput generate and give the best one 
        early_stopping = True
    )

    # token ids => text(decode)
    summary = tokenizer.decode(targets[0] , skip_special_tokens = True)# EOS , SEP skip 
    return summary

# api endpoint
# get : to get from the server
# post : to send the data
# async : let say we have three task to perform adn we know the first task gonna take ample amount of time then it will side by side start doin the task 2 
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summarize_dialogue(dialogue_input.dialogue)
    return {"summary": summary}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

