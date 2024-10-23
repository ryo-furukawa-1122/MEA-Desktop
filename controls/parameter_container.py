import flet as ft

class ParameterContainer(ft.Row):
    def __init__(self):
        self.trials = ft.TextField(label="Trials", value="20", text_align=ft.TextAlign.LEFT, width=150, height=50)
        self.stim_onset = ft.TextField(label="Stim. onset (ms)", value="50", text_align=ft.TextAlign.LEFT, width=150, height=50)
        self.stim_ch = ft.TextField(label="Stim. ch", value="43", text_align=ft.TextAlign.LEFT, width=150, height=50)
        self.vscale = ft.TextField(label="Scale (\u03bcV)", value="80", text_align=ft.TextAlign.LEFT, width=150, height=50)
        super().__init__([self.trials, self.stim_onset, self.stim_ch, self.vscale], alignment=ft.MainAxisAlignment.CENTER)

    def get_parameters(self):
        return {
            "trials": self.trials.value,
            "stim_onset": self.stim_onset.value,
            "stim_ch": self.stim_ch.value,
            "vscale": self.vscale.value
        }
    
#     def __init__(self, value: float, label: str, width: int = 150, height: int = 50):
#         kwargs = {"width": width, "height": height}
#         self.value = value
#         self.label = label
#         self.control = ft.TextField(str(value), label=label, **kwargs, on_change=self.on_change)

#     def on_change(self, e):
#         new_value = e.control.value
#         print(new_value)
#         try:
#             self.value = float(new_value)
#             self.contol.value = new_value
#         except:
#             pass
#         self.control.update()

# class ParameterContainerFields:
#     def __init__(self):
#         self.trials = ParameterContainer(20, "Trials")
#         self.stim_onset = ParameterContainer(50, "Stim. onset (ms)")
#         self.stim_ch = ParameterContainer(43, "Stim. ch")
#         self.vscale = ParameterContainer(80, "Scale (\u03bcV)")
    
#     @property
#     def values(self):
#         return [self.trials, self.stim_onset, self.stim_ch, self.vscale]
    
#     @property
#     def labels(self):
#         return ["Trials", "Stim. onset (ms)", "Stim. ch", "Scale (\u03bcV)"]
    
#     @property
#     def controls(self):
#         return [control.control for control in self.values]

#     def get_parameters(self):
#         print("Called get_parameters")
#         return {
#             "trials": self.trials.control.value,
#             "stim_onset": self.stim_onset.control.value,
#             "stim_ch": self.stim_ch.control.value,
#             "vscale": self.vscale.control.value
#         }
        
# class ParameterSetter(ft.Row):
#     def __init__(self):
#         self.fields = ParameterContainerFields()
#         super().__init__([*self.fields.controls])