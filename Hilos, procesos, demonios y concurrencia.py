import threading
import multiprocessing
import concurrent.futures
import time
# Función para ejecutar en un hilo
def thread_function(name)
print(f'Hilo {name} iniciado.')
time.sleep(2)
print(f'Hilo {name} finalizado.')
# Función para ejecutar en un proceso
def process_function(name)
print(f'Proceso {name} iniciado.')
time.sleep(2)
print(f'Proceso {name} finalizado.')
if __name__ == __main__
# Crear un hilo
thread = threading.Thread(target=thread_function, args=('Hilo 1',))
thread.start()
# Crear un proceso
process = multiprocessing.Process(target=process_function,
args=('Proceso 1',))
process.start()
# Crear un demonio
daemon_thread = threading.Thread(target=thread_function, args=('Demonio
1',))
daemon_thread.daemon = True
daemon_thread.start()
# Utilizar concurrent.futures para concurrencia
with concurrent.futures.ThreadPoolExecutor() as executor
futures = []
for i in range(3)
futures.append(executor.submit(thread_function, f'Concurrencia

{i}'))
for future in concurrent.futures.as_completed(futures)
print(f'Concurrencia {future.result()} finalizada.')