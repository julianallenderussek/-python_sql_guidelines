from dbhelpers import run_statement;

num_rooms = input("Please input the number of rooms of your dream home? ")
result = run_statement('call get_homes_by_num_rooms(?)', [num_rooms])
print(result)

search_value = input("Please input the address / city of dream home? ")
result = run_statement('call get_home_by_city(?)', [search_value])
print(result)