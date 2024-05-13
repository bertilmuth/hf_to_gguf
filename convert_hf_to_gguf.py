import importlib.util
spec = importlib.util.spec_from_file_location("module.name", "./llama.cpp/convert-llama-ggml-to-gguf.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

from llmtuner.chat import ChatModel
from llmtuner.extras.misc import torch_gc
from huggingface_hub import snapshot_download

base_model_name="microsoft/Phi-3-mini-4k-instruct"
hf_model_id="bertilmuth/phi"

snapshot_download(repo_id=hf_model_id, local_dir="hf_model", revision="main")

module.main("hf_model --outfile model.gguf")
  

  


