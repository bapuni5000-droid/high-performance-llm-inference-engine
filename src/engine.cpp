#include "engine.hpp"
#include <algorithm>
#include <future>
#include <sstream>
namespace llm {
std::vector<int> Tokenizer::encode(const std::string& text) const {
  std::vector<int> ids; std::istringstream in(text); std::string w;
  while(in>>w){int h=0;for(unsigned char c:w)h=(h*31+c)%50000;ids.push_back(h);}
  return ids;
}
Engine::Engine(unsigned threads):threads_(threads?threads:std::max(1u,std::thread::hardware_concurrency())){}
std::vector<float> Engine::matvec(const std::vector<float>& A,const std::vector<float>& x,unsigned rows,unsigned cols) const {
  if(A.size()!=size_t(rows)*cols||x.size()!=cols) throw std::invalid_argument("matrix/vector dimensions mismatch");
  std::vector<float> y(rows); std::vector<std::future<void>> jobs;
  unsigned workers=std::min(threads_,rows);
  for(unsigned t=0;t<workers;t++) jobs.push_back(std::async(std::launch::async,[&,t]{for(unsigned r=t;r<rows;r+=workers){float s=0;for(unsigned c=0;c<cols;c++)s+=A[r*cols+c]*x[c];y[r]=s;}}));
  for(auto& j:jobs)j.get(); return y;
}
std::string Engine::generate(const std::string& prompt,unsigned max_tokens) const {
  auto ids=Tokenizer{}.encode(prompt); std::ostringstream out; out<<prompt;
  for(unsigned i=0;i<max_tokens;i++) out<<" ["<<((ids.empty()?0:ids[i%ids.size()])+i)%50000<<"]";
  return out.str();
}
}
