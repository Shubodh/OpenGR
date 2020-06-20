# OpenGR

OpenGR is a set C++ libraries for 3D Global Registration.
It is a fork of the [Super4PCS library](https://github.com/nmellado/Super4PCS), and aims at providing several state of the art global registration algorithms for 3d data.
This fork is maintained by the same authors as the Super4PCS library.

See the offical documentation here: https://storm-irit.github.io/OpenGR/index.html

---

Here's a BibTeX entry for OpenGR that you can use in your academic publications:

```
 @MISC{openGR,
  author = {Nicolas Mellado and others},
  title = {OpenGR: A C++ library for 3D Global Registration},
  howpublished = {https://storm-irit.github.io/OpenGR/},
  year = {2017}
 }
```

---

# Grad + OpenGR

This folder is meant for OpenGR experimentation and documentation. Be it as small as a bash script or a big feature like visualization, please commit and document everything.

In the future:

-   Visualization

# Steps to Reproduce Error of Identity Matrix:

1. Downlaod precompiled version of OpenGR from this link : https://github.com/nmellado/Super4PCS/releases/tag/v1.1.3
2. After unzipping the folder go to desired directory using :
   `cd home/travis/build/nmellado/Super4PCS/Super4PCS-v1.1.3-linux-g++-5`
3. To check a working example initially provided by them go to scripts folder using
   `cd scripts`
   and then run command `./run-example.sh`
4. Now to test with our own dataset copy the points clouds of .obj file format to your current working directory.
5. And run it with `../bin/Super4PCS -i path_to_file1 path_to_file2 -o 0.7 -d 0.01 -t 1000 -n 200 -m output.txt`
6. Output is always coming an identity matrix.
