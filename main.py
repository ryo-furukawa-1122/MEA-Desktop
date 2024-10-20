import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
import re
import controls.parameter_container as pc
import analyzer.main_plot as mp

def main(page: ft.Page):
    page.title = "MEA"
    page.padding = 50

    status_text = ft.Text()
    plot_container = ft.Container(visible=False)

    def on_file_selected(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            try:
                status_text.value = "Generating graph..."
                page.update()

                parameters = pc.ParameterContainer().get_parameters()
                fig, plot_path = call_analyzer(file_path, parameters)
                
                plot_container.content = MatplotlibChart(fig)
                plot_container.visible = True
                status_text.value = f"Scatter Plot has been saved: {plot_path}"
            except Exception as ex:
                status_text.value = f"Error: {str(ex)}"
            
            page.update()
        
    def call_analyzer(csv_path: str, parameters: dict):
        try:
            fig = mp.Analyzer().plot_lfps(csv_path, parameters)

            # ---
            # df = pd.read_csv(csv_path)

            # fig, ax = plt.subplots(figsize=(10, 8))
            # ax.scatter(df.iloc[:, 0], df.iloc[:, 5])
            
            csv_path = Path(csv_path).resolve()
            safe_filename = re.sub(r'[^\w\-_\.]', '_', csv_path.stem)
            graph_filename = safe_filename + ".png"

            plot_path = os.path.join(os.path.dirname(csv_path), graph_filename)
            fig.savefig(plot_path)
            
            return fig, str(plot_path)
        except Exception as e:
            raise ValueError(f"Error: {str(e)}")
        
    file_picker = ft.FilePicker(on_result=on_file_selected)
    page.overlay.append(file_picker)

    page.add(
        ft.ElevatedButton("File Upload", on_click=lambda _: file_picker.pick_files(allowed_extensions=["csv"])),
        pc.ParameterContainer(),
        status_text,
        plot_container
    )

ft.app(target=main)