import time
from multiprocessing import cpu_count, current_process
import concurrent.futures


def factorize(*number):
    result = []
    print(f'Process {current_process().name} started')
    print(number)
    for num in number:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
        return factors


if __name__ == '__main__':
    print(cpu_count())
    start_time = time.time()
    # a, b, c, d, f, g, h = factorize(10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060)
    with concurrent.futures.ProcessPoolExecutor(max_workers=7) as executor:
        a, b, c, d, f, g, h = executor.map(factorize,
                                           (10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060))
        print(a)
    # замалі числа були для процесів, тому я взяв більші числа щоб побачити різницю в часі виконання
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Час виконання: {execution_time} секунд")
