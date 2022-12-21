import logger
import view
import model


def show_main_menu():
    while True:
        menu_num = view.start()

        if menu_num == '1':  # показ работников
            result = logger.view_all_employee()
            view.print_message(result)
        elif menu_num == '2':  # добавление новых работников
            model.enter_employee_record()
        elif menu_num == '3':  # поиск работников
            data = view.insert_data('Поиск работника: ')
            result3 = model.search_employee_record(data)
            view.print_message(result3)
        elif menu_num == '4':  # удаление работников
            data = view.insert_data('Поиск работника, для удаления: ')
            model.delete_employee(data)
        elif menu_num == '5':  # выход из программы
            break

        else:
            print("Ошибка, Введите [1 до 4]\n")