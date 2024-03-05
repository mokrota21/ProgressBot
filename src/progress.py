import pandas as pd
import numpy as np
from datetime import datetime, timedelta

template = pd.DataFrame(columns=['ID', 'Progress', 'Date'])
class PersonalProgress:
    '''
    This class allows to manipulate progress of person with given ID and eventually save it in file provided by path.
    Variable save_threshold only describes after how much new rows df needs to save.
    If any information existed prior it takes information from given path.
    '''

    def __init__(self, path, ID, save_threshold = 1) -> None:
        self._path = path
        self._ID = ID
        self._counter = 0
        self._save_threshold = save_threshold
        try:
            self._df = pd.read_json(path)
        except FileNotFoundError:
            self._df = pd.DataFrame(columns=['ID', 'Progress', 'Date'])
        self._df['Date'] = pd.to_datetime(self._df['Date'])
    
    # Checking if threshold is exceeded
    @property
    def df(self):
        return self._df
    
    @df.setter
    def df(self, new_df):
        self._counter += len(new_df)- len(self._df)
        self._df = new_df

        if self._counter >= self._save_threshold:
            self._df.to_json(self._path)
            self._counter = 0
            

    # Updates progress based on message
    def update_progress(self, new_progress: str) -> None:
        new_progress = {'ID': self._ID, 'Progress': new_progress, 'Date': datetime.now()}
        self.df = pd.concat([self.df, pd.DataFrame([new_progress])], ignore_index=True)

    #Gets progress in given timeframe
    def get_progress(self, since=datetime(2000, 1, 1), to=datetime(2200, 12, 31)):
        df = self.df
        print(pd.to_datetime(to), pd.to_datetime(since))
        return df.loc[(df['Date'] <= to) & (df['Date'] >= since)]
        
