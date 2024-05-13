from llmtuner.chat import ChatModel
from llmtuner.extras.misc import torch_gc
from huggingface_hub import snapshot_download
from scripts.llama_cpp import convert_hf_to_gguf
import argparse

base_model_name="microsoft/Phi-3-mini-4k-instruct"
hf_model_id="bertilmuth/phi"

# Download the model from Huggingface
snapshot_download(repo_id=hf_model_id, local_dir="hf_model", revision="main")

# Convert the model to GGUF format, 
# using an adapted version of convert-hf-to-gguf.py (of llama.cpp)
convert_hf_to_gguf.convert_model("hf_model", "model.gguf")
  

  


