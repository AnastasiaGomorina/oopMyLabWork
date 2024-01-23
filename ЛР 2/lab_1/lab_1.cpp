#include <iostream>
#include <locale>

class ComplexNumber {
private:
    double real;
    double imaginary;

public:
    // Конструктор комплексного числа по умолчанию
    ComplexNumber() : real(0.0), imaginary(0.0) {}

    // Конструктор комплексного числа с параметрами
    ComplexNumber(double r, double i) : real(r), imaginary(i) {}

    // Метод для сложения
    ComplexNumber add(const ComplexNumber& other) const {
        return ComplexNumber(real + other.real, imaginary + other.imaginary);
    }

    // Метод для вычитания
    ComplexNumber subtract(const ComplexNumber& other) const {
        return ComplexNumber(real - other.real, imaginary - other.imaginary);
    }

    // Метод для умножения
    ComplexNumber multiply(const ComplexNumber& other) const {
        double resultReal = real * other.real - imaginary * other.imaginary;
        double resultImaginary = real * other.imaginary + imaginary * other.real;
        return ComplexNumber(resultReal, resultImaginary);
    }

    // Метод для вывода
    void display() const {
        std::cout << real << " + " << imaginary << "i" << std::endl;
    }
};

int main() {
    setlocale(LC_ALL, "Russian");
    
    ComplexNumber num1(2.0, 3.0);
    ComplexNumber num2(1.0, -1.0);

    int choice;
    do {
        std::cout << "Выберите операцию:\n";
        std::cout << "1. Сложение\n";
        std::cout << "2. Вычитание\n";
        std::cout << "3. Умножение\n";
        std::cout << "4. Выход\n";
        std::cin >> choice;

        switch (choice) {
        case 1:
            (num1.add(num2)).display();
            break;
        case 2:
            (num1.subtract(num2)).display();
            break;
        case 3:
            (num1.multiply(num2)).display();
            break;
        case 4:
            std::cout << "Программа завершена.\n";
            break;
        default:
            std::cout << "Неверный выбор.\n";
        }
    } while (choice != 4);

    return 0;
}