@echo off

if "%~1"=="" (
    echo Usage: %0 huggingface_model_id
    exit /b 1
)

set "HF_MODEL_ID=%~1"

:: Perform setup if necessary
call ./scripts/setup.bat

:: Activate the conda environment for all the Python libraries
call conda activate __convert_hf_to_gguf__

:: Verify the activation
if "%CONDA_DEFAULT_ENV%"=="__convert_hf_to_gguf__" (
    echo INFO: Conda environment activated.
) else (
    echo ERROR: Failed to activate conda environment.
    exit /b 1
)

:: Do the conversion from Hugging Face model to GGUF
call python ./scripts/convert_hf_to_gguf.py "%HF_MODEL_ID%"