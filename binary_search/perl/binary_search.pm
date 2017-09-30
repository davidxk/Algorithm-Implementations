package binary_search;
use Exporter;
@ISA = ('Exporter');
@EXPORT = ('binary_search');

sub binary_search {
	my ($array, $target) = @_;
	my ($left, $right) = (0, $#{$array});
	while($left <= $right) {
		my $center = int(($left + $right) / 2);
		if($$array[$center] == $target) {
			return $center;
		} elsif($$array[$center] < $target) {
			$left = $center + 1;
		} else {
			$right = $center - 1;
		}
	}
	return -1;
}

1;
