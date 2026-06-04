#!/bin/bash

# runs all the test in the test/folder

echo "Running ENTSO-E object generation tests..."

for full_path in test/*_test.py; do
    test_file_raw=$(echo "$full_path" | cut -d'/' -f2)
    test_file=${test_file_raw%???}
    python -m "test.$test_file"
    if [ $? -ne 0 ]; then
        echo "Test failed: $test_file"
    fi
done

echo "Generating test cases exeecuted successfully!"