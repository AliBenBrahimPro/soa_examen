import time
from monothread import run_monothread
from multiprocess import run_multiprocess
from multithread import run_multithread
from synchronization import run_synchronization

if __name__ == "__main__":
    print("Running monothread version...")
    start_time = time.time()
    run_monothread()
    print(f"Execution Time (Monothread): {time.time() - start_time:.4f} seconds\n")

    print("Running multiprocessing version...")
    start_time = time.time()
    run_multiprocess()
    print(f"Execution Time (Multiprocess): {time.time() - start_time:.4f} seconds\n")

    print("Running multithread version...")
    start_time = time.time()
    run_multithread()
    print(f"Execution Time (Multithread): {time.time() - start_time:.4f} seconds\n")

    print("Running synchronization example...")
    run_synchronization()
