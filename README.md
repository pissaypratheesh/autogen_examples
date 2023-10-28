# Generic steps to install

1. Create a new conda environment with Python 3.10:
   ```
   conda create -n autogen python=3.10
   ```

2. Activate the conda environment:
   ```
   conda activate autogen
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## To run the Autogen recipe example (to create a recipe for system design)

Run the following command:

```
python create_recipe.py
```
And then you can copy the recipe and paste(or leave it so if you don't want to change the existing recipe) in the `system_design_recipe.py` and run it like 
```
 python system_design_recipe.py --deisgn="netflix backend"
 ```
