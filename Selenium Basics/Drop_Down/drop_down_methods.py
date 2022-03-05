from selenium.webdriver.support.ui import Select


def drop_down(drop_down_name, value):
    selected_drop_down = Select(drop_down_name)
    selected_drop_down.select_by_visible_text(value)


def show_all_drop_down_items(drop_down_name):
    selected_drop_down = Select(drop_down_name)
    values = selected_drop_down.options

    for item in values:
        print(item.text)


def stop_after_specific_value(drop_down_name, value):
    selected_drop_down = Select(drop_down_name)
    values = selected_drop_down.options
    for item in values:
        print(item.text)
        if item.text == value:
            break


def without_using_select(drop_down_name):
    for item in drop_down_name:
        print(item.text)
