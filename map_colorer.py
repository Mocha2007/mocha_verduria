# 1;255;255;0;West Erelae;x
# used to determine map colors so I don't accidentally dupe

def definition_csv(n: int, is_land: bool = True) -> str:
	n_ = n * 64 # oscillate between red, vermillion, orange, amber, and back
	green = n_ % 255 # deliberately excluding 255
	red_or_blue = n_ // 255
	return f"{n};255;{green};{red_or_blue};PROV_NAME;x" if is_land \
		else f"{n};{red_or_blue};{green};255;Sea;x"

def test() -> None:
	for i in range(100):
		print(definition_csv(i + 1))