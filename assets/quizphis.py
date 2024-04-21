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
    uni_img2 = pygame.transform.scale(pygame.image.load("images/backgrounds/uniroom2.png"), (1700, 1465))
    questions = [
        {
            "question": "What is the SI unit of measurement for time?",
            "options": ["Seconds", "Meters", "Grams", "Volts"],
            "correct_answer": "Seconds"
        },
        {
            "question": "What is the force that attracts objects towards the center of the Earth?",
            "options": ["Gravity", "Friction", "Magnetism", "Inertia"],
            "correct_answer": "Gravity"
        },
        {
            "question": "What is the speed of light in a vacuum?",
            "options": ["300,000 km/s", "150,000 km/s", "500,000 km/s",
                        "1,000,000 km/s"],
            "correct_answer": "300,000 km/s"
        },
        {
            "question": "What law states that for every action, there is an equal and opposite reaction?",
            "options": ["Newton's First Law", "Newton's Second Law",
                        "Newton's Third Law", "Ohm's Law"],
            "correct_answer": "Newton's Third Law"
        },
        {
            "question": "What is the process by which water changes from a liquid to a gas?",
            "options": ["Condensation", "Evaporation", "Melting", "Freezing"],
            "correct_answer": "Evaporation"
        },
        {
            "question": "What is the measure of the amount of matter in an object?",
            "options": ["Volume", "Density", "Weight", "Mass"],
            "correct_answer": "Mass"
        },
        {
            "question": "What type of energy is associated with the motion of an object?",
            "options": ["Potential Energy", "Kinetic Energy", "Thermal Energy",
                        "Chemical Energy"],
            "correct_answer": "Kinetic Energy"
        },
        {
            "question": "What is the formula for calculating speed?",
            "options": ["s = vt", "s = vt + 1/2at^2", "s = (v + u)/2",
                        "s = d/t"],
            "correct_answer": "s = d/t"
        },
        {
            "question": "What is the process by which a solid turns directly into a gas without passing through the liquid phase?",
            "options": ["Sublimation", "Condensation", "Evaporation",
                        "Melting"],
            "correct_answer": "Sublimation"
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
