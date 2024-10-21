import flet as ft

class ParameterContainer(ft.Row):
    def __init__(self):
        self.trials = ft.TextField(label="Trials", value="20", text_align=ft.TextAlign.LEFT, width=150)
        self.stim_onset = ft.TextField(label="Stim. onset (ms)", value="50", text_align=ft.TextAlign.LEFT, width=150)
        self.stim_ch = ft.TextField(label="Stim. ch", value="43", text_align=ft.TextAlign.LEFT, width=150)
        self.vscale = ft.TextField(label="Scale (\u03bcV)", value="80", text_align=ft.TextAlign.LEFT, width=150)
        super().__init__([self.trials, self.stim_onset, self.stim_ch, self.vscale], alignment=ft.MainAxisAlignment.CENTER)
    
    def get_parameters(self):
        return {
            "trials": self.trials.value,
            "stim_onset": self.stim_onset.value,
            "stim_ch": self.stim_ch.value,
            "vscale": self.vscale.value
        }
        