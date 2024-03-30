import os
from PIL import Image, ImageTk
import shutil
import tkinter as tk

class ImageLabeler:
    def __init__(self, folder_path, keep_path, move_path):
        self.folder_path = folder_path
        self.keep_path = keep_path
        self.move_path = move_path
        self.image_files = [f for f in os.listdir(self.folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        self.total_images = len(self.image_files)
        self.idx = 0
        
        self.root = tk.Tk()
        self.root.title("Image Labeler")
        self.root.geometry("800x700")  # Set window size to 800x700 pixels
        
        self.image_label = tk.Label(self.root)
        self.image_label.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        
        self.prev_button = tk.Button(self.button_frame, text="Previous Image (P)", command=self.prev_image)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        
        self.keep_button = tk.Button(self.button_frame, text="Keep (S)", command=self.keep_image)
        self.keep_button.pack(side=tk.LEFT, padx=5)
        
        self.move_button = tk.Button(self.button_frame, text="Move (M)", command=self.move_image)
        self.move_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = tk.Button(self.button_frame, text="Next Image (N)", command=self.next_image)
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        self.quit_button = tk.Button(self.button_frame, text="Quit (Q)", command=self.quit_program)
        self.quit_button.pack(side=tk.LEFT, padx=5)
        
        self.root.bind("<KeyPress>", self.key_pressed)  # Listen for keyboard events
        
        self.show_image()

    def show_image(self):
        if 0 <= self.idx < self.total_images:
            image_path = os.path.join(self.folder_path, self.image_files[self.idx])
            image = Image.open(image_path)
            image = self.resize_image(image, (1200, 600))  # Resize images to 1200x600 pixels
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo
            self.root.title(f"Image Labeler - ({self.idx+1}/{self.total_images}) {self.image_files[self.idx]}")

    def keep_image(self):
        self.idx += 1
        self.show_image()

    def move_image(self):
        if 0 <= self.idx < self.total_images:
            image_path = os.path.join(self.folder_path, self.image_files[self.idx])
            shutil.move(image_path, os.path.join(self.move_path, self.image_files[self.idx]))
            self.idx += 1
            self.show_image()

    def next_image(self):
        self.idx += 1
        self.show_image()
        
    def prev_image(self):
        self.idx -= 1
        self.show_image()

    def quit_program(self):
        self.root.quit()
        self.root.destroy()

    def resize_image(self, image, size):
        return image.resize(size, Image.LANCZOS)  # Use Image.LANCZOS for resizing images instead of Image.ANTIALIAS

    def key_pressed(self, event):
        key = event.keysym
        if key == "s":
            self.keep_image()
        elif key == "m":
            self.move_image()
        elif key == "n":
            self.next_image()
        elif key == "p":
            self.prev_image()
        elif key == "q":
            self.quit_program()

if __name__ == "__main__":
    folder_path = r"D:\YOUR IMAGE FOLDER PATH"
    keep_path = folder_path  # Path to folder where you want to keep the images
    move_path = r"D:\YOUR CLEANED IMAGE FOLDER PATH"  # Path to folder where you want to move the images
    
    app = ImageLabeler(folder_path, keep_path, move_path)
    app.root.mainloop()
