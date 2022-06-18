
unsorted_list = [64, 25, 12, 22, 11]
sorted_list = unsorted_list


#
# idx1 is the pass index for sorting
#
# idx2 is the selection index
#
list_length = len( sorted_list )

for idx1 in range( 0, list_length-1):

    #
    # STEP 1: intialization
    #
    the_largest_value = sorted_list[idx1]
    the_largest_index = idx1

    #
    # STEP 2:find the next smallest value and its position
    #
    for idx2 in range( idx1+1, list_length ):
        if( the_largest_value > sorted_list[idx2] ):
            the_largest_value = sorted_list[idx2]
            the_largest_index = idx2

    #
    # Step 3: swap the smallest value from it unsorted position to its sorted position
    #
    temporal_value = sorted_list[idx1]
    sorted_list[idx1] =  the_largest_value
    sorted_list[the_largest_index] = temporal_value

    print( "Pass %d  "%(idx1), sorted_list )
