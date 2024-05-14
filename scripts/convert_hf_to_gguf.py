import os, argparse, subprocess, shutil
from pathlib import Path
from huggingface_hub import snapshot_download

def main():
    # Process the command line arguments
    parser = argparse.ArgumentParser(description='Process a model ID for Hugging Face.')
    parser.add_argument('hf_model_id', type=str, help='The Hugging Face model ID')
    args = parser.parse_args()

    hf_model_id = args.hf_model_id
    
    # Download the model from Hugging Face
    local_hf_source_model_root_path = f"hf_models/{hf_model_id}"
    snapshot_download(repo_id=hf_model_id, local_dir=local_hf_source_model_root_path, revision="main")

    # Define variables & create GGUF model directory
    hf_model_name = extractModelName(hf_model_id)
    gguf_model_directory_path = f"gguf_models/{hf_model_id}"
    create_directory_if_not_exists(gguf_model_directory_path)

    # Convert the model to GGUF format, using llama.cpp
    gguf_model_path = f"{gguf_model_directory_path}/{hf_model_name}.gguf"
    converter = ["python", "scripts/llama.cpp/convert-hf-to-gguf.py", 
               "--outfile", gguf_model_path, "--outtype", "f16", local_hf_source_model_root_path]
    run(converter)
    
    # Automatically install 
    if directory_exists(gguf_model_directory_path):
      install_to_lmstudio(gguf_model_directory_path)

def extractModelName(hf_model_id):
    parts = hf_model_id.split('/', 1)
    if len(parts) > 1:
        return parts[1]
    else:
        raise ValueError("Invalid Hugging Face model id: " + hf_model_id)

def create_directory_if_not_exists(directory_path):
    if not directory_exists(directory_path):
        os.makedirs(directory_path)

def directory_exists(directory_path):
    return os.path.exists(directory_path)

def run(commandline_command):
    result = subprocess.run(commandline_command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    
def install_to_lmstudio(source_model_root_path):
    user_home_dir = Path.home()
    lmstudio_models_dir = user_home_dir / '.cache' / 'lm-studio' / 'models'
    
    if not directory_exists(lmstudio_models_dir):
      return

    source_dir = Path(source_model_root_path)
    
    shutil.copytree(source_dir, lmstudio_models_dir)
    print(f"All files from {source_model_root_path} have been copied to {lmstudio_models_dir}")


if __name__ == '__main__':
    main()
