# Импорт всех ресурсов из модуля main_view_resources
from ai_app_projects.frontend.frontend_resources.main_view_resources import *


# Основная функция приложения, принимающая объект страницы ft.Page
def app(page: ft.Page):
    # Настройка свойств страницы
    page.title = "Тест"  # Заголовок окна
    page.theme_mode = ft.ThemeMode.DARK  # Темная тема
    page.bgcolor = '#03050F'  # Цвет фона страницы
    page.window.height = 715  # Высота окна
    page.window.width = 1200  # Ширина окна
    allowed_file_types = ["xls", "xlsx", "csv", "ods", "xltx", "xlsm", "ots", "dif"]  # Разрешенные типы файлов
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Вертикальное выравнивание по центру
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Горизонтальное выравнивание по центру
    page.padding = ft.Padding(left=10, bottom=10, right=10, top=10)  # Внутренние отступы
    page.fonts = {  # Регистрация пользовательского шрифта
        "Manrope": "C:/Users/User/PycharmProjects/pythonProject5/"
                   "ai_app_projects/assets/Fonts/Manrope-VariableFont_wght.ttf",
    }
    page.window.resizable = False  # Запрет изменения размера окна
    page.update()  # Применение настроек

    # Обработчик выбора файлов
    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            # Получение путей к выбранным файлам
            file_paths = [f.path for f in e.files]
            # Формирование строки с именами файлов
            selected_file_name.value = ", ".join(f.name for f in e.files)
            selected_file_name.update()  # Обновление интерфейса
            # Изменение цвета контейнера для визуальной обратной связи
            selected_file_name_container.bgcolor = '#163B88'
            selected_file_name_container.update()
            return file_paths[0]  # Возврат первого файла
        else:
            # Обработка отмены выбора
            selected_file_name.value = "Отменено!"
            selected_file_name.update()
            return None

    # Создание диалога выбора файлов
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)  # Добавление диалога в слой страницы

    # Создание кнопок интерфейса
    # Кнопка загрузки файла
    upload_file_but = ft.ElevatedButton(
        content=upload_file_but_row,  # Контент кнопки (импортирован)
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=True,
            allowed_extensions=allowed_file_types
        ),
        height=40,
        width=640,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        bgcolor='#163B88'
    )

    # Кнопка запуска расчета
    calcul_start_but = ft.ElevatedButton(
        content=calcul_start_text,  # Текст кнопки (импортирован)
        height=40,
        width=640,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        bgcolor='#163B88'
    )

    # Кнопка скачивания результатов
    result_file_download_but = ft.ElevatedButton(
        content=result_file_row,  # Контент кнопки (импортирован)
        height=50,
        width=440,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
        bgcolor='#163B88'
    )

    # Формирование колонки для загрузки файлов
    upload_column = ft.Column(
        controls=[
            upload_file_but,  # Кнопка загрузки
            selected_file_text,  # Текст "Выбранный файл" (импортирован)
            selected_file_name_container  # Контейнер для отображения имени файла
        ],
        height=590,
        width=265,
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Основная колонка загрузки
    main_upload_column = ft.Column(
        controls=[upload_column, calcul_start_but],  # Колонка + кнопка расчета
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=640,
        width=265
    )

    # Контейнер для блока загрузки
    upload_container = ft.Container(
        content=main_upload_column,
        height=659,
        width=280,
        bgcolor='#192D45',
        alignment=ft.Alignment(0, 0)  # Центрирование содержимого
    )

    # Элементы блока результатов
    # Заголовок результатов
    had_result_text_container = ft.Container(
        content=had_result_text,  # Текст "Результаты" (импортирован)
        height=45,
        width=500,
        bgcolor='#192D45',
        alignment=ft.Alignment(0, 0)
    )

    # Контейнер с результатами расчета
    result_energy_container = ft.Container(
        content=result_energy_row,  # Строка с данными (импортирована)
        bgcolor='#163B88',
        alignment=ft.Alignment(0, 0),
        height=50,
        width=360,
        border_radius=14
    )

    # Контейнер для кнопки скачивания
    result_file_container = ft.Container(
        content=result_file_download_but,
        bgcolor='#192D45',
        height=50,
        width=500,
        alignment=ft.Alignment(0, 0)
    )

    # Основные элементы блока результатов
    # Строка с результатом и кнопкой скачивания
    main_result_row = ft.Row(
        controls=[result_energy_container, result_file_container],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=0
    )

    # Колонка результатов
    main_result_column = ft.Column(
        controls=[
            had_result_text_container,  # Заголовок
            main_result_row,  # Блок с данными и кнопкой
            result_divider,  # Разделитель (импортирован)
            result_graph_img  # График результатов (импортирован)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=640,
        width=860,
        spacing=0
    )

    # Контейнер для всего блока результатов
    main_result_container = ft.Container(
        content=main_result_column,
        width=880,
        height=659,
        alignment=ft.Alignment(0, 1),  # Выравнивание по нижнему краю
        bgcolor='#192D45'
    )

    # Главная строка приложения
    main_row = ft.Row(
        controls=[
            upload_container,  # Блок загрузки
            main_divider,  # Вертикальный разделитель (импортирован)
            main_result_container  # Блок результатов
        ],
        spacing=0,
        expand=True
    )

    # Главный контейнер приложения
    main_container = ft.Container(
        content=main_row,
        bgcolor='#7990A3'  # Цвет фона
    )

    # Добавление контейнера на страницу
    page.add(main_container)


# Запуск приложения
ft.app(target=app)
