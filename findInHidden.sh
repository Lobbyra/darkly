#!/bin/bash
grep -rn ./hidden/ | grep -v 'voisin\|Toujours pas\|aide\|toujours'
