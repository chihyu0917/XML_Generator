# XML Generator (XML DOM)

An album management system, using AJAX to convert an input text file into an output XML file, with the backend implemented in Python Flask. Achieving the reading of XML files, and the addition, modification, deletion, and querying of elements using the DOM API. 
The method of use switches between various subsystems for generating XML, adding albums, modifying albums, deleting albums, and querying albums.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

If running on Localhost, please ensure that the Python modules [flask](https://pypi.org/project/Flask/), [flask-cors](https://pypi.org/project/Flask-Cors/), and [jsons](https://pypi.org/project/Flask-Cors/) have been installed.
Then, execute the app on shell.
```sh
python app.py
```
If you don't want to install anything, please click the following link.
XML Generator has deployed on render.com: 
https://xml-generator-1lwe.onrender.com/

## Usage

- Generating XML: The file format for upload must be .txt. The upload result can be seen on returning to the main screen.
- Adding albums, Modifying albums: The URL field must be a web image link and cannot be left blank.
- Deleting albums: Click the delete button.
- Querying albums: Search for the singer's name.

