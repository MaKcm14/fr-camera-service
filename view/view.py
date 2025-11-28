import time
import base64
from flask import Flask, jsonify, send_from_directory
from services.server.interactor import FlowInteractor

class Controller:
    _flow: FlowInteractor
    _read_delay: float

    def __init__(self, flow: FlowInteractor, read_delay: float):
        self._flow = flow
        self._read_delay = read_delay
        self.app = Flask(__name__)
        self.config_endpoints()


    def config_endpoints(self):
        self.app.add_url_rule("/", view_func=self.index)
        self.app.add_url_rule("/enqueue", view_func=self.handler_get_frame)


    def index(self):
        return send_from_directory('static', 'index.html')


    def handler_get_frame(self):
        time.sleep(self._read_delay)

        msg = f"Ещё чуть-чуть...\nЗаписываем Вас в очередь..."
        dto, frame = self._flow.notify()

        if frame is not None:
            frame = base64.b64encode(frame).decode('utf-8')
        else:
            return jsonify({"error": "camera API's error"}), 400

        if dto.enqueued:
            msg = f"Вы были записаны.\nВаш талон: №{dto.ticket_id}"

        return jsonify({
            "ticket_id": dto.ticket_id,
            "image_bytes": frame,
            "message": msg
        }), 200


    def run(self):
        self.app.run(host="localhost", port=9090)


# import time
# import tkinter as tk

# from io import BytesIO
# from PIL import Image, ImageTk
# from services.server.interactor import FlowInteractor

# # InfoDisplayView defines the logic of the user's GUI.
# class InfoDisplayView:
#     _flow: FlowInteractor
#     _read_delay: float

#     def __init__(self, flow: FlowInteractor, read_delay: float):
#         self._flow = flow
#         self._read_delay = read_delay

#         self.root = tk.Tk()
#         self.root.title("Information Display")
#         self.root.geometry(f"{800}x{600}")
        
#         self.root.title("Status Display")
#         self.root.geometry("800x600")
#         self.current_image = None
        
#         self.image_frame = tk.Frame(self.root, bg='#D2691E')
#         self.image_frame.pack(fill=tk.BOTH, expand=True)
        
#         self.image_label = tk.Label(self.image_frame, bg='#FAEBD7')
#         self.image_label.pack(fill=tk.BOTH, expand=True)

#         self.status_var = self._create_status_bar(
#             self.root, 
#             initial_text="Готов к работе...",
#             bg_color="#4682B4", 
#             fg_color="white",
#             height=25
#         )


#     # run starts the UI.
#     def run(self):
#         while True:
#             #time.sleep(self._read_delay)
#             dto, frame = self._flow.notify()

#             if frame is not None:
#                 self._update_image(frame)

#             if dto.enqueued:
#                 self._update_status(f"Вы были записаны.\nВаш талон: №{dto.ticket_id}")
#             else:
#                 self._update_status(f"Ещё чуть-чуть...\nЗаписываем Вас в очередь...")
#             self.root.update()


#     # close releases the resources.
#     def close(self):
#         self._flow.close()


#     # _update_status defines the logic of updating the status-bar's string.
#     def _update_status(self, message: str):
#         self.status_var.set(str(message))


#     # _update_image defines the logic of updating the image on the main page.
#     def _update_image(self, image_bytes: bytes):
#         try:
#             image = Image.open(BytesIO(image_bytes))

#             label_width = 800
#             label_height = 600

#             image = self._resize_image(image, label_width, label_height)
#             self.current_image = ImageTk.PhotoImage(image)
#             self.image_label.configure(image=self.current_image)

#         except Exception as e:
#             pass


#     # _create_status_bar defines the logic of creating the status bar on the main page.
#     def _create_status_bar(self, parent, initial_text, bg_color, fg_color, height):
#         status_frame = tk.Frame(parent, bg=bg_color, height=height)
#         status_frame.pack(fill=tk.X, pady=(5, 200))
#         status_frame.pack_propagate(True)
        
#         status_var = tk.StringVar(value=initial_text)
        
#         status_label = tk.Label(
#             status_frame,
#             textvariable=status_var,
#             bg=bg_color,
#             fg=fg_color,
#             font=('Arial', 30, 'normal'),
#             padx=10,
#             anchor=tk.CENTER,
#             justify=tk.CENTER,
#             height=30,
#             pady=20,
#         )
#         status_label.pack(fill=tk.Y, expand=True)

#         return status_var


#     # _resize_image defines the logic of resizing the getting image.
#     def _resize_image(self, image, max_width, max_height):
#         original_width, original_height = image.size
        
#         ratio = min(max_width/original_width, max_height/original_height)
        
#         new_width = int(original_width * ratio)
#         new_height = int(original_height * ratio)
        
#         return image.resize((new_width, new_height), Image.Resampling.LANCZOS)
