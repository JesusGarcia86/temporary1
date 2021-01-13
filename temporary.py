def iterate_dictionary(some_list):
  for curr_dict in some_list:
    display_str = ''
    for curr_key in curr_dict.keys():
      display_str += f"{curr_key} - {curr_dict[curr_key]}"
    # remove comma and extra space from display_str
    display_str = display_str[:len(display_str) - 2]
    print(display_str)

iterate_dictionary(students)