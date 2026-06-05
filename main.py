import flet as ft


def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.DARK

    def text_name(e):   # e - event
        name = text_input.value.strip()

        if name:
            text_hello.value = f"Добро пожаловать! {text_input.value}"
            text_hello.color = ft.Colors.GREEN_900
            text_input.value = ""
        else:
            text_hello.value = f"Поле ввода имени не заполнено!"
            text_hello.color = ft.Colors.RED_900
            
    text_hello = ft.Text('Hello', size=25)
    text_input = ft.TextField(label="Введите свое имя", on_submit=text_name)
    btn = ft.ElevatedButton('SEND', on_click=text_name)

    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        
    
    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    page.add(text_hello, text_input, btn, theme_btn)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
