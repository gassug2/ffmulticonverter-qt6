FF Multi Converter
====================

FF Multi Converter is a simple graphical application for Linux which enables you
to convert audio, video, image and document files between all popular formats,
by utilizing and combining other programs. It uses ffmpeg for audio/video files,
unoconv for document files and the ImageMagick library for image file conversions.

Project homepage: https://sites.google.com/site/ffmulticonverter/

Dependencies
-------------
python3
pyqt6

Optional dependencies
----------------------
ffmpeg
imagemagick
unoconv

The program does NOT require the optional dependencies to run.
e.g. you can run the application even if you don't have ImageMagick installed,
but you will be able to convert any other types except image files.

Feature selection
-----------------

FFMC_AUDIOVIDEO, FFMC_IMAGE, and FFMC_DOCUMENT environment variables
control which features are enabled at build time.

These values are used during the build process to generate:

    ffmulticonverter/features.py

This file determines which tabs and functionality are included in the application.
The settings do NOT affect runtime behavior directly.

In order to generate your desired featureset, run:

    python generate_features.py

With the appropriate environment variables, and then build

Build
-----

Run the following in the app directory:

    python -m build

Installation
-------------
From application's directory run as root:

    python -m install dist/*.whl

Or:

    pip install dist/*.whl

Run without installing
-----------------------
You can even launch the application without installing it, by running the
launcher script. This option has not been extensively tested for everyday use
though, and you may experience unexpected issues.
