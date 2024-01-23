#include "AEROFLOT.h"
#include <algorithm>
#include <windows.h>


int main() {
    SetConsoleOutputCP(1251);
    const int arraySize = 7;
    AEROFLOT aeroflotArray[arraySize];

    // Ввод данных в массив и сортировка по пунктам назначения
    for (int i = 0; i < arraySize; ++i) {
        aeroflotArray[i].setInputValues();
    }

    std::sort(aeroflotArray, aeroflotArray + arraySize, [](const AEROFLOT& a, const AEROFLOT& b) {
        return a.getDestination() < b.getDestination();
        });

    // Вывод на экран пунктов назначения и номеров рейсов по введенному типу самолета
    std::string searchAircraftType;
    std::cout << "Введите тип самолета для поиска: ";
    std::cin >> searchAircraftType;

    bool found = false;
    for (const AEROFLOT& aeroflot : aeroflotArray) {
        if (aeroflot.getAircraftType() == searchAircraftType) {
            std::cout << "Пункт назначения: " << aeroflot.getDestination() << ", Номер рейса: " << aeroflot.getFlightNumber() << std::endl;
            found = true;
        }
    }

    // Вывод сообщения, если рейсов с введенным типом самолета нет
    if (!found) {
        std::cout << "Рейсов с указанным типом самолета не найдено." << std::endl;
    }

    return 0;
}
