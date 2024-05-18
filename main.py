import os
from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import messagebox

def remove_background_from_images(input_folder, output_folder):
    # 입력 폴더와 출력 폴더가 존재하지 않으면 생성합니다.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 입력 폴더 내의 모든 파일을 순회합니다.
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 파일이 이미지인지 확인합니다.
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            with open(input_path, 'rb') as input_file:
                input_image = input_file.read()

            output_image = remove(input_image)
            
            with open(output_path, 'wb') as output_file:
                output_file.write(output_image)

def show_completion_message():
    root = tk.Tk()
    root.withdraw()  # 기본 Tk 윈도우를 숨깁니다.
    messagebox.showinfo("완료", "이미지 배경 제거가 완료되었습니다!")
    root.destroy()

if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"
    
    remove_background_from_images(input_folder, output_folder)
    show_completion_message()