# Import package, test suite, and other packages as needed
import molssi_develops
import pytest
import sys
import pytest
import numpy as np

@pytest.mark.parametrize("num_list, expected_mean" , [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5),
    (list(range(1, 1000000)), 1000000/2.0)
])

def test_many(num_list, expected_mean):
    # assert mean(num_list) == expected_mean
    assert np.isclose(molssi_develops.mean(num_list), expected_mean, 1e-6)
def test_mean():
    'test mean function'
    test_list=[1.0,2.0,3.0,4.0,5.0]
    expected_number=3.0
    calculated=molssi_develops.mean(test_list)
    assert expected_number == calculated
    

