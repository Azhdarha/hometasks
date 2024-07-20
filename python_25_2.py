from multiprocessing import Pool
import time

# Функция, которая будет применена к каждому элементу
def square(n):
    return n * n

if __name__ == '__main__':
    # Создание пула из 4 процессов
    with Pool(processes=4) as pool:
        # Входной список значений
        values = [1, 2, 3, 4, 5]
        # Применение функции square к каждому элементу в списке параллельно
        results = pool.map(square, values)
        print(results)




start_time = time.time()
end_time = time.time()

elapsed_time = end_time - start_time

print(f"The task took {elapsed_time:.2f} seconds to complete.")

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))