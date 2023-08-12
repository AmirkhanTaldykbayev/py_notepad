import view
import model


notes = model.load_notes()

def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                model.print_notes(notes)
            case 2:
                model.add_note(notes)
                view.print_message("Заметка добавлена")
            case 3:
                model.edit_note(notes)
            case 4:
                model. delete_note(notes)
            case 5:
                view.print_message("До свидания!")
                break
        