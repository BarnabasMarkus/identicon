# identicon

## About

A Python library for generating GitHub-like symmetrical 5x5 identicons.

[Identicon wikipedia](https://en.wikipedia.org/wiki/Identicon)

[GitHub identicons](https://github.com/blog/1586-identicons)

## Requirements
PIL Pillow package
```
pip3 install pillow
```

## Usage / example

```Python
>>> from identicon import Identicon
>>> user_id = 354
>>> icon = Identicon(user_id)
>>> icon.show()
>>> icon.save()
```
![Result identicon](https://github.com/BarnabasMarkus/identicon/blob/master/examples/354.jpg)

```Python
>>> icon = Identicon(633)
>>> icon.show()
```
![Result identicon](https://github.com/BarnabasMarkus/identicon/blob/master/examples/633.jpg)

```Python
>>> icon = Identicon(643123814053102).show()
```
![Result identicon](https://github.com/BarnabasMarkus/identicon/blob/master/examples/643123814053102.jpg)

```Python
>>> icon = Identicon(905994379828304).show()
```
![Result identicon](https://github.com/BarnabasMarkus/identicon/blob/master/examples/905994379828304.jpg)

## License
MIT License
