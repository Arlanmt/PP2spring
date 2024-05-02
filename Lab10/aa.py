import pygame
import os


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")


font = pygame.font.SysFont(None, 36)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

current_song_index = 0

def play_song():
    pygame.mixer.music.play()


def stop_song():
    pygame.mixer.music.stop()


running = True
while running:
    screen.fill(WHITE)
    text = font.render("Press SPACE to play, S to stop, N for next song, P for previous song", True, BLACK)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_song()
            elif event.key == pygame.K_s:
                stop_song()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_p:
                previous_song()



pygame.quit()