import pyautogui
import keyboard
import time
import tkinter as tk
from threading import Thread


# Функция для остановки программы при закрытии окна
def stop_program():
    global running
    running = False
    print("Программа завершена.")
    root.quit()


# Функция для работы с мышью
def move_mouse_and_click():
    while running:
        if keyboard.is_pressed('q'):  # Если нажата клавиша 'q', выходим
            stop_program()
            break

        # Смещаем курсор на 5 пикселей вправо
        pyautogui.move(5, 0)

        # Нажимаем левую кнопку мыши
        pyautogui.click(button='left')
        print("Смещение вправо и нажата левая кнопка.")

        # Ждем 5 секунд
        time.sleep(5)

        # Смещаем курсор на 5 пикселей влево
        pyautogui.move(-5, 0)

        # Нажимаем правую кнопку мыши
        pyautogui.click(button='left')
        print("Смещение влево и нажата левая кнопка.")

        # Ждем 5 секунд
        time.sleep(5)


# Основное окно с Tkinter
root = tk.Tk()
root.title("Mouse Controller")

# Устанавливаем флаг, который будет отвечать за работу цикла
running = True

# Кнопка для закрытия программы
close_button = tk.Button(root, text="Закрыть", command=stop_program)
close_button.pack(padx=10, pady=10)

# Создаем и запускаем поток с движением мыши
thread = Thread(target=move_mouse_and_click)
thread.daemon = True  # Делаем поток фоновым
thread.start()

# Запускаем главный цикл окна
root.mainloop()

# pyinstaller --onefile --windowed screen.py
