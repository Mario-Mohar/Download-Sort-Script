import os
import shutil

download_folder = "/Users/mariomohar/Downloads"
pdf_folder = "/Users/mariomohar/Downloads/PDFs"
document_folder = "/Users/mariomohar/Downloads/Documents"
image_folder = "/Users/mariomohar/Downloads/Images"
file_folder = "/Users/mariomohar/Downloads/Files"
video_folder = "/Users/mariomohar/Downloads/Videos"
music_folder = "/Users/mariomohar/Downloads/Music"

folders = [pdf_folder, document_folder, image_folder, file_folder, video_folder, music_folder]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

for filename in os.listdir(download_folder):
    if filename.endswith(".pdf"):
        shutil.move(download_folder+"/"+filename, pdf_folder+"/"+filename)
    elif filename.endswith(".txt") or filename.endswith(".doc") or filename.endswith(".docx") or filename.endswith(".xls") or filename.endswith(".xlsx") or filename.endswith(".ppt") or filename.endswith(".pptx"):
        shutil.move(download_folder + "/" + filename, document_folder + "/" + filename)
    elif filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".gif") or filename.endswith(".svg") or filename.endswith(".psd") or filename.endswith(".ai") or filename.endswith(".eps") or filename.endswith(".raw") or filename.endswith(".indd") or filename.endswith(".tif") or filename.endswith(".tiff"):
        shutil.move(download_folder+"/"+filename, image_folder+"/"+filename)
    elif filename.endswith(".zip") or filename.endswith(".rar") or filename.endswith(".dmg") or filename.endswith(".exe") or filename.endswith(".pkg") or filename.endswith(".iso") or filename.endswith(".tar") or filename.endswith(".gz") or filename.endswith(".7z"):
        shutil.move(download_folder+"/"+filename, file_folder+"/"+filename)
    elif filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mkv"):
        shutil.move(download_folder+"/"+filename, video_folder+"/"+filename)
    elif filename.endswith(".mp3") or filename.endswith(".m4a") or filename.endswith(".flac"):
        shutil.move(download_folder+"/"+filename, music_folder+"/"+filename)
