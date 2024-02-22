import psutil

def revisar_estado_aplicacion():
    # Obtener la lista de todos los procesos en ejecución
    for proc in psutil.process_iter():
        try:
            # Obtener información sobre cada proceso
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_percent'])
        except psutil.NoSuchProcess:
            pass
        else:
            # Filtrar los procesos que pertenecen a la aplicación 
            if "Code.exe" in pinfo['name']:
                print(f"PID: {pinfo['pid']}, Nombre: {pinfo['name']}, Usuario: {pinfo['username']}, %CPU: {pinfo['cpu_percent']}, %Memoria: {pinfo['memory_percent']}")

if __name__ == "__main__":
    revisar_estado_aplicacion()
