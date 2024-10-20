import numpy as np

class Waveform():
    def averaged_wave(self, data:np.ndarray[float], CHS:int, TRIALS:int, N:int):
        """Return the averaged waveform"""
        self.data = data
        self.CHS = CHS
        self.TRIALS = TRIALS
        self.N = N

        waves = [[] for ch in range(CHS)]
        for i in range(TRIALS):
            for ch in range(CHS):
                wave = data[i*self.N:self.N*(i+1), ch]
                waves[ch].append(wave)
        
        waves = np.array(waves)
        
        return np.mean(waves, axis=1)