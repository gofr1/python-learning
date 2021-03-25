# Settings for VS Code pytest

    {
        "python.pythonPath": "/usr/local/bin/python3",
    
        "python.testing.unittestEnabled": false,
        "python.testing.unittestArgs": [
        ],
        "python.testing.nosetestsEnabled": false,
        "python.testing.pytestEnabled": true, // enables and used pip3 install pytest
        "python.testing.pytestPath": "pytest",
        "python.testing.pytestArgs": [
            "-vs",
            "unit_tests",
            "tests"
        ]
    }

`-v, --verbose` increase verbosity.  
`-q, --quiet` decrease verbosity.  
`-s` shortcut for `--capture=no`.  
`--verbosity=VERBOSE` set verbosity. Default is `0`.  
`--color=color` color terminal output (yes/no/auto).  