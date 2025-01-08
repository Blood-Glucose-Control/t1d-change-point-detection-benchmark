#  TODO: Add a base class once we have more data to load

from datasets import Dataset, load_dataset
from typing import Optional, List, Union, Dict
import pandas as pd


class T1dCpd:
    def __init__(self):
        # Dataset is a 6 months dataset
        # TODO: Point to the lastest dataset
        path = "Toooony/t1d_cpd_benchmark_dataset"
        ds = load_dataset(path, split="train")

        self.train_duration = 1 * 30
        self.test_duration = 1 * 30

        self.splits = []

        # TODO: Remove these columns as they won't exist in the latest data
        self.df = ds.to_pandas().drop(
            columns=["Unnamed: 0.1", "Unnamed: 0", "food_glycemic_index", "affects_iob", "affects_fob", "dose_units"])

    # Data_set
    def split_df(self, split="all") -> list[dict]:
        """
        Splits time series data for each patient into train/test/validation sets.

        The function divides each patient's temporal data into three consecutive periods:
        - Training: First 4 * 30 days
        - Test: Following 1 * 30 days
        - Validation: Remaining days

        Parameters:
            split (str): Data split to return ("train", "test", "val"). Default to "all"

        Returns:
           list[dict]: List of dictionaries for each patient containing:
               - 'id': Patient identifier
               - 'train': DataFrame with first 4 months of data
               - 'test': DataFrame with next 1 month of data
               - 'val': DataFrame with final 1 month of data
        """

        # Separate each patient based on 'id'
        for _, patient in self.df.groupby('id'):
            # Sort by time within each group
            patient = patient.set_index('date')
            patient.index = pd.DatetimeIndex(patient.index)
            patient.sort_index(inplace=True)

            start_time = patient.index[0]
            train_end = start_time + pd.Timedelta(days=self.train_duration)
            test_end = train_end + pd.Timedelta(days=self.test_duration)

            split_data = {
                'id': patient['id'].iloc[0]
            }

            if split == "train":
                split_data['train'] = patient[start_time:train_end]
            elif split == "test":
                split_data['test'] = patient[train_end:test_end]
            elif split == "val":
                split_data['val'] = patient[test_end:]
            else:
                split_data.update({
                    'train': patient[start_time:train_end],
                    'test': patient[train_end:test_end],
                    'val': patient[test_end:]
                })

            self.splits.append(split_data)

        return self.splits

    def loader(
            self,
            split: str = "all",
            patient_ids: Optional[List[int]] = None
    ) -> list[dict]:
        """
        Load patient data based on specified split and patient IDs.

        Args:
            split (str): Data split to return ("train", "test", "val"). Default to all
            patient_ids (List[str], optional): List of specific patient IDs to fetch. Default return all patients

        Returns:
            List[Dict[str, Dataset]]:
                If split specified: Returns Dataset for that split
                If split="all": Returns Dict with all splits {"train": DataFrame, "test": DataFrame, "val": DataFrame}
        """
        # Filter patients if IDs provided
        data = self.split_df(split=split)
        if patient_ids:
            data = [x for x in data if x['id'] in patient_ids]

        return data



dataset = T1dCpd()
patients = dataset.loader("train", patient_ids=[1, 3, 5])
print(patients)
