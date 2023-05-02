def check(string_check, str_dic):
    for x in str_dic:
        if str_dic[x] == string_check:
            return True
    return False


dic ={"name":"Rajesh","roll":"108","sec":"2B","college":"JIS"}
while(1):
    n = input("Do you want to check string:(y/n)")
    if n == 'y':
        str = input("Enter string:")
        if check(str,dic) :
            print("Element is Present")
        else:
            print("Element is not present")
    else:
        break