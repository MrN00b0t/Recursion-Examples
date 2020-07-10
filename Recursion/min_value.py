def find_min(my_list):
  min = None
  if not my_list:
    return min
  current_list = my_list
  current_value = current_list.pop()
  check_value = find_min(current_list)
  if not check_value or current_value < check_value:
    return current_value
  else:
    return check_value



# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)
