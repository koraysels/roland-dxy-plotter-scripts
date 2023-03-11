# setup Requirements
## MacOS
Install [pstoedit](http://www.calvina.de/pstoedit/)

Via Brew: `brew install pstoedit`

Download [HPGL-Distiller](https://pldaniels.com/hpgl-distiller/)

Install / Make:

- `tar zxvf hpgl-distiller-0.9.1.tar.gz`
- `cd hpgl-distiller-0.9.1; make`
- `make install`

Then install requirements.txt 

```bash
$ pip install -r requirements.txt
```
---

## Linux

Install [pstoedit](http://www.calvina.de/pstoedit/)

Via apt-get: `sudo apt-get install pstoedit`

Download [HPGL-Distiller](https://pldaniels.com/hpgl-distiller/)

Install:

- `tar zxvf hpgl-distiller-0.9.1.tar.gz`
- `cd hpgl-distiller-0.9.1; make`
- `make install`

```bash
$ pip install -r requirements.txt
```
----


# Usage


```bash
$ sh ep-to-plotter.sh <your-epsfile>.eps
```