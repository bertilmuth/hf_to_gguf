def extractModelName(hf_model_id):
    parts = hf_model_id.split('/', 1)
    if len(parts) > 1:
        return parts[1]
    else:
        raise ValueError("Invalid huggingface model id: " + hf_model_id)

from huggingface_hub import snapshot_download
import subprocess

hf_model_id="bertilmuth/phi"

# Download the model from Huggingface
local_hf_model_path = f"hf_models/{hf_model_id}"
snapshot_download(repo_id=hf_model_id, local_dir=local_hf_model_path, revision="main")

# Convert the model to GGUF format, 
# using an adapted version of convert-hf-to-gguf.py (of llama.cpp)
script_path = "scripts/llama.cpp/convert-hf-to-gguf.py"
hf_model_name = extractModelName(hf_model_id)
local_gguf_model_path = f"gguf_models/{hf_model_id}/{hf_model_name}.gguf"
command = ["python", script_path, "--outfile", f"{hf_model_name}.gguf", "--outtype", "f16", local_hf_model_path]
  
result = subprocess.run(command, capture_output=True, text=True)

# Print the output of the script
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return code:", result.returncode)


  


