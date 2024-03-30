
# Image Data Cleaning Application

This is a simple Python application for cleaning image data. It allows you to quickly browse through a folder of images, decide whether to keep or move each image, and then perform the corresponding action.

## Features

- Browse through a folder of images.
- Keep or move images to another folder.
- Keyboard shortcuts for quick navigation.
- Resizable image display window.
- Saves progress automatically.
- Easy-to-use graphical interface.

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/image-data-cleaning.git
```

2.  Navigate to the project directory:
```bash
cd image-data-cleaning
```


3.  Install the required dependencies:
```bash
 pip install -r requirements.txt
 ```

4.  Edit the `main.py` file to specify the folder paths for your image data:
```bash
folder_path = r"path\to\your\image\folder"
keep_path = folder_path  # Path to folder where you want to keep the images
move_path = r"path\to\your\cleaned\image\folder"  # Path to folder where you want to move the images
```

5.  Run the application:
```bash
python main.py
```


## Keyboard Shortcuts
-   **S:** Keep the current image.
-   **K:** Move the current image to another folder.
-   **N:** Move to the next image.
-   **P:** Move to the previous image.
-   **Q:** Quit the application.