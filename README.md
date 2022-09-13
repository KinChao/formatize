# A python script to correct the CDL2 m3 ff formatting to be used in Charmm-gui

**Problem: CDL2 lipid is not yet available in the Charmm-gui in martini 3 ff setting** <br /> <br />
**Solution: Merge the m2 protein input files from charmm-gui and m3 membrane (including CDL2) input files also from charmm-gui** <br /> <br />
**Challenge: m2 and m3 martinises the protein differently so we will need to correct the numbering** <br /> <br />
**Solution: Use Excel to autofill the numbering** <br /> <br />
**Problem: Excel will mess up the specified formatting that is used in gromacs** <br /> <br />

**This martinse.py script is created to convert the tap separated entities in Excel to the very specific "gromacs" formatting of the pdb file so that the software can run successfully**
