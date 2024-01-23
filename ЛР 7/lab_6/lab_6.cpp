#include <iostream>
#include "Flightbookingsystem.h"
#include <Windows.h>

int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    FlightBookingSystem bookingSystem;
    int choice;

    do {
        std::cout << "Меню:\n";
        std::cout << "1. Добавить заявку\n";
        std::cout << "2. Удалить заявку\n";
        std::cout << "3. Вывести заявки по номеру рейса и дате вылета\n";
        std::cout << "4. Вывести все заявки\n";
        std::cout << "0. Выйти из программы\n";
        std::cout << "Выберите действие: ";
        std::cin >> choice;

        switch (choice) {
        case 1: {
            std::string dest, name, date;
            int flightNum;
            std::cout << "Введите пункт назначения: ";
            std::cin >> dest;
            std::cout << "Введите номер рейса: ";
            std::cin >> flightNum;
            std::cout << "Введите фамилию пассажира: ";
            std::cin >> name;
            std::cout << "Введите инициалы пассажира: ";
            std::string initials;
            std::cin >> initials;
            name += " " + initials;
            std::cout << "Введите желаемую дату вылета: ";
            std::cin >> date;
            FlightRequest newRequest(dest, flightNum, name, date);
            bookingSystem.addRequest(newRequest);
            break;
        }
        case 2: {
            int flightNum;
            std::string date;
            std::cout << "Введите номер рейса для удаления: ";
            std::cin >> flightNum;
            std::cout << "Введите дату вылета для удаления: ";
            std::cin >> date;
            bookingSystem.removeRequest(flightNum, date);
            break;
        }
        case 3: {
            int flightNum;
            std::string date;
            std::cout << "Введите номер рейса для вывода заявок: ";
            std::cin >> flightNum;
            std::cout << "Введите дату вылета для вывода заявок: ";
            std::cin >> date;
            bookingSystem.printRequestsByFlightAndDate(flightNum, date);
            break;
        }
        case 4:
            bookingSystem.printAllRequests();
            break;
        case 0:
            std::cout << "Программа завершена.\n";
            break;
        default:
            std::cout << "Неверный выбор. Пожалуйста, выберите действие из меню.\n";
            break;
        }

    } while (choice != 0);

    return 0;
}