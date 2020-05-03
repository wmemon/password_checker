from password_check import get_password,get_result,in_result
hash_list = get_password()
print(in_result(get_result(hash_list[0]),hash_list[1]))