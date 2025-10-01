from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def CalcularSalarioMensual(self):
        pass

    def __str__(self):
        return f"Nombre: {self.nombre}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salario_anual: float):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def CalcularSalarioMensual(self):
        return self.salario_anual / 12

    def __str__(self):
        return f"{super().__str__()}, Salario Anual: {self.salario_anual}, Salario Mensual: {self.CalcularSalarioMensual():.2f}"

class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre: str, horas_trabajadas: float, tarifa_por_hora: float):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def CalcularSalarioMensual(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def __str__(self):
        return f"{super().__str__()}, Horas: {self.horas_trabajadas}, Tarifa: {self.tarifa_por_hora}, Salario Mensual: {self.CalcularSalarioMensual():.2f}"

empleados = []

print("Ingrese 3 empleados a tiempo completo:")
for i in range(3):
    nombre = input(f"Empleado #{i+1} Nombre: ")
    salario_anual = float(input("Salario anual: "))
    empleados.append(EmpleadoTiempoCompleto(nombre, salario_anual))

print("2 empleados a tiempo horario:")
for i in range(2):
    nombre = input(f"Empleado {i+1} Nombre: ")
    horas = float(input("Horas trabajadas: "))
    tarifa = float(input("Tarifa por hora: "))
    empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))

print("Información de empleados")
for emp in empleados:
    print(f"{emp.nombre}-Salario mensual: {emp.CalcularSalarioMensual():.2f}")
