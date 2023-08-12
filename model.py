import json
import datetime
import view

def load_notes():
    try:
        with open('notes.json') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

def print_notes(notes):
    if len(notes) == 0:
        view.print_message("Нет заметок")
    else:
        for note in notes:
            print("ID:", note['id'])
            print("Заголовок:", note['title'])
            print("Тело заметки:", note['body'])
            print("Дата/время создания:", note['created_at'])
            print("Дата/время последнего изменения:", note['updated_at'])
            print()

def add_note(notes):
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = str(datetime.datetime.now())
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'created_at': timestamp,
        'updated_at': timestamp
    }
    notes.append(note)
    save_notes(notes)
    

def edit_note(notes):
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новое тело заметки: ")
            note['updated_at'] = str(datetime.datetime.now())
            save_notes(notes)
            view.print_message("Заметка отредактирована")
            return
    view.print_message("Заметка с таким ID не найдена")

def delete_note(notes):
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            view.print_message("Заметка удалена")
            return
    view.print_message("Заметка с таким ID не найдена")


