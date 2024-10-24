import flet as ft

class Manual(ft.Markdown):
    def __init__(self):
        self.md = """
# Manual
## Features
You can plot the averaged local field potential (LFP) recorded with a 64-ch multielectrode array (MED probe).

## Materials
- 64-ch multielectrode array (MED probe)
- CSV file containing the LFP data for all trials

## Procedure
1. Set the parameters for the LFP plot. The parameters are: the number of trials, the stimulation onset time, the stimulation channel, and the scale of the vertical bar (the horizontal bar indicates 20 ms).
2. Upload the CSV file containing the LFP data.
3. The figure will be displayed below and saved in the directory of the csv file.
"""

        super().__init__(self.md)