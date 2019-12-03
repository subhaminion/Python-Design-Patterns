from model import Person
import view


def show_all():
    perople_in_db = Person.get_all()
    return view.show_all_view(perople_in_db)


def start():
    view.start_view()
    entered_input = input()
    if entered_input == 'y':
        return show_all()
    else:
        return view.endView()


if __name__ == "__main__":
    start()
