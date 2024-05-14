:: Run the script (in the current directory) 
:: to setup the conda environment if needed
call "%~dp0setup_conda.bat" __convert_hf_to_gguf__

:: Activate the environment
call conda activate __convert_hf_to_gguf__

:: Verify the activation
if "%CONDA_DEFAULT_ENV%"=="__convert_hf_to_gguf__" (
    echo INFO: Conda environment activated.
) else (
    echo ERROR: Failed to activate conda environment.
    exit /b 1
)

git clone https://github.com/ggerganov/llama.cpp scripts/llama.cpp >nul 2>&1
pip install -q -r scripts/llama.cpp/requirements.txt
pip install -q llmtuner

