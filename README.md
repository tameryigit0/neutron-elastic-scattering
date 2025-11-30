# neutron-elastic-scattering
Calculation of the final energy of a neutron resulting from an elastic collision with a target nucleus.
Computational Analysis of Neutron Elastic Scattering

1. Introduction

This project provides a computational implementation for analyzing the kinematics of neutron elastic scattering with a stationary target nucleus. Elastic scattering is the primary mechanism for neutron moderation (thermalization) in nuclear reactors, making the accurate calculation of energy transfer essential for reactor physics and shielding analysis.

The provided Python script calculates the post-collision kinetic energy ($E'$) of a neutron based on the target mass number ($A$) and the scattering angle in the Center of Mass (COM) system.

2. Theoretical Background

The mechanics of the collision are analyzed using conservation of momentum and energy. While the scattering angle is naturally described in the Center of Mass system ($\theta_{CM}$), the energy loss is observed in the Laboratory system ($E_L$).

The ratio of the final neutron energy $E'$ to the initial energy $E_0$ is governed by the following kinematic relationship:

$$\frac{E'}{E_0} = \frac{A^2 + 1 + 2A \cos(\theta_{CM})}{(A + 1)^2}$$

Where:

$E'$: Final neutron energy (MeV)

$E_0$: Initial neutron energy (Normalized to 1.0 MeV in this simulation)

$A$: Mass number of the target nucleus ($M_{target} / m_{neutron}$)

$\theta_{CM}$: Scattering angle in the Center of Mass system

3. Implementation Details

The simulation is implemented in Python and utilizes the standard math library for trigonometric computations. The code structure is defined as follows:

3.1. Variables

E0: Represents the incident neutron energy, initialized to 1.0 unit (e.g., MeV).

A: The mass number of the target nucleus (user input).

tetha: The scattering angle input by the user.

numerator / denominator: Intermediate variables representing the algebraic components of the collision formula derived from the transformation between COM and Lab frames.

3.2. Calculation Logic

The script executes the computation in three steps:

Input Acquisition: Queries the user for target properties and scattering geometry.

Unit Conversion: Converts the input angle into radians using math.radians().

Energy Computation: Evaluates the kinematic factor $\alpha(\theta)$ to determine the final energy.

4. Usage Instructions

Prerequisites

Python 3.x

No external dependencies required (uses standard library).

Execution

Run the script via a terminal or Python IDE:

python neutron_scattering.py


Input Parameters

The program requires two inputs during runtime:

Mass Number ($A$): Integer or float representing the target nucleus (e.g., 1 for Hydrogen, 12 for Carbon).

Scattering Angle: The angle of scattering.

Note on Units: The script applies a degree-to-radian conversion. Ensure the input is provided in degrees to obtain the physically correct result (e.g., input 180 for a back-scattering event corresponding to $\pi$ radians).

5. Sample Output

Scenario: Scattering off Carbon-12 ($A=12$) at $45^{\circ}$.

Enter mass number: 12
Enter scattering angle (radian): 45
mass number: 12.0
scattering angle (radian): 0.7853981633974483
Final neutron energy (MeV): 0.962372
