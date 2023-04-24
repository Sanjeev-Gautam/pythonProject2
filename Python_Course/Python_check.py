# def return_last(*args):
#     result1 = args[-1]
#     print(result1)
#
# return_last([1,2,3,4,5],['a','b','c'],['mike','john'])

def key_list_items(key,**kwargs):
    value_list = kwargs[key]
    return value_list[-2]

print(key_list_items("things", things=['book','tv'], people=['pete','mike','jan','tom']))