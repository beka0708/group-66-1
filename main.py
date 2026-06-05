import flet as ft


def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []

    greeting_text = ft.Text("История приветствий: ")

    def text_name(e):   # e - event
        name = text_input.value.strip()

        if name:
            text_hello.value = f"Добро пожаловать! {text_input.value}"
            text_hello.color = ft.Colors.GREEN_900
            text_input.value = ""
            greeting_history.append(name)
            greeting_text.value = f"История приветствий: \n" + "\n".join(greeting_history)

        else:
            text_hello.value = f"Поле ввода имени не заполнено!"
            text_hello.color = ft.Colors.RED_900
            
    text_hello = ft.Text('Как тебя зовут?', size=25)
    text_input = ft.TextField(label="Введите свое имя", on_submit=text_name, expand=False)
    btn = ft.ElevatedButton('SEND', on_click=text_name)

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История приветствий: "

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        
    
    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    main_object = ft.Row(
        controls=[text_input, btn, clear_button],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    text_row = ft.Row(
        controls=[text_hello],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(text_row, main_object, theme_btn, greeting_text)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
