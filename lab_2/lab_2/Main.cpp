#include "T1.h"
#include "T2.h"
#include "Factory.h"
#include <iostream>
#include <locale>
#include <windows.h>


void displayMenu() {
    std::cout << "Меню:\n";
    std::cout << "1. Создать и показать объекты T1\n";
    std::cout << "2. Создать и показать объекты T2\n";
    std::cout << "3. Вычесть объекты T1\n";
    std::cout << "4. Вычесть объекты T2\n";
    std::cout << "5. Выход\n";
}

int main() {
    SetConsoleOutputCP(1251);
    int choice;
    do {
        displayMenu();
        std::cout << "Введите ваш выбор: ";
        std::cin >> choice;

        switch (choice) {
        case 1: {
            std::string str1, str2;
            std::cout << "Введите строку для T1 объекта 1: ";
            std::cin.ignore(); // Очистка буфера ввода
            std::getline(std::cin, str1);


            T1 t1Obj1 = Factory::createT1("str1", str1);

            t1Obj1.showValue();
            break;
        }
        case 2: {
            std::string oct1, oct2;
            int octValue1, octValue2;

            std::cout << "Введите строку для T2 объекта 1 (восьмеричное число): ";
            std::cin >> oct1;



            try {
                octValue1 = std::stoi(oct1, nullptr, 8);
            }
            catch (std::invalid_argument&) {
                std::cerr << "Ошибка: введите корректное восьмеричное число.\n";
                continue;
            }

            T2 t2Obj1 = Factory::createT2("oct1", octValue1);

            t2Obj1.showValue();
            break;
        }
        case 3: {
            std::string str1, str2;
            std::cout << "Введите строку для T1 объекта 1: ";
            std::cin.ignore(); // Очистка буфера ввода
            std::getline(std::cin, str1);

            std::cout << "Введите строку для T1 объекта 2: ";
            std::getline(std::cin, str2);

            T1 t1Obj1 = Factory::createT1("str1", str1);
            T1 t1Obj2 = Factory::createT1("str2", str2);

            t1Obj1.showValue();
            t1Obj2.showValue();

            T1 resultT1 = t1Obj1 - t1Obj2;
            std::cout << "Результат после вычитания: " << resultT1 << std::endl;
            Factory::deleteObject(&t1Obj1);
            break;
        }
        case 4: {
            std::string oct1, oct2;
            int octValue1, octValue2;

            std::cout << "Введите строку для T2 объекта 1 (восьмеричное число): ";
            std::cin >> oct1;

            std::cout << "Введите строку для T2 объекта 2 (восьмеричное число): ";
            std::cin >> oct2;

            try {
                octValue1 = std::stoi(oct1, nullptr, 8);
                octValue2 = std::stoi(oct2, nullptr, 8);
            }
            catch (std::invalid_argument&) {
                std::cerr << "Ошибка: введите корректное восьмеричное число.\n";
                continue;
            }

            T2 t2Obj1 = Factory::createT2("oct1", octValue1);
            T2 t2Obj2 = Factory::createT2("oct2", octValue2);

            t2Obj1.showValue();
            t2Obj2.showValue();

            T2 resultT2 = t2Obj1 - t2Obj2;
            std::cout << "Результат после вычитания: " << resultT2 << std::endl;
            Factory::deleteObject(&t2Obj1);
            break;
        }
        case 5:
            std::cout << "Выход из программы.\n";
            break;
        default:
            std::cout << "Неверный выбор. Пожалуйста, введите допустимую опцию.\n";
        }

    } while (choice != 5);

    return 0;
}