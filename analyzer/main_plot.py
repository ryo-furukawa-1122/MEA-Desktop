import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import analysis.waveform as wf
import analysis.plotter as pl
import general.loadings as ld
import general.settings as st

class Analyzer():
    def plot_lfps(self, csv_path: str, parameters: dict):
        """Main function of plotting the LFPs"""
        self.csv_path:str = csv_path
        self.parameters:dict = parameters

        # Load the csv file
        lfps = ld.Loading().read_csv(self.csv_path)
        
        # Set the basic parameters
        FS, CHS, DURATION = st.Settings().set_basic_params()
        TRIALS:int = self.parameters["trials"]
        STIM_TIMING:float = self.parameters["stim_timing"]
        scale:float = self.parameters["scale"]
        stim_ch:int = self.parameters["stim_ch"]

        N:int = int(FS * DURATION)

        t:np.ndarray[float] = np.arange(0, DURATION, 1/FS) * 1e3  # in ms
        averaged_lfps = wf.Waveform().averaged_wave(lfps, CHS, TRIALS, N)

        # Plot the LFPs
        fig = pl.Figure().plot_lfps(t, averaged_lfps, STIM_TIMING, scale, CHS, stim_ch)

        return fig
