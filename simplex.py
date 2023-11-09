import numpy as np

simplex_tab = np.array([
    [1,-5,-4,-3,0,0,0,0],
    [0,2,3,1,1,0,0,5],
    [0,4,1,2,0,1,0,11],
    [0,3,4,2,0,0,1,8]
], dtype=float)


def simplex_pass(pivot_row_cache:list=None):
    pivot_col_idx = np.argmin( simplex_tab[0,:] )
    tmp_right_side = np.round(np.abs(simplex_tab[1:, -1]/simplex_tab[1:, pivot_col_idx]),4)
    tmp_right_side[tmp_right_side==np.nan]=0
    min_right_side = np.min( tmp_right_side )
    # print(f'{tmp_right_side = }, {min_right_side = }')
    if pivot_row_cache is not None:
        possible_pivots = np.where( tmp_right_side == min_right_side )[0]
        # print(f'{possible_pivots = }')
        if len(possible_pivots) == 1:
            pivot_row_idx = possible_pivots[0]
        elif len(possible_pivots)>1:
            for ppivot in possible_pivots:
                if ppivot not in pivot_row_cache:
                    pivot_row_idx = ppivot
                    break
            else:
                pivot_row_idx ,= np.random.choice( possible_pivots, 1 )
        pivot_row_cache.append( pivot_row_idx )
    else:
        pivot_row_idx,=np.random.choice( np.where( tmp_right_side == min_right_side )[0], 1 )
    pivot_row_idx+=1
    div_el = simplex_tab[pivot_row_idx, pivot_col_idx]
    simplex_tab[pivot_row_idx, :] /= div_el
    for i in range( simplex_tab.shape[0] ):
        if i == pivot_row_idx: continue
        simplex_tab[i,:] -= simplex_tab[i, pivot_col_idx]*simplex_tab[pivot_row_idx, :]
    return pivot_row_idx, pivot_col_idx, pivot_row_cache

pivot_cache=[]
while np.sum(simplex_tab[0,:]<0)!=0:
    simplex_pass(pivot_cache) 


print(simplex_tab)