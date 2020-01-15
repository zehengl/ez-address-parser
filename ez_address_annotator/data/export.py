from pathlib import Path
import json
import pickle

here = Path(__file__).parent.absolute()
paths = (here / "../completions").glob("*.json")

results = []
for path in paths:
    with open(path) as f:
        completion = json.load(f)

    result = sorted(
        [
            (
                record["value"]["start"],
                record["value"]["text"],
                record["value"]["labels"][0],
            )
            for record in completion["completions"][0]["result"]
        ],
        key=lambda record: record[0],
    )

    results.append([(record[1], record[2]) for record in result])

with open(here / "data.pkl", "wb") as f:
    pickle.dump(results, f)
