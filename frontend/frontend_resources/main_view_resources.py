import flet as ft

# Ресурсы для элемента "Выбранный файл" (левая панель)
selected_file_text = ft.Text(
    value="Выбранный файл:",
    font_family='Manrope',  # Используемый шрифт
    size=20,                # Размер шрифта
    color='#C1DFF9',        # Цвет текста (голубой)
    weight=ft.FontWeight.W_400  # Толщина шрифта (нормальная)
)

# Поле для отображения имени выбранного файла
selected_file_name = ft.Text(
    font_family='Manrope',
    size=16,
    color='#C1DFF9',
    weight=ft.FontWeight.W_500  # Полужирный
)

# Контейнер для имени файла с оформлением
selected_file_name_container = ft.Container(
    content=selected_file_name,  # Содержимое контейнера
    alignment=ft.Alignment(0, 0),  # Центрирование содержимого
    width=265,                   # Фиксированная ширина
    padding=ft.Padding(left=7, bottom=7, right=7, top=7),  # Внутренние отступы
    border_radius=12             # Закругление углов
)

# Текст для кнопки "Начать расчет"
calcul_start_text = ft.Text(
    value="Начать расчет",
    font_family='Manrope',
    size=20,
    weight=ft.FontWeight.W_500,  # Средняя толщина
    color='#C1DFF9'
)

# Ресурсы для кнопки "Выбрать файл" (основная кнопка загрузки)
upload_file_but_text = ft.Text(
    value="Выбрать файл",
    font_family='Manrope',
    size=20,
    weight=ft.FontWeight.W_500,
    color='#C1DFF9'
)

# Иконка для кнопки загрузки
upload_file_but_icon = ft.Icon(
    name=ft.Icons.UPLOAD_FILE_OUTLINED,  # Стандартная иконка загрузки
    size=30,
    color='#C1DFF9'
)

# Горизонтальное расположение иконки и текста внутри кнопки
upload_file_but_row = ft.Row(
    controls=[upload_file_but_icon, upload_file_but_text],
    height=40,
    width=640,
    spacing=28  # Расстояние между иконкой и текстом
)

# === Ресурсы для правой панели (результаты) ===

# Заголовок раздела результатов
had_result_text = ft.Text(
    value="Результаты",
    font_family='Manrope',
    size=24,
    weight=ft.FontWeight.W_800,  # Очень жирный
    color='#C1DFF9'
)

# Элемент для отображения результата расчета энергии
result_energy_text = ft.Text(
    value="E = no_data",  # Значение по умолчанию
    font_family='Manrope',
    size=20,
    weight=ft.FontWeight.W_700,  # Жирный
    color='#C1DFF9'
)

# Иконка "молния" для визуального обозначения энергии
result_energy_icon = ft.Icon(
    name=ft.Icons.BOLT_ROUNDED,  # Иконка молнии
    size=30,
    color='#C1DFF9'
)

# Горизонтальная компоновка иконки и текста энергии
result_energy_row = ft.Row(controls=[result_energy_icon, result_energy_text])

# Элементы для секции скачивания результатов

# Название файла для скачивания
result_file_name_text = ft.Text(
    value="Spins.csv",  # Имя файла по умолчанию
    font_family='Manrope',
    size=20,
    weight=ft.FontWeight.W_700,
    color='#C1DFF9'
)

# Текст-подсказка для скачивания
result_file_text = ft.Text(
    value="Скачать итоговый файл: ",
    font_family='Manrope',
    size=20,
    weight=ft.FontWeight.W_500,
    color='#C1DFF9'
)

# Иконка скачивания
result_file_icon = ft.Icon(
    name=ft.Icons.DOWNLOAD_ROUNDED,  # Иконка загрузки
    size=30,
    color='#C1DFF9'
)

# Компоновка элементов скачивания в строку
result_file_row = ft.Row(
    controls=[result_file_icon, result_file_text, result_file_name_text],
    alignment=ft.MainAxisAlignment.CENTER  # Центрирование по горизонтали
)

# Элемент для отображения графика результатов
result_graph_img = ft.Image(
    src='F:/Илюша/модики/обои/untitled__by_longlemongrass_djsejp.png',  # Путь к изображению
    width=860,    # Ширина изображения (под размер контейнера)
    height=527,   # Высота изображения
    fit=ft.ImageFit.COVER  # Режим отображения (заполнение с сохранением пропорций)
)

# === Разделители ===

# Горизонтальный разделитель для секции результатов
result_divider = ft.Divider(
    height=10,      # Высота разделителя
    thickness=3,    # Толщина линии
    color='#7990A3'  # Цвет (серо-голубой)
)

# Вертикальный разделитель между левой и правой панелями
main_divider = ft.VerticalDivider(
    width=4,        # Ширина разделителя
    thickness=3,    # Толщина линии
    color='#7990A3'  # Цвет (серо-голубой)
)
