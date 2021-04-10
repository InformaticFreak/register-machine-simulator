
import os, sys, time, platform
from colorama import init, Fore, Back, Style
init(autoreset=False)

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
		self.os = platform.system().lower()
		"""Load file into the program memory"""
		self.__pmem = []
		self.__pmem.append(["INI", 00])
		with open(os.path.join(file_name), "r") as file:
			lines = file.readlines()
			list_of_code = [ line.replace("\n", "").upper().split(" ") for line in lines if not (line.replace("\n", "").startswith("#") or line.replace("\n", "") == "")]
			list_of_tuples = [ [str(element[0]), float(element[1])] for element in list_of_code ]
		self.__pmem.extend(list_of_tuples)
		self.__pmem.append(["HLT", 99])
		"""Load anchor points as a reference to the equivalent index in the program memory"""
		self.__areg = {}
		for i, e in enumerate(self.__pmem):
			if e[0] == "ANC":
				self.__areg[e[1]] = i
		"""Initialize the data memory as an empty dictionary and the accumulator and instruction counter with zero"""
		self.__dmem = {}
		self.__accu = 0
		self.__pind = 0
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
			"BRK": self.__BRK
		}
		"""Command markdown register"""
		self.__cmdr = {
			"LDK LDA LDP STA STP ldk lda ldp sta stp": Fore.MAGENTA,
			"JMP JEZ JLZ JGZ JNE JLE JGE ANC jmp jez jlz jgz jne jle jge anc": Fore.RED,
			"ADK ADA ADP SUK SUA SUP MUK MUA MUP DIK DIA DIP adk ada adp suk sua sup muk mua mup dik dia dip": Fore.YELLOW,
			"INP OUT HLT INI BRK inp out hlt ini brk": Fore.CYAN
		}
	
	def next(self):
		"""Read the current command name and command parameter from the program memory and execute the command."""
		cmd, par = self.__pmem[self.__pind]
		self.__cpar = par
		return self.__creg[cmd]()
	
	def status(self):
		"""Return the complete status of the register machine"""
		return {"dmem": self.__dmem, "pmem": self.__pmem, "accu": self.__accu, "pind": self.__pind, "cpar": self.__cpar, "creg": self.__creg, "areg": self.__areg}
	
	def show(self):
		"""Show the status of the register machine"""
		listScreen_dmem = [ f"{dmem}: {self.__dmem[dmem]}" for dmem in self.__dmem ]
		cLen = 20
		cRes = Fore.WHITE
		listScreen = []
		listScreen.append("")
		listScreen.append(f" {fit('Instruction counter', cLen)} | {fit('Program memory', cLen)} | {fit('Data memory', cLen)} | {fit('Accumulator', cLen)} ")
		listScreen.append(f"-{'-' * cLen}-+-{'-' * cLen}-+-{'-' * cLen}-+-{'-' * cLen}-")
		for ind, pmem in enumerate(self.__pmem):
			dmem, o_pind, accu, sInd = "", "l", "", Style.DIM
			if ind < len(listScreen_dmem): dmem = listScreen_dmem[ind]
			if ind == self.__pind: o_pind = "r"; sInd = Style.BRIGHT
			if ind == 0: accu = self.__accu
			try: cPmem = self.__cmdr[[ key for key in self.__cmdr if self.__pmem[ind][0] in key ][0]]
			except: cPmem = ""
			listScreen.append(f" {sInd + fit(ind, cLen, o_pind)} | {cPmem + pmem[0] + cRes + ' ' + fit(pmem[1], cLen - 4)} | {fit(dmem, cLen)} | {fit(accu, cLen)} ")
		screen = "\n".join(listScreen)
		if self.os == "windows": os.system("cls")
		else: os.system("clear")
		print(screen)
	
	"""
	All these methods are the implementations for the corresponding instruction name from the instruction register.
	They change the instruction index, accumulator or data memory depending on the functionality.
	"""
	"""Start and terminate the program"""
	def __INI(self):
		self.__pind += 1
	def __HLT(self):
		return "HLT"
	def __BRK(self):
		self.__pind += 1
		return "BRK"
	"""Load and store values"""
	def __LDK(self):
		self.__accu = self.__cpar
		self.__pind += 1
	def __LDA(self):
		self.__accu = self.__dmem[self.__cpar]
		self.__pind += 1
	def __LDP(self):
		self.__accu = self.__dmem[self.__dmem[self.__cpar]]
		self.__pind += 1
	def __STA(self):
		self.__dmem[self.__cpar] = self.__accu
		self.__pind += 1
	def __STP(self):
		self.__dmem[self.__dmem[self.__cpar]] = self.__accu
		self.__pind += 1
	"""Anchor points and jumps to them"""
	def __ANC(self):
		self.__pind += 1
	def __JMP(self):
		self.__pind = self.__areg[self.__cpar]
	def __JEZ(self):
		if self.__accu == 0:
			self.__pind = self.__areg[self.__cpar]
		else:
			self.__pind += 1
	def __JLZ(self):
		if self.__accu < 0:
			self.__pind = self.__areg[self.__cpar]
		else:
			self.__pind += 1
	def __JGZ(self):
		if self.__accu > 0:
			self.__pind = self.__areg[self.__cpar]
		else:
			self.__pind += 1
	def __JNE(self):
		if self.__accu != 0:
			self.__pind = self.__areg[self.__cpar]
		else:
			self.__pind += 1
	def __JLE(self):
		if self.__accu <= 0:
			self.__pind = self.__areg[self.__cpar]
		else:
			self.__pind += 1
	def __JGE(self):
		if self.__accu >= 0:
			self.__pind = self.__areg[self.__cpar]
		else:
			self.__pind += 1
	"""Read input and print output"""
	def __INP(self):
		try:
			self.__dmem[self.__cpar] = float(input("INP: "))
			self.__pind += 1
		except:
			pass
	def __OUT(self):
		self.__pind += 1
		return f"OUT: {self.__dmem[self.__cpar]}"
	"""Arithmetic operations"""
	def __ADK(self):
		self.__accu += self.__cpar
		self.__pind += 1
	def __ADA(self):
		self.__accu += self.__dmem[self.__cpar]
		self.__pind += 1
	def __ADP(self):
		self.__accu += self.__dmem[self.__dmem[self.__cpar]]
		self.__pind += 1
	def __SUK(self):
		self.__accu -= self.__cpar
		self.__pind += 1
	def __SUA(self):
		self.__accu -= self.__dmem[self.__cpar]
		self.__pind += 1
	def __SUP(self):
		self.__accu -= self.__dmem[self.__dmem[self.__cpar]]
		self.__pind += 1
	def __MUK(self):
		self.__accu *= self.__cpar
		self.__pind += 1
	def __MUA(self):
		self.__accu *= self.__dmem[self.__cpar]
		self.__pind += 1
	def __MUP(self):
		self.__accu *= self.__dmem[self.__dmem[self.__cpar]]
		self.__pind += 1
	def __DIK(self):
		self.__accu /= self.__cpar
		self.__pind += 1
	def __DIA(self):
		self.__accu /= self.__dmem[self.__cpar]
		self.__pind += 1
	def __DIP(self):
		self.__accu /= self.__dmem[self.__dmem[self.__cpar]]
		self.__pind += 1

def fit(text, length, orientation="l", fillCharakter=" ", endCharakter=" ..."):
	"""Return input text, but cut to a maximum length"""
	text, length, fillCharakter = str(text), int(length), str(fillCharakter)
	if len(text) <= length:
		orientation = orientation.lower()[0]
		if orientation == "c":
			leftLen = (length - len(text)) // 2
			rightLen = length - len(text) - leftLen
			return "{}{}{}".format(leftLen * fillCharakter, text, rightLen * fillCharakter)
		elif orientation == "r":
			return "{}{}".format((length - len(text)) * fillCharakter, text)
		else:
			return "{}{}".format(text, (length - len(text)) * fillCharakter)
	else:
		return "{}{}".format(text[0:length-len(endCharakter)], endCharakter)

"""
Command line arguments:
 1st: path to the .rm code file
 2nd: "-p" (printing of the status of the accumulator and the instruction counter) OR "-w" (printing the status ~ and wait for enter)
 3rd: time in millisecons between commands for print mode "-p"
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
	if arg_print or arg_wait:
		if platform.system().lower() == "windows":
			os.system("mode con cols=100")
	"""3rd argument"""
	arg_time = 0.01
	if len(sys.argv) >= 4:
		if sys.argv[3].isdigit():
			if int(sys.argv[3]) >= 0:
				arg_time = int(sys.argv[3]) / 1_000
			else:
				raise ValueError
		else:
			raise ValueError

	"""Mainloop"""
	rm = RM(arg_file)
	while True:
		"""Printing the status"""
		if arg_print or arg_wait:
			rm.show()
		if arg_wait:
			input("WAIT")
		elif arg_print:
			print()
			time.sleep(arg_time)
		"""Execute next command"""
		error = rm.next()
		if error == "HLT":
			print("Program finished\n")
			break
		elif error == "BRK" and arg_print:
			input("BRK")
		elif error is not None and error[:3] == "OUT":
			input(error)
		elif error != None:
			print("Unexpected error\n")
			break
