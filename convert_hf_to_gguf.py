from huggingface_hub import snapshot_download
import subprocess

base_model_name="microsoft/Phi-3-mini-4k-instruct"
hf_model_name = "phi"
hf_model_id="bertilmuth/phi"

# Download the model from Huggingface
snapshot_download(repo_id=hf_model_id, local_dir=hf_model_name, revision="main")

# Convert the model to GGUF format, 
# using an adapted version of convert-hf-to-gguf.py (of llama.cpp)
script_path = "scripts/llama.cpp/convert-hf-to-gguf.py"
command = ["python", script_path, "--outfile", f"{hf_model_name}.gguf", "--outtype", "f16", hf_model_name]
  
result = subprocess.run(command, capture_output=True, text=True)

# Print the output of the script
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return code:", result.returncode)
  


