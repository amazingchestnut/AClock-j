import tkinter as tk
import time

def start_pomodoro_timer(duration):
    root = tk.Tk()
    root.title("专注时钟")
    
    # 创建标签用于显示倒计时时间
    timer_label = tk.Label(root, font=("Helvetica", 48))
    timer_label.pack(pady=20)
    
    def update_timer(remaining_time):
        timer_label.config(text=f"剩余时间: {remaining_time//60:02d}:{remaining_time%60:02d}")
        if remaining_time > 0:
            root.after(1000, update_timer, remaining_time-1)
        else:
            timer_label.config(text="时间到！")
_timer(duration)
    root.mainloop()

# 设置专注时长（以秒为单位）
focus_duration = 25 * 60  # 25分钟

start_pomodoro_timer(focus_duration)
