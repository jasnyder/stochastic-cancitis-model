from collections import namedtuple
import numpy as np

def nonreduced_cancitis_rhs(t, u, p=[8.7e-4, 1.5e-3, 1.1e-5, 1.1e-5, 4.7e13, 4.7e13, 2e-3, 2e-3, 129, 129, 2e-9, 7.5e-5, 7.5e-5, 7.5e-5, 7.5e-5, 2, 3e-4, 2e9, 2e-8, 7]):
    # defines the right-hand side of the original cancitis model as defined in the PLOS One paper from 2017
    # for now only allows constant external inflammatory load I (last entry in p)
    rx, ry, ax, ay, Ax, Ay, dx0, dy0, dx1, dy1, dy0t, cxx, cxy, cyx, cyy, es, rs, ea, rm, I = p
    x0, x1, y0, y1, a, s = u
    phix = 1/(1+(cxx*x0 + cxy*y0)**2)
    phiy = 1/(1+(cyx*x0 + cyy*y0)**2)
    return np.array([
        (rx * phix * s - dx0 - ax - rm*s)*x0,
        ax*Ax*x0 - dx1*x1,
        (ry * phiy * s - dy0 - ay)*y0 + rm*s*x0,
        ay*Ay*y0 - dy1*y1,
        dx0*x0 + dx1*x1 + dy0*y0 + dy1*y1 - ea*s*a,
        rs*a - es*a + I
    ])

def reduced_cancitis_rhs(t, X, J, R, Bx, By, Cx, Cy, D0, D1):
    num = J + np.sqrt(J**2 + 2*Bx*X[0] + 2*By*X[1])
    return np.array([((num / (1 + X[0] + Cy*X[1])) - 1) * X[0],
                     (R*(num / (1 + Cx*X[0] + X[1])) - D0 - D1*X[1]) * X[1]])


def dimensional_reduced_cancitis_rhs(t, x, rx, ry, ax, ay, Ax, Ay, dx0, dy0, dx1, dy1, dy0t, cxx, cxy, cyx, cyy, es, rs, ea, I):
    x0, y0 = x
    x1 = ax*Ax*x0/dx1
    y1 = ay*Ay*y0/dy1
    phix = 1/(1+cxx*x0 + cxy*y0)
    phiy = 1/(1+cyx*x0 + cyy*y0)
    kappa = dx0*x0 + (dy0t*y0 + dy0)*y0 + dx1*x1 + dy1*y1
    a = 0.5*np.sqrt((I/rs)**2 + 4*es*kappa/(ea*rs)) - I/(2*rs)
    s = rs*a/es + I/es
    return np.array([
        (rx*phix*s - dx0 - ax)*x0,
        (ry*phiy*s - dy0 - dy0t*y0 - ay)*y0
    ])


Args = namedtuple('Args', ['J', 'R', 'Bx', 'By', 'Cx', 'Cy', 'D0', 'D1'],
                  defaults=(0.76, 1.49, 0.06, 0.07, 0.93, 1.08, 1.0, 0.1))
DimlArgs = namedtuple('DimlArgs', ['rx', 'ry', 'ax', 'ay', 'Ax', 'Ay', 'dx0', 'dy0', 'dx1', 'dy1', 'dy0t', 'cxx', 'cxy', 'cyx', 'cyy', 'es', 'rs', 'ea', 'I'],
                      defaults=(8.7e-4, 1.5e-3, 1.1e-5, 0.52e-5, 4.7e9, 4.7e9, 2e-3, 2e-3, 1.29e-2, 1.29e-2, 2e-9, 5.6e-5, 5.4e-5, 5.2e-5, 5.0e-5, 2, 3e-4, 2e5, 7))
