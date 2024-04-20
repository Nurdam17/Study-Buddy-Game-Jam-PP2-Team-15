import pygame
import sys
import random

def run_quiz_game():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Quiz Game")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    FONT = pygame.font.Font(None, 36)

    score = 0

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
            "options": ["s = vt", "s = vt + 1/2at^2", "s = (v + u)/2", "s = d/t"],
            "correct_answer": "s = d/t"
        },
        {
            "question": "What is the process by which a solid turns directly into a gas without passing through the liquid phase?",
            "options": ["Sublimation", "Condensation", "Evaporation", "Melting"],
            "correct_answer": "Sublimation"
        }
    ]

    selected_questions = random.sample(questions, 3)

    current_question_index = 0

    def draw_buttons():
        for i, option in enumerate(selected_questions[current_question_index]["options"]):
            button_text = FONT.render(f"{i + 1}. {option}", True, WHITE)
            button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))
            SCREEN.blit(button_text, button_rect)
            pygame.draw.rect(SCREEN, WHITE, button_rect, 2)
        pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, option in enumerate(selected_questions[current_question_index]["options"]):
                    button_rect = FONT.render(f"{i + 1}. {option}", True, WHITE).get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))
                    if button_rect.collidepoint(event.pos):
                        if option == selected_questions[current_question_index]["correct_answer"]:
                            score += 1
                        current_question_index += 1
                        if current_question_index >= len(selected_questions):
                            running = False
                        else:
                            SCREEN.fill(BLACK)
                            draw_buttons()

        SCREEN.fill(BLACK)

        if current_question_index < len(selected_questions):
            question_text = FONT.render(selected_questions[current_question_index]["question"], True, WHITE)
            question_rect = question_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            SCREEN.blit(question_text, question_rect)
            draw_buttons()
        else:
            running = False

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
