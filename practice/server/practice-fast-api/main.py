from fastapi import FastAPI
import uvicorn
from string_ops import reverse_str, letter_counts_map, remove_every_third, remove_vowels, to_upper

app = FastAPI()

@app.get("/reverse")
def reverse_str_(strung: str):
    return reverse_str(strung)

@app.get("/uppercase{text}")
def to_upper_(string: str):
    return to_upper(string)

@app.post("/remove-vowels")
def remove_vowels_(s: str):
    return remove_vowels(s)

@app.post("/remove-every-third")
def remove_every_third_(s: str):
    return remove_every_third(s)

@app.post("/letter-counts")
def letter_counts_map_(s: str):
    return letter_counts_map(s)


if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)
