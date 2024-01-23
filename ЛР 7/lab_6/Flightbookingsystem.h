#ifndef FLIGHT_BOOKING_SYSTEM_H
#define FLIGHT_BOOKING_SYSTEM_H

#include "Flightrequest.h"
#include <list>

class FlightBookingSystem {
private:
    std::list<FlightRequest> requests;

public:
    void addRequest(const FlightRequest& request) {
        requests.push_back(request);
        std::cout << "Заявка успешно добавлена.\n";
    }

    void removeRequest(int flightNumber, const std::string& departureDate) {
        requests.remove_if([&](const FlightRequest& request) {
            return (request.flightNumber == flightNumber && request.departureDate == departureDate);
            });
        std::cout << "Заявки успешно удалены.\n";
    }

    void printRequestsByFlightAndDate(int flightNumber, const std::string& departureDate) {
        for (const auto& request : requests) {
            if (request.flightNumber == flightNumber && request.departureDate == departureDate) {
                std::cout << "Пункт назначения: " << request.destination << "\n";
                std::cout << "Номер рейса: " << request.flightNumber << "\n";
                std::cout << "Фамилия и инициалы пассажира: " << request.passengerName << "\n";
                std::cout << "Желаемая дата вылета: " << request.departureDate << "\n\n";
            }
        }
    }

    void printAllRequests() {
        for (const auto& request : requests) {
            std::cout << "Пункт назначения: " << request.destination << "\n";
            std::cout << "Номер рейса: " << request.flightNumber << "\n";
            std::cout << "Фамилия и инициалы пассажира: " << request.passengerName << "\n";
            std::cout << "Желаемая дата вылета: " << request.departureDate << "\n\n";
        }
    }
};

#endif
