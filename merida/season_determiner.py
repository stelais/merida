"""
DRAFT CODE: It identifies the season of a given data point
It work but the intervals were just hard coded
"""

# HARD CODED
seasons_intervals = {'2006': (3810.0, 4070.0),
                     '2007': (4120.0, 4430.0),
                     '2008': (4480.0, 4800.0),
                     '2009': (4840.0, 5160.0),
                     '2010': (5210.0, 5530.0),
                     '2011': (5580.0, 5890.0),
                     '2012': (5940.0, 6260.0),
                     '2013': (6310.0, 6620.0),
                     '2014': (6670.0, 6980.0)}
#
peaks = [6425.0, 3931.0, 3892.0, 4656.0, 3930.0, 4735.0,
         5428.0, 6021.0, 4240.0, 3976.0, 4080.0, 4550.0, 4213.0,
         6063.0, 4644.0, 5810.0, 4523.0, 6892.0, 5490.0, 5806.0, 5090.0,
         6899.0, 6600.0, 3937.0, 6501.0, 6020.0, 6585.0, 6455.0, 6424.0,
         4650.0, 5090.0, 6532.0, 6096.0, 5705.0, 4635.0, 4697.0, 6451.0,
         6048.0, 4591.0, 6526.0, 6111.0, 5311.0, 5364.0, 4015.0, 5318.0,
         6054.0, 6891.0,]

# Find the season for each peak
peak_seasons = {}
for peak in peaks:
    for season, (start, end) in seasons_intervals.items():
        if start <= peak <= end:
            peak_seasons[peak] = season
            break

print()
# print(peak_seasons)
for key, value in peak_seasons.items():
    print(f"{key}: {value}")