import requests
import tkinter as tk

# UserNotifDisplayView defines the object of interaction with the notification display.
class UserNotifDisplayView:
    _socket: str

    def __init__(self, socket: str):
        self._socket = socket
        self.root = tk.Tk()
        self.root.title("Notification Display")
        self.root.geometry(f"{800}x{600}")
        
        self.root.title("Notification Display")
        self.root.geometry("800x600")

        self.status_var = self._create_status_bar(
            self.root, 
            initial_text="Готов к работе...",
            bg_color="#FFFFFF", 
            fg_color="orange",
            height=25
        )

    def start(self):
        while True:
            msg = "Ожидание получения очереди..."
            resp = requests.get(f"http://{self._socket}/user/invite")
            if resp.status_code < 300:
                data = resp.json()
                msg = f"Талон №{data['ticket_id']}\nПодойдите к окну №{data['window_id']}"
            self._update(msg)


    # update defines the logic of updating the notification display.
    def _update(self, message: str):
        self.status_var.set(message)
        self.root.update()


    # _create_status_bar defines the logic of creating the status bar on the main page.
    def _create_status_bar(self, parent, initial_text, bg_color, fg_color, height):
        status_frame = tk.Frame(parent, bg=bg_color, height=height)
        status_frame.pack(fill=tk.X, pady=(5, 200))
        status_frame.pack_propagate(True)
        
        status_var = tk.StringVar(value=initial_text)
        
        status_label = tk.Label(
            status_frame,
            textvariable=status_var,
            bg=bg_color,
            fg=fg_color,
            font=('Arial', 70, 'normal'),
            padx=10,
            anchor=tk.CENTER,
            justify=tk.CENTER,
            height=30,
            pady=20,
        )
        status_label.pack(fill=tk.Y, expand=True)

        return status_var

