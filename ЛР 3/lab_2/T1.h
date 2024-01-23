#ifndef T1_H
#define T1_H

#include <string>
#include <iostream>

class T1 {
private:
    std::string identifier;
    std::string value;

public:
    T1(const std::string& id, const std::string& val);
    void showValue() const;
    T1 operator-(const T1& other) const;
    friend std::ostream& operator<<(std::ostream& os, const T1& t1);
};

#endif // T1_H
