<br />
<div align="center">
  <h1 align="center">Tugas Kecil 2 IF2211 Strategi Algoritma</h1>

  <p align="center">
    <h3>Creating Bézier Curve with Divide and Conquer based Midpoint Algorithm</h3>

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
* Nth Degree Bézier Curve
* Divide and Conquer Algorithm + Execution Time
* Brute Force Algorithm + Execution Time
* Visualisation of midpoint algorithm iterations
* Bézier curve visualizer

## Program Structure

```
├── bin
│   ├── main.exe
├── doc
│   ├── Tucil2_13522062_13522063.pdf
├── src
│   ├── Input.py
│   ├── main.py
│   ├── N_BF.py
│   ├── N_DnC.py
│   ├── Visualisation.py
├── test
│   ├── Bonus_1.png
│   ├── Bonus_2.png
│   ├── Bonus_3.png
│   ├── Bonus_4.png
│   ├── Bonus_5.png
│   ├── Bonus_6.png
│   ├── Test_1.png
│   ├── Test_2.png
│   ├── Test_3.png
│   ├── Test_4.png
│   ├── Test_5.png
│   ├── Test_6.png
└── README.md
```

## Module Used
1. matplotlib.pyplot
2. matplotlib.animation
3. numpy
4. time
5. collections
6. typing


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


## Program Flow
1. The program will display the main menu.
2. The program will accept the desired user input. If the input is not valid, the program will continue to accept input choices until so.
3. If the user selects option 1 (Nth Degree), the program will accept the number of control points as input. Then, the program will accept each control point according to the previously inputted number. The program will also accept the input for the number of iterations. If the inputted point exceeds 2 digits or is not a number, the program will prompt for the point input again.
4. The program will execute the creation of Nth bezier curves using both the divide and conquer method and the brute force method.
5. The program will display the execution time for both methods as well as a comparison of their execution times.
6. The program will display the curve generated using the divide and conquer method and the curve using the brute force method.
7. Then, the program will provide an option to display the final visualization. If the user selects 3, the main screen will reappear.
8. The program will accept input choices again. The program will only stop when the user chooses option 2 (exit).

<br>
<h3 align="center"> THANK YOU! </h3>