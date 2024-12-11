from pathlib import Path
import pandas as pd
from typing import Optional


def load_obfuscated_data(index: Optional[int] = None) -> pd.DataFrame:
    """
    Load obfuscated CGM data.

    Parameters
    ----------
    index: Optional integer index of the patient file (0-based).
           If None, loads all patients' data.

    Returns
    -------
    DataFrame containing the obfuscated data
    """
    data_dir = Path(__file__).parent.parent / 'data' / 'obfuscated'
    files = sorted(data_dir.glob("*.csv"))

    if not files:
        raise FileNotFoundError("No data files found in obfuscated directory")

    if index is not None:
        if index < 0 or index >= len(files):
            raise IndexError(f"Index {index} out of range. Available range: 0-{len(files) - 1}")
        return pd.read_csv(files[index])

    return pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
