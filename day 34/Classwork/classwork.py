def pop_elements(main_list, indexes_list):
    indexes_list= sorted(indexes_list, reverse=True)

    for index in indexes_list:
        if 0 <= index < len(main_list):
            main_list.pop(index)
