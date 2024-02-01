import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK
    
    
    def expand_image(e):
        for c in carrossel.controls:
            c.col = 1
            
        e.control.col = 12 - len(carrossel.controls) + 1    
        carrossel.update()
        
    
    carrossel = ft.ResponsiveRow(
        columns=12,
        spacing=5,
        controls=[
            ft.Container(
            col=1,
            image_src=f'https://picsum.photos/250/300?{num}', 
            image_fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(5),
            on_click=expand_image
              
            ) for num in range (10,18)
        ]
        
    )
    
    carrossel.controls[0].col = 12 - len(carrossel.controls) + 1
    layout = ft.Container(
        width=700,
        height=300,
        bgcolor=ft.colors.GREY_200,
        shadow=ft.BoxShadow(blur_radius=500,color=ft.colors.YELLOW),
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.all(5),
        content=carrossel
    )
    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
