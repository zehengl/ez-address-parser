from pathlib import Path

import pandas as pd

here = Path(__file__).parent.absolute()
paths = (here / "raw").glob("province_*")

csv_folder = here / "csv"
csv_folder.mkdir(exist_ok=True)

for path in paths:
    with open(path) as f:
        address = f.read().splitlines()
    df = pd.DataFrame(dict(address=address))
    df.to_csv(csv_folder / f"{path.stem}.csv", index=False)
