#include <iostream>
#include "StackList.h"
#include <Windows.h>

int main() {
    SetConsoleOutputCP(1251);
    try {
        // Пример с типом int
        Stack<int> intStack;
        intStack.push(1);
        intStack.push(2);
        int topIntValue = intStack.getTop();
        std::cout << "Извлечено из intStack: " << topIntValue << std::endl;

        // Пример с типом double
        Stack<double> doubleStack;
        doubleStack.push(3.57);
        doubleStack.push(4.62);
        double topDoubleValue = doubleStack.getTop();
        std::cout << "Извлечено из doubleStack: " << topDoubleValue << std::endl;

        // Пример с типом std::string
        Stack<std::string> stringStack;
        //stringStack.push("Кот");
        //stringStack.push("Дождь");
        std::string topStringValue = stringStack.getTop();
        std::cout << "Извлечено из stringStack: " << topStringValue << std::endl;

    }
    catch (const std::exception& e) {
        std::cerr << "Исключение: " << e.what() << std::endl;
    }

    return 0;
}
