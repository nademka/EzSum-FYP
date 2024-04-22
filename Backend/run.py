# run.py
import uvicorn

if __name__ == "__main__":
    # uvicorn.run accepts the import string for your FastAPI app instance
    # along with other parameters such as host, port, and reload
    # The "app:app" tells Uvicorn to look for an object named `app`
    # inside a module named `app.py`. If your FastAPI instance is named differently or located in a different file,
    # you will need to modify this string accordingly.
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
