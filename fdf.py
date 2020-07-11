#!/usr/bin/env python3
from fdfgen import forge_fdf
fields = [('Name', 'John Smith')]
fdf = forge_fdf("",fields,[],[],[])

with open("data.fdf", "wb") as fdf_file:
 fdf_file.write(fdf)
