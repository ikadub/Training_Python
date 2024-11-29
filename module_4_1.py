from fake_math import divide as f_m
from true_math import divide as t_d

if __name__ == "__main__":
    result1 = f_m(69, 3)
    result2 = f_m(3, 0)
    result3 = t_d(49, 7)
    result4 = t_d(15, 0)

    print(result1)
    print(result2)
    print(result3)
    print(result4)