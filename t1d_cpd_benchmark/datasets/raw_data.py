from pathlib import Path
import pandas as pd
from typing import Optional


def load_raw_data(index: Optional[int] = None) -> pd.DataFrame:
    """
    Load raw CGM data.

    Parameters
    ----------
    index: Optional integer index of the patient file (0-based).
           If None, loads all patients' data.

    Returns
    -------
    DataFrame containing the obfuscated data
    """
    data_dir = Path(__file__).parent.parent / 'data' / 'raw'
    files = []
    for file in sorted(data_dir.glob("*.csv")):
        if ('CVGA' in file.name) or ('risk_trace' in file.name) or ('performance' in file.name):
            continue
        files.append(file)

    if not files:
        raise FileNotFoundError("No data files found in raw directory")

    if index is not None:
        if index < 0 or index >= len(files):
            raise IndexError(f"Index {index} out of range. Available range: 0-{len(files) - 1}")
        return pd.read_csv(files[index])

    # If no index specified, concatenate all files
    return pd.concat([pd.read_csv(f) for f in files], ignore_index=True)