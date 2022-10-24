# Virtual Env
* `conda create --name your_env_name python=3.8`
    * `conda activate your_env_name`
    * `conda deactivate`

## Save all packages name in requirements.txt file
* `pip freeze > requirements.txt`    
* `pip3 install -r requirements.txt`

## Pycaret
### Regression
This function initializes the training environment and creates the transformation pipeline. Setup function must be called before executing any other function. It takes two mandatory parameters: data and target. All the other parameters are optional.
```
from pycaret.datasets import get_data
data = get_data('insurance')
```