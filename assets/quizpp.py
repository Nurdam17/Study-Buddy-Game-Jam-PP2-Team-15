import pygame
import sys
import random

def run_quiz_game():
    pygame.init()

    WIDTH, HEIGHT = 1700, 1000
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    FONT = pygame.font.Font(None, 36)
    uni_img1 = pygame.transform.scale(pygame.image.load("images/backgrounds/uniroom1.png"), (1700, 1465))


    score = 0

    questions = [
        {
            "question": "What is Python?",
            "options": ["A type of snake", "A programming language",
                        "A food item", "A country in Europe"],
            "correct_answer": "A programming language"
        },
        {
            "question": "What is Pygame?",
            "options": ["A type of video game", "A programming language",
                        "A Python library for game development",
                        "An operating system"],
            "correct_answer": "A Python library for game development"
        },
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "correct_answer": "def"
        },
        {
            "question": "What module is used to work with dates and times in Python?",
            "options": ["datetime", "timeanddate", "calendar",
                        "datemanipulation"],
            "correct_answer": "datetime"
        },
        {
            "question": "Which of the following is NOT a valid data type in Python?",
            "options": ["Integer", "Float", "String", "Boolean"],
            "correct_answer": "Float"
        },
        {
            "question": "What method is used to draw a rectangle in Pygame?",
            "options": ["draw_circle()", "draw_triangle()", "draw_rect()",
                        "draw_line()"],
            "correct_answer": "draw_rect()"
        },
        {
            "question": "What function is used to load an image in Pygame?",
            "options": ["load_image()", "load()", "load_image_file()",
                        "image.load()"],
            "correct_answer": "load()"
        },
        {
            "question": "Which of the following is NOT a type of loop in Python?",
            "options": ["for", "while", "loop", "do-while"],
            "correct_answer": "loop"
        },
        {
            "question": "What is the purpose of the pygame.display.set_mode() function in Pygame?",
            "options": ["To set the screen resolution",
                        "To set the background color",
                        "To create a window for the game", "To load an image"],
            "correct_answer": "To create a window for the game"
        }
    ]

    selected_questions = random.sample(questions, 3)
    current_question_index = 0

    def draw_text_in_block(text, block_rect):
        lines = text.split('\n')
        y_offset = block_rect.top + 20  # Начальное смещение по вертикали
        for line in lines:
            text_surface = FONT.render(line, True, BLACK)
            # Проверяем, не выходит ли текст за нижнюю границу блока
            if y_offset + text_surface.get_height() <= block_rect.bottom - 20:
                text_rect = text_surface.get_rect(center=(block_rect.centerx, y_offset))
                SCREEN.blit(text_surface, text_rect)
                y_offset += text_surface.get_height() + 5

    def draw_options_in_block(options, block_rect):
        y_offset = block_rect.top + block_rect.height // 2  # Начальное смещение по вертикали
        for i, option in enumerate(options):
            option_text = FONT.render(option, True, BLACK)
            option_rect = option_text.get_rect(center=(block_rect.centerx, y_offset + i * 50))
            SCREEN.blit(option_text, option_rect)
            pygame.draw.rect(SCREEN, BLACK, option_rect, 2)

    def check_answer(mouse_pos, options, correct_answer):
        for i, option in enumerate(options):
            option_rect = FONT.render(option, True, WHITE).get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))
            if option_rect.collidepoint(mouse_pos):
                return option == correct_answer
        return False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if check_answer(mouse_pos, selected_questions[current_question_index]["options"], selected_questions[current_question_index]["correct_answer"]):
                    score += 1
                current_question_index += 1
                if current_question_index >= len(selected_questions):
                    running = False
                else:
                    SCREEN.fill(WHITE)
                    draw_text_in_block(selected_questions[current_question_index]["question"], pygame.Rect(500, 100, 700, 450))
                    draw_options_in_block(selected_questions[current_question_index]["options"], pygame.Rect(500, 100, 700, 450))

        SCREEN.blit(uni_img1, (0,0))

        if current_question_index < len(selected_questions):
            draw_text_in_block(selected_questions[current_question_index]["question"], pygame.Rect(500, 100, 700, 450))
            draw_options_in_block(selected_questions[current_question_index]["options"], pygame.Rect(500, 100, 700, 450))
        else:
            running = False
            pygame.time.wait(1000)
            return score

        pygame.display.flip()

    score_text = FONT.render(f"Your score: {score}", True, BLACK)
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    SCREEN.blit(score_text, score_rect)
    pygame.display.flip()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    run_quiz_game()
