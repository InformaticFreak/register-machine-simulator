
import os, sys

class RM:
	"""
	Components:
	 - Accumulator as float
	 - Instruction counter (program index) as integer
	 - Instruction register as tuple with command and parameter
	 - Program memory as list of tuples with command and parameter
	 - Data memory as dictionary of index and value
	"""
	def __init__(self, file_name):
		"""Load file into the program memory"""
		self.__pmem = [["INI", 0]]
		with open(os.path.join(file_name), "r") as file:
			lines = file.readlines()
			list_of_code = [ line.replace("\n", "").upper().split(" ") for line in lines if not (line.replace("\n", "").startswith("#") or line.replace("\n", "") == "")]
			list_of_tuples = [ [str(element[0]), float(element[1])] for element in list_of_code ]
		self.__pmem.extend(list_of_tuples)
		"""Load anchor points as a reference to the equivalent index in the program memory"""
		self.__areg = {}
		for i, e in enumerate(self.__pmem):
			if e[0] == "ANC":
				self.__areg[e[1]] = i
		"""Initialize the data memory as an empty dictionary and the accumulator and instruction counter with zero"""
		self.__dmem = {}
		self.__accu = 0
		self.__cind = 0
		"""
		Initialize the command register in two parts. Firstly, the command parameter as an attribute and secondly, 
		the command as a dictionary with all command names as keys and the corresponding method as an item.
		"""
		self.__cpar = 0
		self.__creg = {
			"INI": self.__INI,
			"LDK": self.__LDK,
			"LDA": self.__LDA,
			"LDP": self.__LDP,
			"STA": self.__STA,
			"STP": self.__STP,
			"JMP": self.__JMP,
			"JEZ": self.__JEZ,
			"JLZ": self.__JLZ,
			"JGZ": self.__JGZ,
			"JNE": self.__JNE,
			"JLE": self.__JLE,
			"JGE": self.__JGE,
			"ANC": self.__ANC,
			"INP": self.__INP,
			"OUT": self.__OUT,
			"ADK": self.__ADK,
			"ADA": self.__ADA,
			"ADP": self.__ADP,
			"SUK": self.__SUK,
			"SUA": self.__SUA,
			"SUP": self.__SUP,
			"MUK": self.__MUK,
			"MUA": self.__MUA,
			"MUP": self.__MUP,
			"DIK": self.__DIK,
			"DIA": self.__DIA,
			"DIP": self.__DIP,
			"HLT": self.__HLT,
		}
	
	def next(self):
		"""Read the current command name and command parameter from the program memory and execute the command."""
		cmd, par = self.__pmem[self.__cind]
		self.__cpar = par
		return self.__creg[cmd]()
	
	def status(self):
		"""Return the status of the accumulator and the instruction counter"""
		return (self.__accu, self.__cind)
	
	"""
	All these methods are the implementations for the corresponding instruction name from the instruction register.
	They change the instruction index, accumulator or data memory depending on the functionality.
	"""
	def __INI(self):
		self.__cind += 1
	def __LDK(self):
		self.__accu = self.__cpar
		self.__cind += 1
	def __LDA(self):
		self.__accu = self.__dmem[self.__cpar]
		self.__cind += 1
	def __LDP(self):
		self.__accu = self.__dmem[self.__dmem[self.__cpar]]
		self.__cind += 1
	def __STA(self):
		self.__dmem[self.__cpar] = self.__accu
		self.__cind += 1
	def __STP(self):
		self.__dmem[self.__dmem[self.__cpar]] = self.__accu
		self.__cind += 1
	def __JMP(self):
		self.__cind = self.__areg[self.__cpar]
	def __JEZ(self):
		if self.__accu == 0:
			self.__cind = self.__areg[self.__cpar]
		else:
			self.__cind += 1
	def __JLZ(self):
		if self.__accu < 0:
			self.__cind = self.__areg[self.__cpar]
		else:
			self.__cind += 1
	def __JGZ(self):
		if self.__accu > 0:
			self.__cind = self.__areg[self.__cpar]
		else:
			self.__cind += 1
	def __JNE(self):
		if self.__accu != 0:
			self.__cind = self.__areg[self.__cpar]
		else:
			self.__cind += 1
	def __JLE(self):
		if self.__accu <= 0:
			self.__cind = self.__areg[self.__cpar]
		else:
			self.__cind += 1
	def __JGE(self):
		if self.__accu >= 0:
			self.__cind = self.__areg[self.__cpar]
		else:
			self.__cind += 1
	def __ANC(self):
		self.__cind += 1
	def __INP(self):
		self.__dmem[self.__cpar] = float(input("INP: "))
		self.__cind += 1
	def __OUT(self):
		print("OUT: " + str(self.__dmem[self.__cpar]))
		self.__cind += 1
	def __ADK(self):
		self.__accu += self.__cpar
		self.__cind += 1
	def __ADA(self):
		self.__accu += self.__dmem[self.__cpar]
		self.__cind += 1
	def __ADP(self):
		self.__accu += self.__dmem[self.__dmem[self.__cpar]]
		self.__cind += 1
	def __SUK(self):
		self.__accu -= self.__cpar
		self.__cind += 1
	def __SUA(self):
		self.__accu -= self.__dmem[self.__cpar]
		self.__cind += 1
	def __SUP(self):
		self.__accu -= self.__dmem[self.__dmem[self.__cpar]]
		self.__cind += 1
	def __MUK(self):
		self.__accu *= self.__cpar
		self.__cind += 1
	def __MUA(self):
		self.__accu *= self.__dmem[self.__cpar]
		self.__cind += 1
	def __MUP(self):
		self.__accu *= self.__dmem[self.__dmem[self.__cpar]]
		self.__cind += 1
	def __DIK(self):
		self.__accu /= self.__cpar
		self.__cind += 1
	def __DIA(self):
		self.__accu /= self.__dmem[self.__cpar]
		self.__cind += 1
	def __DIP(self):
		self.__accu /= self.__dmem[self.__dmem[self.__cpar]]
		self.__cind += 1
	def __HLT(self):
		return 0

"""
Command line arguments:
 1st: path to the file
 2nd: "-p" (printing of the status of the accumulator and the instruction counter) OR "-w" (printing the status ~ and wait for enter)
"""

if __name__ == "__main__":
	"""1st argument"""
	if len(sys.argv) >= 2:
		arg_file = str(sys.argv[1])
	else:
		raise AttributeError
	"""2nd argument"""
	arg_print, arg_wait = False, False
	if len(sys.argv) >= 3:
		if sys.argv[2] == "-p":
			arg_print = True
		elif sys.argv[2] == "-w":
			arg_wait = True
		else:
			raise ValueError

	"""Mainloop"""
	rm = RM(arg_file)
	while True:
		error = rm.next()
		if error == 0: print("Program finished\n")
		if error != None: break
		"""Printing the status"""
		status = rm.status()
		if arg_print or arg_wait: print(f"STATUS: accu: {status[0]} | cind: {status[1]}")
		if arg_wait: input()
