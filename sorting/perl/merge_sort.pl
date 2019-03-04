package sorting;
use Exporter;
@ISA = ('Exporter');
@EXPORT = ('merge_sort');

sub merge_sort {
	my $array = shift @_;
	m_sort($array, 0, $$array);
}

sub m_sort {
	my ($array, $start, $end) = @_;
	if($end - $start > 1) {
		my $middle = int(($start + $end) / 2);
		m_sort($array, $start, $middle);
		m_sort($array, $middle, $end);
		merge($array, $start, $middle, $end);
	}
}

sub merge {
	my ($array, $start, $middle, $end) = @_;
	my @tmp;
	my ($i, $j) = ($start, $middle);
	while($i < $middle and $j < $end) {
		if($$array[$i] < $$array[$j]) {
			push @tmp, $$array[$i++];
		} else {
			push @tmp, $$array[$j++];
		}
	}
	while($i < $middle) {
		push @tmp, $$array[$i++];
	}
	while($j < $end) {
		push @tmp, $$array[$j++];
	}
	for(my $i = $start; $i < $end; $i++) {
		$$array[$i] = $tmp[$i - $start];
	}
}

1;
