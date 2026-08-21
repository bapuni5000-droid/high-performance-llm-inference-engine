#include "engine.hpp"
#include <iostream>
int main(){llm::Engine engine; std::cout<<engine.generate("Hello from the C++ inference engine",12)<<"\n"; return 0;}
