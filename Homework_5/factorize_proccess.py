from time import time
from multiprocessing import Pool


def factorize(*numbers) -> list:
    try:
        dividers = [[divider for divider in range(1, num + 1) if num % divider == 0] for num in numbers]
        return dividers
    except NotImplementedError:
        raise NotImplementedError()

    # ==============================2 variant=============================
    # try:
    #     for num in numbers:
    #         num_dividers = []
    #         for divider in range(1, num + 1):
    #             if num % divider == 0:
    #                 num_dividers.append(divider)
    #         dividers.append(num_dividers)
    #     return dividers
    # except NotImplementedError:
    #     raise NotImplementedError()


# ==========================================================================

if __name__ == '__main__':
    number_list = [128, 255, 99999, 10651060]

    pr_counter = 1

    while pr_counter < 5:
        start = time()
        with Pool(processes=pr_counter) as pool:
            pool.map_async(factorize, number_list)
        pr_counter += 1
        finish = time() - start
        print(finish)

    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
