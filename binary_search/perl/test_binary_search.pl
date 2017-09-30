#!/usr/bin/perl

use strict;
use warnings;
use binary_search;

sub test_binary_search {
	my $size = 10_000;
	my @array = (0 .. $size);
	for(0 .. 100) {
		my $pick = int(rand($size));
		my $retval = binary_search(\@array, $pick);
		my ($expect) = grep{ $array[$_] == $pick } @array;
		return 0 if $retval != $expect;
	}
	return 1;
}

sub main {
	if(not test_binary_search()){
		print "WA: binary_search"
	}
}

main()
