import pygame
import sys
import random

def run_quiz_game():
    pygame.init()

    WIDTH, HEIGHT = 1700, 1000
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    BLACK = (255, 255, 255)
    WHITE = (0, 0, 0)

    FONT = pygame.font.Font(None, 36)

    score = 0
    uni_img2 = pygame.transform.scale(pygame.image.load("images/backgrounds/uniroom3.png"), (1700, 1465))
    questions = [
    {
        "question": "Who was the founder of the Kazakh Khanate?",
        "options": ["Kasym Khan", "Abulkhair Khan", "Ablai Khan", "Kerei Khan"],
        "correct_answer": "Kerei Khan"
    },
    {
        "question": "When did Kazakhstan gain independence from the Soviet Union?",
        "options": ["1990", "1991", "1992", "1993"],
        "correct_answer": "1991"
    },
    {
        "question": "Which famous Silk Road city is located in present-day Kazakhstan?",
        "options": ["Samarkand", "Bukhara", "Almaty", "Tashkent"],
        "correct_answer": "Almaty"
    },
    {
        "question": "Who was the first President of Kazakhstan?",
        "options": ["Nursultan Nazarbayev", "Kassym-Jomart Tokayev", "Askar Akayev", "Islam Karimov"],
        "correct_answer": "Nursultan Nazarbayev"
    },
    {
        "question": "What was the name of the Kazakh nomadic horsemen known for their military skill?",
        "options": ["Cossacks", "Bashkirs", "Saka", "Tatars"],
        "correct_answer": "Saka"
    },
    {
        "question": "Which famous historical figure invaded Kazakhstan in the 13th century?",
        "options": ["Genghis Khan", "Alexander the Great", "Attila the Hun", "Julius Caesar"],
        "correct_answer": "Genghis Khan"
    },
    {
        "question": "Which body of water forms part of Kazakhstan's border with Russia?",
        "options": ["Caspian Sea", "Black Sea", "Aral Sea", "Baltic Sea"],
        "correct_answer": "Caspian Sea"
    },
    {
        "question": "What major event led to a significant decrease in the population of Kazakhstan in the early 20th century?",
        "options": ["Civil War", "Famine", "Pandemic", "Industrial Revolution"],
        "correct_answer": "Famine"
    },
    {
        "question": "Which ancient civilization had significant interactions with the people of what is now Kazakhstan?",
        "options": ["Egyptian", "Mesopotamian", "Chinese", "Indus Valley"],
        "correct_answer": "Chinese"
    }
]

    selected_questions = random.sample(questions, 3)
    current_question_index = 0

    def draw_text_in_block(text, block_rect):
        lines = text.split('\n')
        y_offset = block_rect.top + 20  # Начальное смещение по вертикали
        for line in lines:
            text_surface = FONT.render(line, True, WHITE)
            # Проверяем, не выходит ли текст за нижнюю границу блока
            if y_offset + text_surface.get_height() <= block_rect.bottom - 20:
                text_rect = text_surface.get_rect(center=(block_rect.centerx, y_offset))
                SCREEN.blit(text_surface, text_rect)
                y_offset += text_surface.get_height() + 5

    def draw_options_in_block(options, block_rect):
        y_offset = block_rect.top + block_rect.height // 2  # Начальное смещение по вертикали
        for i, option in enumerate(options):
            option_text = FONT.render(option, True, WHITE)
            option_rect = option_text.get_rect(center=(block_rect.centerx, y_offset + i * 50))
            SCREEN.blit(option_text, option_rect)
            pygame.draw.rect(SCREEN, WHITE, option_rect, 2)

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
                    SCREEN.fill(BLACK)
                    draw_text_in_block(selected_questions[current_question_index]["question"], pygame.Rect(500, 100, 700, 450))
                    draw_options_in_block(selected_questions[current_question_index]["options"], pygame.Rect(500, 100, 700, 450))

        SCREEN.blit(uni_img2, (0,0))

        if current_question_index < len(selected_questions):
            draw_text_in_block(selected_questions[current_question_index]["question"], pygame.Rect(500, 100, 700, 450))
            draw_options_in_block(selected_questions[current_question_index]["options"], pygame.Rect(500, 100, 700, 450))
        else:
            running = False
            pygame.time.wait(1000)
            return score

        pygame.display.flip()

    score_text = FONT.render(f"Your score: {score}", True, WHITE)
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    SCREEN.blit(score_text, score_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    run_quiz_game()
