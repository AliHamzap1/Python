
# my $string = "alihamza ali hamza moazzam ali moazzam ali";
# my %seen;
# my $result = join ' ', grep { !$seen{$_}++ } split /\s+/, $string;
# print "$result\n";


# while ($string) {
#    chomp;
#    my @words = split;
# }

# my %seen;
# my @unique = grep { ! $seen{$_}++ } @words;
# print "$unique\n";


# my $string = "ali/hamza, ali hamza Naveed;naveed- moazzam.moazzam ali ali";
# my %seen;

# # Normalize all separators to spaces and split
# my @words = split /\W+/, $string;

# # Filter duplicates
# my $result = join ' ', grep { !$seen{$_}++ } @words;

# print "$result\n";


my $string = "ali/hamza, ali hamza Naveed;naveed- moazzam.moazzam ali ali:Naveed mujeeb-mujeeb";
my %seen;

my @words = split /\W+/, $string;
my $result = join ' ', grep { !$seen{$_}++ } @words;

print "$result\n";