#!/usr/bin/perl

use strict;
use warnings;
use kmp_matcher;

sub gen_str {
	my $size = shift;
	my (@chars, $str);
	my @ATCG = qw(A T C G);
	for(0 .. $size) {
		push @chars, $ATCG[int(rand(4))];
	}
	$str = join '', @chars;
	return $str;
}

sub test_str_matcher {
	my $text;
	my $pattern;
	for(1 .. 1000) {
		$text =  gen_str(2000);
		$pattern = gen_str(5);
		if(kmp_matcher($text, $pattern) != index($text, $pattern)) {
			return 0;
		}
	}
	return 1;
}

sub main {
	if(not test_str_matcher()) {
		print "WA: kmp_matcher\n";
	}
}

main()
