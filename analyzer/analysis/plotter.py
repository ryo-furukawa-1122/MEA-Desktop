import matplotlib.pyplot as plt

class Figure():
    def _set_plot_theme(self):
        """Set the plot theme"""
        plt.rcParams["font.family"] = "Arial"
        plt.rcParams["font.size"] = 16

        kwargs_signal = {
            "color": "black",
            "linewidth": 1.4,
        }
        kwargs_stim = {
            "color": "White",
            "marker": "v",
            "markeredgecolor": "royalblue",
            "linewidth": 1,
            "markersize": 3
        }
        kwargs_baseline = {
            "color": "gray",
            "linewidth": 1,
            "linestyle": "dotted"
        }

        return kwargs_signal, kwargs_stim, kwargs_baseline

    def _delete_axes(self):
        """Delete the axes and spines"""
        plt.tick_params(labelbottom=False,
                        labelleft=False,
                        labelright=False,
                        labeltop=False)
        plt.tick_params(bottom=False,
                        left=False,
                        right=False,
                        top=False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)

    def _set_scale_bars(self, ax, vscale:float, STIM_TIMING:float):
        """Set the scale bars"""
        self.scale = vscale * 2
        self.VSCALE = vscale  # in uV
        self.HSCALE = 20  # in ms
        self.HSCALE_START = STIM_TIMING + 25  # in ms
        self.ax = ax

        kwargs_scale = {
            "color": "black",
            "linewidth": 3
        }

        # Vertical scale bar
        self.ax.plot([self.HSCALE_START + self.HSCALE, self.HSCALE_START+self.HSCALE], [-self.scale*0.9, -self.scale*0.9 + self.VSCALE], **kwargs_scale)
        # Horizontal scale bar
        self.ax.plot([self.HSCALE_START, self.HSCALE_START+self.HSCALE], [-self.scale*0.9, -self.scale*0.9], **kwargs_scale)

    def plot_lfps(self, t:float, averaged_lfps:float, STIM_TIMING:float, vscale:float, CHS:int, stim_ch:int):
        """Plot the waves for all channels"""
        self.averaged_lfps = averaged_lfps
        self.t = t  # in ms
        self.CHS = CHS
        self.scale = vscale * 2  # in uV
        self.STIM_TIMING = STIM_TIMING  # in ms
        self.stim_ch = stim_ch

        kwargs_signal, kwargs_stimuli, kwargs_baseline = self._set_plot_theme()

        START = self.STIM_TIMING - 10
        END = self.STIM_TIMING + 50

        fig = plt.figure(dpi=900)

        for ch in range(self.CHS):
            ax = fig.add_subplot(8, 8, ch+1)

            if ch != self.stim_ch-1:
                ax.plot([START, END], [0, 0], **kwargs_baseline)
                ax.plot(self.t, self.averaged_lfps[ch]*1e3, **kwargs_signal)
                ax.plot(self.STIM_TIMING, self.scale/2 * 0.8, **kwargs_stimuli)

                ax.set_xlim([START, END])
                ax.set_ylim([-self.scale, self.scale/2])

            self._delete_axes()
            
        self._set_scale_bars(ax, vscale, self.STIM_TIMING)

        return fig