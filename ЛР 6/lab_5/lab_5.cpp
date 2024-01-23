#include <iostream>
#include <fstream>
#include <chrono>
#include <sstream>
#include "Swapper.h"
#include <Windows.h>
#include "Test.h"


int main() {
    SetConsoleOutputCP(1251);

    std::string filename = "input.txt";

    // Открываем файл для чтения
    std::ifstream inputFile(filename);

    // Проверяем, удалось ли открыть файл
    if (!inputFile.is_open()) {
        std::cerr << "Не удалось открыть файл." << std::endl;
        return 1; // Возвращаем код ошибки
    }

    // Читаем текст из файла в строку
    std::stringstream buffer;
    buffer << inputFile.rdbuf();
    std::string text = buffer.str();

    // Закрываем файл
    inputFile.close();

    // Применяем функцию swapAdjacentWords к тексту
    std::string modifiedText = swapAdjacentWords(text);

    // Выводим результат на экран
    std::cout << "Исходный текст:\n" << text << "\n\n";
    std::cout << "Модифицированный текст (соседние слова поменяны):\n" << modifiedText << std::endl;

    return 0;
}