#!/usr/bin/env python3
$ pytest -v test.py
============================= test session starts ==============================
...
collected 5 items
 
test.py::test_exists PASSED                                              [ 20%]
test.py::test_runnable PASSED                                            [ 40%]
test.py::test_executable FAILED                                          [ 60%]
test.py::test_usage FAILED                                               [ 80%]
test.py::test_input FAILED                                               [100%]
 
=================================== FAILURES ==================================
=
