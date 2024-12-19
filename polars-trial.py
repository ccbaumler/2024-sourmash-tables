#! /usr/bin/env python

import polars as pl
import sys
import io

# Thanks to https://gist.github.com/bitsnaps/aa83219c4ffdd04e56b76bb23523bfb2

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

s_df = pl.DataFrame({'match': ['a bd', 'a fg', 'b wo', 'b fg', 'c po', 'c hj', 'f no'], 'A': [1, 2, 2, 3, 3, 4, 5], 'B': ['4', '4', '5', '5', '6', '7', '5']})

t_df = pl.DataFrame({'ident': ['a', 'b', 'c', 'd'], 'family': ['yup', 'correct', 'right0', 'super']})

print(s_df)
print(t_df)

# Extract the portion before the first whitespace in 'match' using str.split and pl.first
s_df = s_df.with_columns(
    pl.col('match').str.split(' ').list.get(0).alias('match_key'),
    pl.col('match').str.split(' ').list.get(1).alias('match_value')
)

print(s_df)

# Perform the join on 'match' and 'ident'
merged_df = s_df.join(t_df, left_on='match_key', right_on='ident', how='left')

print(merged_df)

missing_df = merged_df.filter(pl.col("family").is_null()).drop(['match_key','match_value', 'family'])
print(missing_df)

# Drop the 'match' and 'ident' columns and rename 'family' to 'match'
final_df = merged_df.drop(['match_key', 'match_value', 'match']).rename({'family': 'match'})

# Show the final DataFrame
print(final_df)

print(final_df.group_by('match').agg(pl.sum("A")))
print(final_df)

keep = ['family', 'A']

print(merged_df.drop([pl.exclude(keep)]).drop_nulls().rename({'family': 'match'}).group_by('match').agg(pl.sum("A")))
