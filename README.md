## Prepare
Clone this repository.
If you haven't done so already, 
[install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
and [conda](https://docs.anaconda.com/free/miniconda/miniconda-install/).

## Convert a Hugging Face model to a GGUF model
1. Start a conda shell (in Windows: click on the Windows symbol, start typing anaconda).
2. Change to the installation directory.
3. Type `./convert <huggingface_model_id>`

NOTE: Replace <huggingface_model_id> by your actual model identifier on Hugging Face.
The converter saves the GGUF in the `gguf_models` subfolder. 


