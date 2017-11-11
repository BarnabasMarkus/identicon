# IDENTICON

## About

A Python library for generating GitHub-like symmetrical 5x5 identicons.

[Identicon wikipedia](https://en.wikipedia.org/wiki/Identicon)
[GitHub identicons](https://github.com/blog/1586-identicons)

## Requirements
Pillow
```
pip3 install pillow
```

## Usage / example

```Python
>>> from identicon import Identicon
>>> user_id = 3523461435
>>> icon = Identicon(user_id)
>>> icon.show()
>>> icon.save()
```
![Result identicon](http://url/to/img.png)

```Python
>>> icon = Identicon(8756324)
>>> icon.show()
>>> icon.save()
```
![Result identicon](http://url/to/img.png)

```Python
>>> icon = Identicon(8756324)
>>> icon.show()
>>> icon.save()
```
![Result identicon](http://url/to/img.png)

