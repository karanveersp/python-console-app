# Python Console Apps

This project is an example of how to create an executable python package which can be installed by `pip` and run on the terminal like any regular command.

1. Initialize the package using `Poetry`

   ```
   poetry new my-python-app
   ```

   This creates new python package ready to be developed.

   ```
   my_python_app/
   	__init__.py
   tests
   	__init__.py
   	test_my_python_app.py
   pyproject.toml
   README.rst
   ```

2. Update the pytest version and add black

   ```toml
   [tool.poetry.dependencies]
   python = "^3.10"

   [tool.poetry.dev-dependencies]
   pytest = "*"
   black = {version = "^21.10b0", allow-prereleases = true}
   ```

3. Add a module `util.py` inside the package with the following content. This util file can contain useful functions used within the package that can be utilized by other scripts importing this package.

   ```py
   """Contains a collection of useful functions"""


   def utilfunc():
   	"""Provides utility"""
   	print("Providing utility!")

   ```

4. Add a module called `main` inside the package, with a `main` function.

   ```py
   from . import util


   def main():
   	util.utilfunc()
   	print("Running your python app!")


   if __name__ == "__main__":
   	main()
   ```

5. Update `__init__.py`

   ```py
   from . import util

   __version__ = "0.1.0"
   ```

6. Add the `tool.poetry.scripts` section in `pyproject.toml`

   ```
   [tool.poetry.scripts]
   mypythonapp = "my_python_app.main:main"
   ```

   This specifies what the cli command will be and which function will be invoked within the package. Follow the convention `package.module:func`

7. Install and test the command within the poetry shell

   ```sh
   poetry shell
   poetry install
   mypythonapp
   > Providing utility!
   > Running your python app!
   ```

8. To install for external python environments, first build the project, then install using `pip`.

   ```sh
   poetry build
   (deactivate or exit venv)
   pip install dist\my_python_app-0.1.0-py3-none-any.whl
   mypythonapp
   > Proviting utility!
   > Running your python app!
   ```

9. Re-install whenever the code is changed.
10. Uninstall the app using `pip uninstall my-python-app`.
