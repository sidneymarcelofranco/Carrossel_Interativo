import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_900

    def move_backward(e):
        carrosel.scroll_to(delta=-200, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carrosel.update()
        
    def move_forward(e):
        carrosel.scroll_to(delta=+200, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carrosel.update()        

    layout = ft.Container(
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.GREY_900),
        content=ft.Column(
            
            controls=[
                carrosel := ft.Row(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Image(
                            src=f'https://picsum.photos/250/300?{num}'
                        ) for num in range(20)

                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.KEYBOARD_ARROW_LEFT, icon_color=ft.colors.WHITE,on_click=move_backward),
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, icon_color=ft.colors.WHITE, on_click=move_forward),
                    ]
                )
            ]
        )

    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
