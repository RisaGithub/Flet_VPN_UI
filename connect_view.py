import flet as ft
import time


class ConnectView(ft.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self.bgcolor = ft.colors.with_opacity(1, "#030611")
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.padding = 0
        self.connect_status_control = ft.Text("Подключиться", size=18)
        self.circle_container = ft.Container(
            ft.Column(
                [self.connect_status_control],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=200,
            border=ft.border.all(2, ft.colors.WHITE),
            width=250,
            height=250,
            on_click=self.start_connect,
            shadow=ft.BoxShadow(
                blur_radius=13,
                color=ft.colors.BLUE_GREY_300,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
        )
        self.connect_circle_stack = ft.Stack([self.circle_container])

        self.controls = [
            ft.Stack(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Column([ft.Container(height=1)]),
                                self.connect_circle_stack,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                        ),
                        expand=True,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[
                                ft.colors.with_opacity(1, "#0f0f34"),
                                ft.colors.with_opacity(1, "#03030f"),
                            ],
                        ),
                        padding=60,
                    ),
                    ft.IconButton(
                        ft.icons.ARROW_BACK,
                        icon_color="white",
                        icon_size=30,
                        padding=30,
                        on_click=lambda _: self.page.go("/login"),
                    ),
                ],
                expand=True,
            )
        ]

    def did_mount(self):
        time.sleep(0.2)
        self.start_connect()
        return super().did_mount()

    def start_connect(self, e=None):
        if self.connect_status_control.value != "Подключено":
            pr = ft.ProgressRing(width=250, height=250, stroke_width=4, color="white")

            self.circle_container.border = None
            self.connect_circle_stack.controls.append(pr)
            self.connect_status_control.value = "Подключение..."
            self.page.update()

            time.sleep(2)

            pr.visible = False

            self.circle_container.shadow.color = ft.colors.with_opacity(1, "#7100ff")
            self.connect_status_control.color = ft.colors.with_opacity(1, "#7100ff")
            self.circle_container.shadow.blur_radius = 20
            self.connect_status_control.value = "Подключено"
            self.circle_container.border = ft.border.all(
                3, ft.colors.with_opacity(1, "#7100ff")
            )

            self.page.update()
            pr.color = "white"
        else:
            self.circle_container.shadow.color = "white"
            self.connect_status_control.color = "white"
            self.circle_container.shadow.blur_radius = 13
            self.connect_status_control.value = "Подключиться"
            self.circle_container.border = ft.border.all(
                3, ft.colors.with_opacity(1, "white")
            )
            self.update()
