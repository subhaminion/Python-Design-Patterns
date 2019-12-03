def show_all_view(user_list):
    print("In our db we %i users. Here ther are: " % len(user_list))
    for item in user_list:
        print(item.name())


def start_view():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')


def endView():
    print('Goodbye!')
