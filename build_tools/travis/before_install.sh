#!/bin/bash

if [[ "$TRAVIS_OS_NAME" == "linux" ]]; then apt-get update; fi

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then brew update && brew install md5sha1sum; fi

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
# Since default gcc on osx is just a front-end for LLVM
    if [[ "$CC" == "gcc" ]]; then
        export CXX=g++-4.9
        export CC=gcc-4.9
    fi
fi