<br />
<div align="center">
  <h1 align="center">Tugas Kecil 2 IF2211 Strategi Algoritma</h1>

  <p align="center">
    <h3>Creating Bézier Curve with Divide and Conquer based Midpoint Algorithm</h3>
<br>
  </p>
</div>

<!-- CONTRIBUTOR -->
<div align="center" id="contributor">
  <strong>
    <h3>Salsabiila</h3>
    <h3>13522062</h3>
    <h3>Shazya Audrea Taufik</h3>
    <h3>13522063</h3>
  </strong>
</div>

## Table of Contents
  - [Table of Contents](#table-of-contents)
  - [Divide and Conquer Implementation](#divide-and-conquer-implementation)
  - [Program Features](#program-features)
  - [Program Structure](#program-structure)
  - [Module Used](#module-used)
  - [Running The Program](#how-to-run)

<!-- GENERAL INFORMATION -->
## Divide and Conquer Implementation
This program implements the divide and conquer method to approximate points in the Bézier Curve. This is efficient because it reduces the number of evaluations needed to approximate the curve. By recursively dividing the curve into smaller segments and evaluating only the necessary points, we can achieve a good approximation of the Bezier curve with fewer computations compared to evaluating every point directly. Divide phase includes dividing the Bézier curve into two equal parts by finding the midpoint. Conquer phase includes recursively applying the same process to each subsegment until a certain number of iterations.

## Program Features
The features of our program:
* Quadratic Bézier Curve and Nth Degree Bézier Curve
* Divide and Conquer Algorithm + Execution Time + Number of distance calculation operations
<!-- * Visualisation of midpoint algorithm iterations -->
* Bézier curve visualizer

## Program Structure

```
├── bin
│   ├── main.exe
├── doc
│   ├── Tucil2_13522062_13522063.pdf
├── src
│   ├── main.py
│   ├── Quadratic_Brute.py
│   ├── Quadratic_DnC.py
├── test
│   ├── 
└── README.md
```

## Module Used
1. matplotlib.pyplot
2. numpy
3. time
4. collections
5. typing


## How to Run
1. Clone repository 
    ```
    git clone https://github.com/zyaaa-aaa/Tucil2_13522062_13522063.git
    ```
2. Open repository folder in terminal.
3. Change directory into *src* with `cd src`
3.  Type in terminal
    ```
    python3 main.py
    ```
(alternative)
1. Clone repository
    ```
    git clone https://github.com/zyaaa-aaa/Tucil2_13522062_13522063.git
    ```
2. Open main.py
3. Run program

<br>
<h3 align="center"> THANK YOU! </h3>