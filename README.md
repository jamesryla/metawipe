# metawipe
**A tool for removing exif data from images.**

Written in python, this tool allows you to remove unwanted exif data from your png, jpg or jpeg images.

Why? Our cameras and various devices as well as applications add exif data to images when they are created. This data can range from harmless info like the size of your image or the model of your camera to more dangerous things like your location. Many websites and applications nowadays remove excess exif data from images when you upload but not all. The scarier part is we have no idea what they may be doing with that information when they remove it. This tool provides a way to wipe the exif data before you upload.

> help menu

![help2](https://github.com/jamesryla/metawipe/assets/58945104/b33ba290-78b3-45c7-b59b-7625de4003d2)

with metawipe you can overwrite your original image or export to png, jpg or jpeg.

> sample exif data from an out of camera image using photool to pull exif data

![before_cleaning2_photool](https://github.com/jamesryla/metawipe/assets/58945104/49deb280-6964-4065-8ef7-6c847b74c7d2)

> exif data pulled using exiftool

![before_cleaning2](https://github.com/jamesryla/metawipe/assets/58945104/8f4537b9-62aa-4fa2-b6f9-d9199d54e81e)

> running metawipe

![cleaning2](https://github.com/jamesryla/metawipe/assets/58945104/a6ad456c-afca-4034-982a-576142af74e3)

> exif data from the cleaned image

![after_cleaning2](https://github.com/jamesryla/metawipe/assets/58945104/305aea39-954a-48e9-b6bb-e213bb9c29a6)

the exif data that exists after cleaning the image is minimal and does not give away any sensitive information that previously existed.
