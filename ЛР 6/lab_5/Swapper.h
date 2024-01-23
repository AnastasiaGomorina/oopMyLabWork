#ifndef SWAPPER_H
#define SWAPPER_H

#include <sstream>
#include <vector>
#include <string>

inline std::string swapAdjacentWords(const std::string& sentence) {
    // –азбиваем предложение на слова
    std::istringstream iss(sentence);
    std::vector<std::string> words(std::istream_iterator<std::string>{iss},
        std::istream_iterator<std::string>());

    // ћен€ем местами каждые два соседних слова
    for (size_t i = 0; i < words.size() - 1; i += 2) {
        std::swap(words[i], words[i + 1]);
    }

    // —обираем обратно предложение из слов
    std::ostringstream oss;
    std::copy(words.begin(), words.end() - 1, std::ostream_iterator<std::string>(oss, " "));
    oss << words.back();

    return oss.str();
}

#endif // SWAPPER_H
