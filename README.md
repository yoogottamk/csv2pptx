# csv2pptx
Generate slides in a presentation using a template with placeholders

## How to use this?
0. Install python modules
    ```bash
    pip install -r requirements.txt
    ```
1. Create a template which you want to populate. [Or use the one provided in examples]
2. For text, you can add placeholders in the slide like: `{{template}}`

    **Make sure you have only one template in a single textbox**
3. Create a csv with a single line header which has the placeholders [eg: `{{template}}`].
  The rows can be filled with the data with which you want to replace the placeholder.
4. For images, you need to specify the exact position, height and width in`config.py` and the file path in the csv.

    _Check the `example` directory and `config.py` to check exactly how_
5. After you have added all the required files[template, images, csv], run
    ```bash
    python3 main.py
    ```
6. The generated file is `gen.pptx` in the current directory

## Things to take care of
1. Make sure that each textbox has **atmost one** placeholder. If you have multiple,
  you can simply create a new textbox and seperate the two.
2. The order of images in `config.py` specifies the z-index too. Images defined earlier are
  placed before the rest.

## Todo
1. Proper error handling
2. ...
