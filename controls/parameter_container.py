import flet as ft

class ParameterContainer(ft.Row):
    def __init__(self):
        self.trials = ft.TextField(label="Trials", value="", text_align=ft.TextAlign.LEFT, width=150, height=50)
        self.stim_onset = ft.TextField(label="Stim. onset (ms)", value="", text_align=ft.TextAlign.LEFT, width=150, height=50)
        self.stim_ch = ft.TextField(label="Stim. ch", value="", text_align=ft.TextAlign.LEFT, width=150, height=50)
        self.vscale = ft.TextField(label="Scale (\u03bcV)", value="", text_align=ft.TextAlign.LEFT, width=150, height=50)
        super().__init__([self.trials, self.stim_onset, self.stim_ch, self.vscale], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    def get_parameters(self):
        return {
            "trials": self.trials.value,
            "stim_onset": self.stim_onset.value,
            "stim_ch": self.stim_ch.value,
            "vscale": self.vscale.value
        }
    