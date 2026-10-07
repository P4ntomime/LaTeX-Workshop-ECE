# Figure generator

`cooling-curves.pdf` in the student template is produced here. The
students never see these two files: they get the finished PDF only, so
that nothing in the template suggests they are meant to run an
experiment or process data.

```sh
cd tools
python3 make_figure.py          # writes cooling-curves.pdf
cp cooling-curves.pdf ../../latex-workshop-template/figures/
```

`cooling.csv` is synthetic — Newton's law of cooling for three time
constants, plus simulated thermometer noise. It is not a measurement
and should not be presented as one.
