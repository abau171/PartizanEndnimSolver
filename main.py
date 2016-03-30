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
		return state[0]
	elif len(state) == 2:
		a, b = state[0], state[1]
		return b if a < b else 0
	else:
		w, b = state[:-1], state[-1]
		return L(w) - R(w) + b if b > R(w) else 0

def R(state):
	if state in right_cache:
		return right_cache[state]
	else:
		result = R_uncached(state)
		right_cache[state] = result
		return result

def R_uncached(state):
	if len(state) == 1:
		return state[0]
	elif len(state) == 2:
		a, b = state[0], state[1]
		return a if b < a else 0
	else:
		a, w = state[0], state[1:]
		return R(w) - L(w) + a if a > L(w) else 0

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
