#ifndef FLIGHT_REQUEST_H
#define FLIGHT_REQUEST_H

#include <string>

class FlightRequest {
public:
    std::string destination;
    int flightNumber;
    std::string passengerName;
    std::string departureDate;

    FlightRequest(const std::string& dest, int flightNum, const std::string& name, const std::string& date)
        : destination(dest), flightNumber(flightNum), passengerName(name), departureDate(date) {}
};

#endif
