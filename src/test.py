import pandas as pd
from datetime import datetime
import numpy as np
from progress import PersonalProgress

Erbol = PersonalProgress('test.json', "#ERBOL", 0)
progress = '+40-64'
Erbol.update_progress(progress)
progress2 = '-40-64'
Erbol.update_progress(progress2)
since = datetime.strptime('2024-03-04', '%Y-%m-%d').date()
to = datetime.strptime('2024-03-09', '%Y-%m-%d').date()

print(Erbol.get_progress(since, to))