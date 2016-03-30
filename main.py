def state_str(state):
	return " ".join(str(num) for num in state)

class ProofEntry:
	def __init__(self, operation, argument, calculation, result):
		self.operation = operation
		self.argument = argument
		self.calculation = calculation
		self.result = result

proof = []

left_cache = {}
right_cache = {}

def L(state):
	if state in left_cache:
		return left_cache[state]
	else:
		result = L_uncached(state)
		left_cache[state] = result
		return result

def L_uncached(state):
	if len(state) == 1:
		result = state[0]
		proof.append(ProofEntry("L", str(state[0]), None, result))
		return result
	elif len(state) == 2:
		a, b = state[0], state[1]
		if a < b:
			result = b
			proof.append(ProofEntry("L", state_str(state), None, result))
			return result
		else:
			result = 0
			proof.append(ProofEntry("L", state_str(state), None, result))
			return result
	else:
		w, b = state[:-1], state[-1]
		l, r = L(w), R(w)
		if b > r:
			result = l - r + b
			proof.append(ProofEntry("L", state_str(state), "{} - {} + {}".format(l, r, b), result))
			return result
		else:
			result = 0
			proof.append(ProofEntry("L", state_str(state), None, result))
			return result

def R(state):
	if state in right_cache:
		return right_cache[state]
	else:
		result = R_uncached(state)
		right_cache[state] = result
		return result

def R_uncached(state):
	if len(state) == 1:
		result = state[0]
		proof.append(ProofEntry("R", str(state[0]), None, result))
		return result
	elif len(state) == 2:
		a, b = state[0], state[1]
		if b < a:
			result = a
			proof.append(ProofEntry("R", state_str(state), None, result))
			return result
		else:
			result = 0
			proof.append(ProofEntry("R", state_str(state), None, result))
			return result
	else:
		a, w = state[0], state[1:]
		l, r = L(w), R(w)
		if a > l:
			result = r - l + a
			proof.append(ProofEntry("R", state_str(state), "{} - {} + {}".format(r, l, a), result))
			return result
		else:
			result = 0
			proof.append(ProofEntry("R", state_str(state), None, result))
			return result

def get_outcome_class(l, r):
	if l == 0:
		return "P" if r == 0 else "L"
	else:
		return "R" if r == 0 else "N"

if __name__ == "__main__":
	text_state = input("state: ")
	state = tuple(int(num_string) for num_string in text_state.split(" "))
	l = L(state)
	r = R(state)
	outcome_class = get_outcome_class(l, r)
	print("w = " + " ".join(str(num) for num in state))
	print("outcome class " + outcome_class)
	print("L(w) = " + str(l))
	print("R(w) = " + str(r))
	show_proof = input("show proof (y/n)? ")
	if show_proof == "y":
		print("proof:")
		for entry in proof:
			if entry.calculation != None:
				print("{}({}) = {} = {}".format(entry.operation, entry.argument, entry.calculation, entry.result))
			else:
				print("{}({}) = {}".format(entry.operation, entry.argument, entry.result))
