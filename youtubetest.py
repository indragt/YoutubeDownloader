from pytube import YouTube
from tkinter import *


def list_available_format():
    global textfield1
    textfield1 = textfield1.get()

    yt = YouTube(textfield1)
    videos = yt.streams.filter(progressive=True).all()
    sr = 1
    video_formats = {}

    for v in videos:
        video_formats.update({sr: v})
        sr += 1
    for k, v in video_formats.items():
        check_text = str(k) + ':' + str(v)
        check_lable = Label(main_window, text=check_text)
        check_lable.grid(row=k + 3, column=0, sticky=S)
        print(f'{k} --> {v}')


def download_video():
    global textfield2
    textfield2 = textfield2.get()
    print(textfield2)
    yt = YouTube(textfield1)
    videos = yt.streams.filter(progressive=True).all()
    sr = 1
    video_formats = {}

    for v in videos:
        video_formats.update({sr: v})
        sr += 1

    vid = video_formats[int(str(textfield2))]
    destination_path = 'D:\\Test'
    vid.download(destination_path)
    label_status_value = Label(main_window, text='Video Has Been Downloaded Successfully')
    label_status_value.grid(row=2, column=1)


main_window = Tk()
main_window.configure(background='black')
main_window.title('Youtube Downloader')
label_url_name = Label(main_window, text='Address or URL :', bg='red')
label_ur_choice = Label(main_window, text='Your Choice :', bg='red')
label_status = Label(main_window, text='DownloadStatus', bg='red')
textfield1 = Entry(main_window)
textfield2 = Entry(main_window)
available_format_button = Button(main_window, text='Available Format', command=list_available_format, bg='blue')
download_button = Button(main_window, text='Download', command=download_video, bg='blue')

label_url_name.grid(row=0, column=0)
textfield1.grid(row=0, column=1)
available_format_button.grid(row=0, column=2)
label_ur_choice .grid(row=1, column=0)
textfield2.grid(row=1, column=1)
download_button.grid(row=1, column=2)
label_status.grid(row=2, column=0)

main_window.mainloop()
