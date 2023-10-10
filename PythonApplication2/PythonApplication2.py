import random

# ������ ������� � ����
events = [
    "�� ������������ � ������ �������. ��� ������ ������?",
    "�� ���������� ����� ���������. ���� �������?",
    "��� �������� ������������ ��������� �����. ������� �� ��� ���?"
]

# ������� � ���������� ������� �� �������
answers = {
    "1": ["����������� � �������", "���������� ������� �����", "�������� � ������"],
    "2": ["����� ������", "����� �������", "��������� �����"],
    "3": ["������� �����", "��������������� � ���� ������"]
}

# ��������� ��� ������������ ���������� �������
visited_locations = set()

# ������� ������ ������� � ��������� �������
def show_event(event_num):
    event = events[event_num - 1]
    print(event)
    options = answers[str(event_num)]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

# ������� ��� ��������� ���������� ������
def process_answer(event_num, answer_num):
    options = answers[str(event_num)]
    selected_option = options[answer_num - 1]
    print(f"�� �������: {selected_option}")
    # ����� ����� �������� ������ ��� ������ ��������� �������

# �������� ������� ����
while True:
    # �������� ��������� �������, ������� ��� �� ��������
    event_num = random.randint(1, len(events))
    while event_num in visited_locations:
        event_num = random.randint(1, len(events))
    visited_locations.add(event_num)
    
    show_event(event_num)
    
    # �������� ��������� ����� �� ������
    answer_num = int(input("������� ����� ���������� ��������: "))
    
    process_answer(event_num, answer_num)
    
    # ��������� ���� ��� ���������� ������������� ���������� �������
    if len(visited_locations) >= 3:
        print("�� ������ ����.")
        break
