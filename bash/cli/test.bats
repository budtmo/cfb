#!/usr/bin/env bats

@test 'Verify help message if there is no argument' {
    output=$(cfb-b)
    [[ $output == *"--help"* ]]
}

@test 'Verify wrong argument' {
    output=$(cfb-b -z)
    [[ $output == *"is not recognized"* ]]
}

@test 'Verify help message' {
    output=$(cfb-b -?)
    [[ $output == *"--help"* ]]
}

@test 'Verify version' {
    output=$(cfb-b --version)
    [[ $output == *"0.1"* ]]
}

@test 'Verify writing output' {
    output=$(cfb-b -w test)
    [[ $output == "test" ]]
}
