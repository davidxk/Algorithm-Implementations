from test_sort_impl import check_sort_impl
from quick_sort_hoare import quick_sort_hoare
from quick_sort_pure import quick_sort_pure
from quick_sort_hpure import quick_sort_hpure
import sys

cnt = 0
while check_sort_impl(quick_sort_pure):
    cnt += 1
    sys.stdout.write("\r" + str(cnt))
