#!/usr/bin/env python3

import argparse

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add two numbers.')
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, help='Second number')
    
    args = parser.parse_args()
    result = add_numbers(args.a, args.b)
    print(f"The sum is: {result}")