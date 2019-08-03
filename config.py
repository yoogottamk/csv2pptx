# path to the template pptx
PATH_PPTX = "example/template.pptx"

# path to data csv
PATH_DATA = "example/data.csv"

"""
Configuration related to images
All properties are required

Adding a new image is as simple as specifying the config here and
populating columns in the csv

The order specifies z-index, later ones are placed above others.

each object in the list:
    name: Same as the header in csv, whose properties are defined here
          The columns for the corresponding name should be path to that image
    unit: One of ["Inches", "Pt", "Cm", "Mm"]
    top: Distance of image's top edge from top in <unit>
    left: Distance of image's left edge from left in <unit>
    height: Height of image in <unit>
    width: Width of image in <unit>
"""
IMG_CONF = [
    {
        "name": "{{image0}}",
        "unit": "Inches",
        "top": 2,
        "left": 2,
        "height": 1,
        "width": 1
    },
    {
        "name": "{{image1}}",
        "unit": "Inches",
        "top": 3,
        "left": 3,
        "height": 2,
        "width": 1
    }
]
