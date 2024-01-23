#include "T1.h"
#include <iostream>

T1::T1(const std::string& id, const std::string& val) : identifier(id), value(val) {}

void T1::showValue() const {
    std::cout << "T1 " << identifier << ": " << value << std::endl;
}

T1 T1::operator-(const T1& other) const {
    size_t found = value.find(other.value);
    if (found != std::string::npos) {
        return T1(identifier, value.substr(0, found) + value.substr(found + other.value.length()));
    }
    else {
        return *this;
    }
}

std::ostream& operator<<(std::ostream& os, const T1& t1) {
    os << "T1 " << t1.identifier << ": " << t1.value;
    return os;
}
