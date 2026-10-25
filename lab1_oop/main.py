from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests

def main():
    N = 14

    rect = Rectangle(N, N, "синий")
    circle = Circle(N, "зелёный")
    square = Square(N, "красный")

    print(rect)
    print(circle)
    print(square)

    print("\n Проверка внешнего пакета")
    print(f"Версия установленного пакета requests: {requests.__version__}")
if __name__ == "__main__":

    main()
