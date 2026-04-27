# music_player.py
import pygame
import os
import sys

def play_music(file_path):
    pygame.mixer.init()
    if not os.path.exists(file_path):
        print("File not found.")
        return
    
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Now playing: {file_path}")
        
        while pygame.mixer.music.get_busy():
            # Keep the script running
            pygame.time.Clock().tick(10)
            
        print("Playback finished.")
    except Exception as e:
        print(f"Error playing music: {e}")

def main():
    print("Music Player")
    print("Enter the path to an MP3 file to play.")
    file_path = input("Path: ")
    play_music(file_path)

if __name__ == "__main__":
    import pygame
    main()