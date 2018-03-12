import numpy as np


def pretty_print_matrix(A, name='A'):
    if not isinstance(A, np.ndarray) or A.ndim > 2:
        raise TypeError('A must be a 1 or 2 dimensional numpy array')

    preface_str = '{} = '.format(name)
    preface_space = ' ' * len(preface_str)

    # Figure out how long a line is going to be so that we can print the top pretty line
    # Force A to be a 2D matrix so that we don't have to keep testing for 1D or 2D later
    if A.ndim == 1:
        A = np.expand_dims(A, axis=1)
    first_line = _pretty_format_row(A[0, :])
    top_bottom_line = '----' + ' '*(len(first_line)-8) + '----'

    # Actually do the printing
    print(preface_space + top_bottom_line)
    print(preface_str + first_line)
    for row in A[1:, :]:
        print(preface_space + _pretty_format_row(row))
    print(preface_space + top_bottom_line)


def _pretty_format_row(row, column_width=15):
    s = '| '
    for val in row.squeeze():
        val_str = '{:.6g}'.format(val)
        space_str = ' '*(column_width - len(val_str))
        s += val_str + space_str
    s += ' |'
    return s