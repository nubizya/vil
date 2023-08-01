import sys

from uvicorn import run
from src.app.main import app  # noqa: F401

if __name__ == "__main__":
    if sys.argv[1] == "prod":
        run("start_vil:app", host="0.0.0.0", port=8000, env_file="env.prod", workers=2)
    elif sys.argv[1] in ["dev", "local", "development"]:
        run(
            "start_vil:app",
            host="127.0.0.1",
            port=8000,
            reload=True,
            env_file="env.dev",
        )
