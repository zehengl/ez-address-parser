from pathlib import Path

import pandas as pd

here = Path(__file__).parent.absolute()
paths = (here / "csv").glob("province_*.csv")

samples = [pd.read_csv(path).sample(10, random_state=2020) for path in paths]

df = pd.concat(samples, ignore_index=True)

df.to_csv(here / "seeds.csv", index=False)
