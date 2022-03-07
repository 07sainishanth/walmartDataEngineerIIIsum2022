### Movie Theater Seating Challenge ###

-- Language used : Python ((v2.7 or above)  or (v3.10 or above))

-- Environment and code for setup -- Download python 2 or 3, clone the git repository, and open terminal in the repsoitory location .


-- command for execution : python main.py \<input file path\>

-- Expected outout : \<output file path\>


## Algo ## 

1. Check if request is valid or not.
2. Check if requested no of seats are available or not.
3. Check if all the requested scenes can be reserved in a single row starting from farthest row from screen.
4. if available allocate.
5. In case all seats are not available in one row allocate available seats in each row from farthest row from screen.



## Assumptions ##

-- Priority to tickets farthest from the screen

-- Priority to find all seats side by side

-- In case not able to find all seats side by side allocate seats available in each row farthest from the screen

-- Can't register more than total no of columns seats in one booking