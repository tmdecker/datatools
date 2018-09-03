# datatools

A collection of useful python functions.

### Installing

Install using pip:

```
pip install git+git://github.com/tmdecker/datatools.git
```
Upgrade:
```
pip install --upgrade git+git://github.com/tmdecker/datatools.git
```

### Dependencies

In addition to Python 3.6 you should have each of the following python libraries installed:
- pandas 0.22.0
- numpy 1.14.2
- matplotlib 2.1.0
- seaborn 0.8.1
- bokeh 0.12.14

### Usage

Import a submodule:
```python
import datatools.datatools as dt

s = dt.txt2str("myfile.txt")
```

Import a specific function of a submodule:
```python
from tdtools.datascience import txt2str

s = txt2str("myfile.txt")
```

## Authors

* **Tim-M. Decker**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Additional resources
Preparing graphs: https://python-graph-gallery.com/  
Colors: http://www.color-hex.com/, http://www.colorbrewer2.org
