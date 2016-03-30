def memoize(f):
	cache = {}
	def wrapper(*args, **kwargs):
		key = repr(args) + repr(kwargs)
		if key not in cache:
			result = f(*args, **kwargs)
			cache[key] = result
			return result
		else:
			return cache[key]
	return wrapper

@memoize
def L(state):
	if len(state) == 1:
		return state[0]
	elif len(state) == 2:
		a, b = state[0], state[1]
		return b if a < b else 0
	else:
		w, b = state[:-1], state[-1]
		return L(w) - R(w) + b if b > R(w) else 0

@memoize
def R(state):
	if len(state) == 1:
		return state[0]
	elif len(state) == 2:
		a, b = state[0], state[1]
		return a if b < a else 0
	else:
		a, w = state[0], state[1:]
		return R(w) - L(w) + a if a > L(w) else 0

if __name__ == "__main__":
	text_state = input("state: ")
	state = [int(num_string) for num_string in text_state.split(" ")]
	print("w = " + " ".join(str(num) for num in state))
	print("L(w) = " + str(L(state)))
	print("R(w) = " + str(R(state)))
