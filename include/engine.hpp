#pragma once
#include <cstdint>
#include <string>
#include <vector>
namespace llm {
// Minimal container for a future quantized weight block.
struct QuantizedTensor { std::vector<int8_t> data; float scale=1.0f; };
class Tokenizer {
public: std::vector<int> encode(const std::string& text) const;
};
class Engine {
public:
  explicit Engine(unsigned threads=0);
  std::vector<float> matvec(const std::vector<float>& matrix,const std::vector<float>& vector,unsigned rows,unsigned cols) const;
  std::string generate(const std::string& prompt,unsigned max_tokens=32) const;
private: unsigned threads_;
};
}
