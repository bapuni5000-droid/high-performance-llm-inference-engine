# High-performance LLM inference engine

C++17 code for experimenting with the pieces that sit underneath an inference runtime.

This is not a replacement for llama.cpp or a production transformer runtime. There are no
model weights in this repository. The useful part here is the structure: a tokenizer boundary,
a small tensor representation, parallel matrix/vector work, and a place to add real model
operators.

## Build

You need CMake and a C++17 compiler.

```bash
cmake -S . -B build
cmake --build build --config Release
```

Run the demo:

```bash
./build/rfg_llm_demo
```

On Visual Studio, run the generated executable from the Release directory.

## What's here

`include/engine.hpp` contains the public interface. The implementation is in `src/`.

The current demo uses deterministic token IDs and a simple generated output. That is intentional:
real model loading, tokenizer vocabularies, quantized kernels and transformer layers can be
added without changing the basic interface.

## Project layout

- `include/` public C++ interfaces
- `src/` inference/runtime demo
- `python/` Python interoperability notes
- `ui/` desktop runtime panel

## Desktop UI

```bash
python ui/app.py
```

The UI is intentionally a front end for the demo runtime. The C++ interface is
kept separate so a pybind11 bridge or local RPC layer can be added later.

## C++ build

```bash
cmake -S . -B build
cmake --build build --config Release
```
