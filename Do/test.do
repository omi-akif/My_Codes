mata:
mata clear

void test(){
	st_view(x, ., "x")
	x
	stata("drop y")
	x
}

end

clear
set obs 5
gen y = 1
gen x = 2
mata: test()
