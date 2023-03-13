import tkinter as tk

def draw_shape(x1, y1, x2, y2, w):
    root = tk.Tk()

    root.wait_visibility(root)
    root.wm_attributes("-fullscreen", 1)
    root.wm_attributes("-transparentcolor", root['bg'])

    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=root.winfo_width(), height=root.winfo_height())
    canvas.pack()

    # рисуем мигающий прямоугольник
    def blink_rect(color1, color2):
        canvas.itemconfig(rect, outline=color1)
        root.after(700, lambda: blink_rect(color2, color1))

    rect = canvas.create_rectangle(x1 - (w // 2), y1 - (w // 2), x1 + (w // 2), y1 + (w // 2), outline="red", width=4)
    blink_rect("red", "white")

    # рисуем мигающую стрелку
    arrow_id = canvas.create_line(x1, y1, x2, y2, arrow='last', width=3, fill='red')
    blink = True

    def blink_arrow():
        nonlocal blink
        if blink:
            canvas.itemconfigure(arrow_id, state='hidden')
            blink = False
        else:
            canvas.itemconfigure(arrow_id, state='normal')
            blink = True
        root.after(500, blink_arrow)

    blink_arrow()

    root.mainloop()
