#!/bin/bash
cd .hidden || exit 1
grep -rn . | grep -v 'voisin\|Toujours pas\|aide\|toujours'
