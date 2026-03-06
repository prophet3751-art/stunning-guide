import tkinter as tk                   # Импортируем Tkinter для GUI

# --- Вспомогательные функции цвета и интерполяции ---

def lerp(a, b, t):                     # Линейная интерполяция: смешивает a и b по доле t (0..1)
    return a + (b - a) * t

def rgb_to_hex(r, g, b):               # Перевод из (R,G,B) 0..255 в строку "#RRGGBB"
    return f"#{int(r):02x}{int(g):02x}{int(b):02x}"

def parse_color(widget, color):        # Преобразует цвет Tk ("#RRGGBB"/имя) в (R,G,B) 0..255
    r, g, b = widget.winfo_rgb(color)  # Tk возвращает 0..65535
    return r // 256, g // 256, b // 256

# --- Рисование диагонального градиента ---

def draw_diagonal_gradient(canvas, color1, color2, offset=0, step=1):
    """
    Рисует диагональный градиент, 'сдвинутый' на offset.
    step — плотность: 1 = каждая линия, 2/3 = быстрее, но заметнее полосы.
    """
    w = max(1, canvas.winfo_width())   # Текущая ширина холста (минимум 1, чтобы не делить на 0)
    h = max(1, canvas.winfo_height())  # Текущая высота холста
    steps = w + h                      # Кол-во диагоналей, чтобы покрыть всё окно
    step = max(1, int(step))           # Гарантируем, что шаг не меньше 1

    r1, g1, b1 = parse_color(canvas, color1)   # Начальный цвет -> (R,G,B)
    r2, g2, b2 = parse_color(canvas, color2)   # Конечный цвет -> (R,G,B)

    # Идея: рисуем множество линий под 45°. Для плавной анимации 'зацикливаем' смешивание 0→1→0.
    for i in range(0, steps, step):
        period = 2 * steps                        # Период для цикла 0..1..0 без резкого шва
        p = ((i + offset) % period) / steps       # Нормированная позиция вдоль периода
        t = 2 - p if p > 1 else p                 # Превращаем 0..2 в 0..1..0 (треугольная волна)

        # Смешиваем два цвета по доле t
        r = lerp(r1, r2, t)
        g = lerp(g1, g2, t)
        b = lerp(b1, b2, t)
        color = rgb_to_hex(r, g, b)               # Возвращаем строку "#RRGGBB"

        # Координаты линии под 45°, которая гарантированно пересечёт прямоугольник (w x h)
        x0 = i if i < w else w                    # Левая/верхняя часть — старт X
        y0 = 0 if i < w else i - w                # и старт Y (вверх или смещён вниз)
        x1 = 0 if i < h else i - h                # Финиш X (слева или смещён вправо)
        y1 = i if i < h else h                    # Финиш Y (вниз или у нижней границы)

        canvas.create_line(x0, y0, x1, y1, fill=color)  # Рисуем линию нужного цвета

# --- Настройки анимации (можешь менять под себя) ---

offset = 0                          # Текущий сдвиг градиента (будем увеличивать для "движения")
speed = 3                           # На сколько увеличивать offset за кадр (скорость)
frame_ms = 33                       # Интервал между кадрами, мс (~30 FPS)
color1 = "#6fa3ef"                  # Первый цвет градиента (попробуй поменять)
color2 = "#ff6f61"                  # Второй цвет градиента
density = 1                         # Плотность линий: 1 — гладко; 2/3 — быстрее, но грубее

# --- Колбэки перерисовки и анимации ---

def redraw_static(event=None):      # Перерисовка при изменении размера окна
    canvas.delete("all")            # Чистим холст
    draw_diagonal_gradient(canvas, color1, color2, offset=0, step=density)  # Рисуем статично

def animate():                      # Главный цикл анимации
    global offset                   # Говорим, что изменяем глобальную переменную offset
    canvas.delete("all")            # Чистим холст перед новым кадром
    draw_diagonal_gradient(canvas, color1, color2, offset=offset, step=density)  # Кадр
    offset += speed                 # Сдвигаем "карту смешивания" — градиент визуально едет
    root.after(frame_ms, animate)   # Планируем следующий кадр через frame_ms миллисекунд

# --- Создание окна и холста ---

root = tk.Tk()                      # Создаём главное окно Tkinter
root.title("Диагональный живой градиент")  # Заголовок окна
root.geometry("1280x1024")            # Стартовый размер окна (можно менять)

canvas = tk.Canvas(root, highlightthickness=0, bd=0)  # Холст без рамок
canvas.pack(fill="both", expand=True)                  # Растягиваем на весь доступный размер

canvas.bind("<Configure>", redraw_static)  # При изменении размера — перерисовать статичный кадр
animate()                                   # Запускаем анимацию
root.mainloop()                             # Главный цикл приложения (держит окно открытым)