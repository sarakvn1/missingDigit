# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def find_missing_digit(str_param):
    n_s = str_param.replace(" ", "")
    new_str = n_s.split("=")
    third = new_str[1]
    splitters = ["+", "-", "/", "*"]
    for i in splitters:
        new_new_str = new_str[0].split(i)
        if len(new_new_str) > 1:
            first = new_new_str[0]
            sec = new_new_str[1]
            splitter = i
        else:
            continue
    splitters_functionality = {"-": "+", "/": "*", "*": "/", "+": "-"}
    final_formula = None
    if third.find("x") > -1:
        final_formula = f"{first}{splitter}{sec}"
        r = eval(final_formula)
        f_r = third
    elif first.find("x") > -1:
        reverse_splitter = splitters_functionality.get(splitter)
        final_formula = f"{third}{reverse_splitter}{sec}"
        r = eval(final_formula)
        f_r = first
    elif sec.find("x") > -1:
        final_formula = f"{first}{splitter}{third}"
        r = eval(final_formula)
        f_r = sec

    r = [i for i in str(r)]
    f_r = [i for i in f_r]
    i = f_r.index('x')
    return r[i]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(find_missing_digit("3x * 2 = 64"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
