#include <v8.h>
#include <node.h>

using namespace v8;
using namespace node;

namespace nodexpdf {
  void Init (Handle<Object> target){
  }
}

NODE_MODULE(bindings, nodexpdf::Init);

