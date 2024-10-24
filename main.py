import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import os
from pathlib import Path
import re
import controls.parameter_container as pc
import controls.manual as mn
import analyzer.main_plot as mp
import matplotlib

matplotlib.use('agg')

def main(page: ft.Page):
    page.title = "MEA"
    page.padding = 50
    page.scroll = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title = ft.Text("Multielectrode Array"),
        center_title = True,
        bgcolor = ft.colors.with_opacity(ft.colors.WHITE, 0.9),
        elevation_on_scroll = 4,
        shadow_color = ft.colors.SHADOW,
        actions = [
            ft.IconButton(icon=ft.icons.SOURCE_OUTLINED, url="https://github.com/ryo-furukawa-1122/MEA-Desktop", icon_color=ft.colors.BLUE),
            ft.Text("    ")
        ]
    )

    status_text = ft.Text()
    plot_container = ft.Container(visible=False)
    parameter_container = pc.ParameterContainer()

    page.snack_bar = ft.SnackBar(
        content = status_text
    )

    def show_status(status_text: ft.Text):
        page.snack_bar.content = status_text
        page.snack_bar.open = True
        page.update()

    def on_file_selected(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            try:
                status_text.value = "Generating graph..."
                show_status(status_text)
                page.update()

                parameters = parameter_container.get_parameters()

                fig, plot_path = call_analyzer(file_path, parameters)
                
                plot_container.content = MatplotlibChart(fig, expand=True)
                plot_container.visible = True
                status_text.value = f"LFP plot has been saved: {plot_path}"
            except Exception as ex:
                status_text.value = f"Error: {str(ex)}"
            
            page.update()
        
    def call_analyzer(csv_path: str, parameters: dict):
        try:
            fig = mp.Analyzer().plot_lfps(csv_path, parameters)

            csv_path = Path(csv_path).resolve()
            safe_filename = re.sub(r'[^\w\-_\.]', '_', csv_path.stem)
            graph_filename = safe_filename + ".png"

            plot_path = os.path.join(os.path.dirname(csv_path), graph_filename)
            fig.savefig(plot_path, bbox_inches='tight')
            
            return fig, str(plot_path)
        except Exception as e:
            raise ValueError(f"Error: {str(e)}")
        
    file_picker = ft.FilePicker(on_result=on_file_selected)
    page.overlay.append(file_picker)

    button_upload = ft.OutlinedButton("Plot LFP", on_click=lambda _: file_picker.pick_files(allowed_extensions=["csv"]), width=150, height=50, icon=ft.icons.FILE_UPLOAD_ROUNDED, icon_color=ft.colors.BLUE, style=ft.ButtonStyle(color=ft.colors.BLUE))

    manual = ft.ExpansionTile(
        title = ft.Text("Manual"),
        affinity = ft.TileAffinity.PLATFORM,
        controls=[mn.Manual()],
        collapsed_text_color = ft.colors.BLUE,
        text_color = ft.colors.BLUE_200,
    )

    contents = [
        parameter_container,
        ft.Row([button_upload], alignment=ft.MainAxisAlignment.CENTER),
        manual,
        plot_container
    ]

    page.add(
        ft.Column(
            contents,
            spacing=40,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(
    main,
    assets_dir="assets"
)