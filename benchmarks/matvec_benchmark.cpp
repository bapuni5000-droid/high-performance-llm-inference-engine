#include "engine.hpp"
#include <chrono>
#include <iostream>
#include <vector>

int main() {
    constexpr unsigned rows = 512;
    constexpr unsigned cols = 512;
    std::vector<float> matrix(rows * cols, 0.001f);
    std::vector<float> input(cols, 1.0f);

    llm::Engine engine;
    auto start = std::chrono::steady_clock::now();
    auto output = engine.matvec(matrix, input, rows, cols);
    auto end = std::chrono::steady_clock::now();

    double ms = std::chrono::duration<double, std::milli>(end - start).count();
    std::cout << "matvec: " << rows << "x" << cols << ", " << ms << " ms\n";
    std::cout << "first value: " << output.front() << "\n";
    return 0;
}
