from fastapi import FastAPI
import uvicorn

app = FastAPI()
items = []

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/items/")
def create_item(name: str):
    new_item = {"id": len(items) + 1, "name": name}
    items.append(new_item)
    return new_item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/search/")
def search_items(q: str = None):
    if q is None:
        return {"result": items}
    filtered = [itm for itm in items if q in itm["name"]]
    return {"query": q, "results": filtered}

if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)
