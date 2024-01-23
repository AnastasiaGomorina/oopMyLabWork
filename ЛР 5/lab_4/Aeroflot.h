#ifndef AEROFLOT_H
#define AEROFLOT_H

#include <iostream>
#include <string>

class AEROFLOT {
private:
    std::string destination;
    int flightNumber;
    std::string aircraftType;

public:
    // Конструктор по умолчанию
    AEROFLOT() : flightNumber(0) {}

    // Конструктор класса
    AEROFLOT(std::string dest, int number, std::string type) : destination(dest), flightNumber(number), aircraftType(type) {}

    // Методы доступа
    std::string getDestination() const {
        return destination;
    }

    int getFlightNumber() const {
        return flightNumber;
    }

    void setFlightNumber(int number) {
        flightNumber = number;
    }

    std::string getAircraftType() const {
        return aircraftType;
    }

    void setInputValues() {
        std::cout << "Введите пункт назначения: ";
        std::cin >> destination;
        std::cout << "Введите номер рейса: ";
        std::cin >> flightNumber;
        std::cout << "Введите тип самолета: ";
        std::cin >> aircraftType;
    }
};

// Перегруженные операции извлечения и вставки
std::ostream& operator<<(std::ostream& os, const AEROFLOT& aeroflot);

std::istream& operator>>(std::istream& is, AEROFLOT& aeroflot);

#endif 
