calls = 0
def count_calls():
    global calls
    calls=calls+1

def string_info(string):
    a = len(string)
    b = string.upper()
    c = string.lower()
    m = (a , b, c)
    count_calls()
    print(m)
    return m

def is_contains(string , list_to_search):
    count_calls()
    a=0
    for i in range(len(list_to_search)):
        b = str(list_to_search[i]).lower()
        string= string.lower()
        if string == b :
            a=a+1
    if a > 0 :
        print(True)
        return True
    else:
        print(False)
        return False

string_info(string = "Anton")
is_contains(string = "Anton" , list_to_search = [5, 7 , "ANTON"])
string_info(string = "kristina")
is_contains(string = "kristina" , list_to_search = [5, 7, 'Anton',8, "KRISTINA"])
string_info(string = "MAX")
is_contains(string = "MAX" , list_to_search = [5, 7 , 'Anton'])
print(calls)
