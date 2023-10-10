import random

# Список событий в игре
events = [
    "Вы просыпаетесь в темной комнате. Что будете делать?",
    "Вы находитесь перед развилкой. Куда пойдете?",
    "Ваш персонаж обнаруживает секретную дверь. Открыть ее или нет?"
]

# Словарь с вариантами ответов на события
answers = {
    "1": ["Осмотреться в комнате", "Попытаться разбить дверь", "Крикнуть о помощи"],
    "2": ["Пойти налево", "Пойти направо", "Вернуться назад"],
    "3": ["Открыть дверь", "Проигнорировать и идти дальше"]
}

# Множество для отслеживания посещенных локаций
visited_locations = set()

# Функция вывода события и вариантов ответов
def show_event(event_num):
    event = events[event_num - 1]
    print(event)
    options = answers[str(event_num)]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

# Функция для обработки выбранного ответа
def process_answer(event_num, answer_num):
    options = answers[str(event_num)]
    selected_option = options[answer_num - 1]
    print(f"Вы выбрали: {selected_option}")
    # Здесь можно добавить логику для разных вариантов ответов

# Основной игровой цикл
while True:
    # Выбираем случайное событие, которое еще не посещали
    event_num = random.randint(1, len(events))
    while event_num in visited_locations:
        event_num = random.randint(1, len(events))
    visited_locations.add(event_num)
    
    show_event(event_num)
    
    # Получаем выбранный ответ от игрока
    answer_num = int(input("Введите номер выбранного варианта: "))
    
    process_answer(event_num, answer_num)
    
    # Завершаем игру при достижении определенного количества событий
    if len(visited_locations) >= 3:
        print("Вы прошли игру.")
        break
