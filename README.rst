ANR Express by G Paw
========================

This is an internal Philips tool to assist Field Engineers to generate FCO Action Notification Report (ANR) form as quickly & efficiently as possible while still complying with Philips Quality Assurance rules.

Creating the .exe:
1. cd into the directory "\ANR_Express"
2. in cmd generate the .exe by typing "pyinstaller ANR_EX.py"
3. place the template.PDF into the \dist\ANR_EX
4. copy the entire reportlab folder from C:\Python27\Lib\site-packages\reportlab and paste it into \dist\ANR_EX (this is to resolve a dependency issue)

Usage:
1.	Copy \dist\ and keep it in a folder somewhere. No installation required.
2.	In the folder, check that template.pdf is the correct ANR required. 
3.	Run ANR_EX.exe
4.	Enter all ANR form details
5.	Click “Generate ANR” to generate a PDF in a new folder called _output

Beware:
1.	The PDF editing function reads off a single template.pdf. User may substitute with the template with another but it may cause the position mapping of all the information to be shifted.
2.	Data.txt is generated and should not be delete or modified. If you messed up the data.txt, just delete it and the program will generate a new one.




