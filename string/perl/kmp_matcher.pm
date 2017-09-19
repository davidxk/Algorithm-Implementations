#!/usr/bin/perl

package kmp_matcher;

use strict;
use warnings;
use Exporter;
our @ISA = qw(Exporter);
our @EXPORT = qw(kmp_matcher);

sub get_char_at {
	my ($string, $index) = @_;
	return substr $string, $index, 1;
}

sub kmp_matcher {
	my ($text, $pattern) = @_;
	my @pi = compute_prefix_function($pattern);
	my $matched = 0;
	for(my $i = 0; $i < length($text); $i++) {
		while($matched > 0 and 
			get_char_at($text, $i) ne get_char_at($pattern, $matched)) {
			$matched = $pi[$matched - 1];
		}
		if(get_char_at($text, $i) eq get_char_at($pattern, $matched)) {
			$matched++;
		}
		if($matched == length($pattern)) {
			return $i - $matched + 1;
		}
	}
	return -1;
}

sub compute_prefix_function {
	my $pattern = shift;
	my @pi = (0); 
	my $matched = 0;
	for(my $i = 1; $i < length($pattern); $i++) {
		while($matched > 0 and
			get_char_at($pattern, $i) ne get_char_at($pattern, $matched)) {
			$matched = $pi[$matched - 1];
		}
		if(get_char_at($pattern, $i) eq get_char_at($pattern, $matched)) {
			$matched++;
		}
		$pi[$i] = $matched;
	}
	return @pi;
}

1;
