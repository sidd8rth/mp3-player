from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

# Change dir path here
global initdir
initdir = 'C:/Users/porwa/newPython/mp3Player/songs_file/'


# GUI Code
root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

# initialise pygame
pygame.mixer.init()

# Functional Python Code


# function to add a song


def play_time():

    if stopped:
        return

    current_time = pygame.mixer.music.get_pos()//1000
    converted_current_time = time.strftime("%M:%S", time.gmtime(current_time))

    # Finding length of active songs
    song = playlist_box.get(ACTIVE)
    song = f"{initdir}{song}.mp3"
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    song_length_converted = time.strftime("%M:%S", time.gmtime(song_length))

    if int(song_slider.get()) == int(song_length):
        stop()
    elif paused:
        pass
        # song_slider.config(value=current_time)
    else:
        # Increase song slider every second and set to value
        next_time = int(song_slider.get()) + 1
        song_slider.config(to=song_length, value=next_time)
        # updating status bar  time with slider time
        converted_current_time = time.strftime("%M:%S", time.gmtime(int(song_slider.get())))
        status_bar.config(text=f"Time Elapsed : {converted_current_time} of {song_length_converted}   ")

    # Print current time and song length in status bar
    if current_time >= 1:
        status_bar.config(text=f"Time Elapsed : {converted_current_time} of {song_length_converted}   ")
    status_bar.after(1000, play_time)


def add_song():
    song = filedialog.askopenfilename(initialdir=initdir, title='Select a song you want to add',
                                      filetype=(('mp3 files', "*.mp3"), ))
    # strip unnecessary from song name
    song = song.replace(initdir, '')
    song = song.replace('.mp3', '')
    playlist_box.insert(END, song)


# function to add many songs from playlist
def add_many_song():
    songs = filedialog.askopenfilenames(initialdir='songs_file', title='Select a song you want to add',
                                        filetype=(('mp3 files', "*.mp3"),))
    # loop thru various song and replace directory from it and insert it
    # strip unnecessary from song name
    for song in songs:
        song = song.replace(initdir, '')
        song = song.replace('.mp3', '')
        playlist_box.insert(END, song)


# delete a song from playlist
def delete_song():
    # anchor means highlighted song, it deletes it from playlist_box
    playlist_box.delete(ANCHOR)


# delete all songs from playlist
def delete_all_songs():
    playlist_box.delete(0, END)

# button function


def play():
    # setting stopped to false as song is being played
    global stopped
    stopped = False
    song = playlist_box.get(ACTIVE)
    song = f"{initdir}{song}.mp3"
    # load and play song with pygame
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_time()


global stopped
stopped = False


def stop():
    # stop song and remove selection
    pygame.mixer.music.stop()
    playlist_box.select_clear(ACTIVE)
    status_bar.config(text=f" ")
    global stopped
    stopped = True

global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # pause
        pygame.mixer.music.pause()
        paused = True


def forward():
    # set values of slider and status bar when song is forwarded or backed
    status_bar.config(text="")
    song_slider.config(value=0)
    # to get song number
    next_to_current_song = playlist_box.curselection()
    # current song + 1
    # print(current_song)
    next_to_current_song = next_to_current_song[0] + 1
    # play next songs
    song = playlist_box.get(next_to_current_song)
    song = f"{initdir}{song}.mp3"
    # load and play song with pygame
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # remove selection from last song
    playlist_box.selection_clear(0, END)
    # moving active bar to next song
    playlist_box.activate(next_to_current_song)
    # selecting active bar
    playlist_box.selection_set(next_to_current_song, last=None)


def back():
    # set values of slider and status bar when song is forwarded or backed
    status_bar.config(text="")
    song_slider.config(value=0)

    previous_to_current_song = playlist_box.curselection()
    # current song - 1
    # print(current_song)
    previous_to_current_song = previous_to_current_song[0] - 1
    # play previous songs
    song = playlist_box.get(previous_to_current_song)
    song = f"{initdir}{song}.mp3"
    # load and play song with pygame
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # remove selection from last song
    playlist_box.selection_clear(0, END)
    # moving active bar to previous song
    playlist_box.activate(previous_to_current_song)
    # selecting active bar
    playlist_box.selection_set(previous_to_current_song, last=None)


def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())


def slider(x):
    song = playlist_box.get(ACTIVE)
    song = f"{initdir}{song}.mp3"
    # load and play song with pygame
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=song_slider.get())

# Create a main frame
main_frame = Frame(root)
main_frame.pack(pady=20)

# create playlist box
playlist_box = Listbox(main_frame, bg='black', fg='green', width=60, selectbackground='green', selectforeground='black')
playlist_box.grid(row=0, column=0)

# Create Volume slider frame
volume_frame = LabelFrame(main_frame, text='Volume')
volume_frame.grid(row=0, column=1, padx=20)

# Creating Volume slider widget
volume_slider = ttk.Scale(volume_frame, from_=1, to=0, orient=VERTICAL, value=0.5, command=volume)
volume_slider.pack(pady=10)
# control frame
control_frame = Frame(main_frame)
control_frame.grid(row=1, column=0, pady=20)

# Defining images
back_btn_img = PhotoImage(file='images/back50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
play_btn_img = PhotoImage(file='images/play50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')

# Creating Button
back_button = Button(control_frame, image=back_btn_img, borderwidth=0, command=back)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
play_button = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)
forward_button = Button(control_frame, image=forward_btn_img, borderwidth=0, command=forward)

back_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)
forward_button.grid(row=0, column=4, padx=10)

#song Slider
song_slider = ttk.Scale(main_frame, from_=0, to=100, orient=HORIZONTAL,length=360, value=0, command=slider)
song_slider.grid(row=2, column=0, padx=20)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add song Menu
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Add Songs', menu=add_song_menu)
# Add one song menu
add_song_menu.add_command(label='Add one song to playlist', command=add_song)
# Add many songs menu
add_song_menu.add_command(label='Add many song to playlist', command=add_many_song)

# Delete song menu
delete_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Delete Songs', menu=delete_song_menu)
delete_song_menu.add_command(label='Delete a song from playlist', command=delete_song)
delete_song_menu.add_command(label='Delete all song from playlist', command=delete_all_songs)


# Status bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Temporary label
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()


