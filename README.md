![ColorEx](res/header.png)

# Introduction

***ColorEx*** is a simple Python data visualization library for creating awesome and interactive heat maps. Heat maps are a great way for studying and learning patterns in data, and they use color extensively. This Python library aims to be simple, easy and straight-forward.

## Features

- **2-Dimensional** heat maps.
- **Styling** and **theming**.
- **Bi-color** heat maps supported.
- Input data supports **CSV** files.
- Output to **GUI, HTML**.
- Flexible data **formatting**, using Python format specifiers.
- **Interactive** heat map, cell (tile) selection with pop-up balloon.
- **Grouping** and **labeling** of tiles, or cells.




## Requirements

- Python 3.7+
- Cheetah - Version?
- Balloon.css (Embedded)



## Installation

### Install using pip (recommended)

To begin using the *ColorEx* library, we first install it using *pip*.

(NOTE: You'll need an Internet connection for this one.)

```shell
$ pip install colorexlib
```



## Let's Get Started

### Your first program!

Let's get started with your first python program using the *ColorEx* library.

1. Create a new directory on your computer.
2. **Copy and paste** the following **code** into a new file and save it as ***first_colorex.py***, in in your directory.

```python
# import modules 
from colorexlib.colorex import ColorExGrid

# set tile grid options
options = dict()
options['source'] = ['attendance.csv', 'csv']
options['title'] = 'Student Attendance'
options['subtitle'] = 'Attendance of students per month in 2018'
options['theme'] = 'sun.cxt'

# create ColorEx object, passing options.
colorex_grid = ColorExGrid(options)

# create color grid in HTML
colorex_grid.to_html('attendance.html','template.html')
```



3. In this repository, download the files ***attendance.csv*** and ***template.html*** in the *first_examples* directory and move them into the directory you created in step (1).

4. Now you should have **three files (3)** in the same directory: 

   1. *first_colorex.py*, 
   2. *attendance.csv* and 
   3. *template.html*. 

   Let's carry on!

5. Now open and **run** your python script ***first_colorex.py***.

6. If all things go smoothly, a new **HTML file** called ***attendance.html*** will be created in the same directory.
7. Open this new HTML file, and you will see a color grid quite similar to the one shown below: 

![Sample Output](res/sample_output.png)



Yayyy! So you've completed your first ever *ColorEx* script. Pretty simple right?!



### Examples

One of the best ways of learning how to use *ColorEx* is by looking at and studying a couple of examples. We've got you covered in this area. In this repo, navigate to the *examples* directory. You will notice a few examples that will help you achieve a solid understanding of how things work, along with the required CSV data files, templates, and theme files too. 



## Contributing

We value **contributions** from anyone, especially you! There is always something to be tested, fixed, developed, and documented here. If you're ever **interested**, please see [Contributing](CONTRIBUTING.md) to learn how you can get started helping us to develop and improve *ColorEx*!



## License

This project is licensed under **MIT License.** 

See [License](LICENSE.md) for more information.
